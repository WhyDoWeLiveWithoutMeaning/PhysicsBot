import matplotlib.pyplot as plt
import numpy as np

import discord
from discord.ext import commands

class RampLab(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rampLab(self, ctx, *expression):
        with ctx.typing():
            nums = [float(x.strip()) for x in "".join(expression).split(",")]

            ## INPUTS
            time = np.arange(0, 1.6, 0.1)
            midTime = np.insert(np.arange(0.05, 1.55, 0.1), 0, 0)
            displacement = np.array(nums)

            # POSITION
            position = [0]
            i = displacement[0]
            for j in range(len(displacement)-1):
                i += round(displacement[j+1], 2)
                position.append(i)

            # INTERVAL VELOCITY
            intervalVelocity = [0]
            for i in range(len(position)-1):
                intervalVelocity.append(
                    round((position[i+1]-position[i])/(time[i+1]-time[i])))

            # PLOT P-T GRAPH
            a, fig = plt.subplots(1, 3)

            fig[0].grid(True, 'both')
            fig[0].fill_between(time, position, 0, color='skyblue')
            fig[0].plot(time, position)
            fig[0].set_xlabel('Time (s)')
            fig[0].set_ylabel('Position (m) [fwd]')
            fig[0].set_title('Position vs. Time')

            # PLOT V-T GRAPH
            # m represents the slope of the line of best fit
            m, b = np.polyfit(midTime, intervalVelocity, 1)

            fig[1].grid(True, 'both')
            fig[1].plot(midTime, m*midTime+b, 'r')
            fig[1].fill_between(midTime, m*midTime+b, 0, color='skyblue')
            fig[1].scatter(midTime, intervalVelocity)
            fig[1].set_xlabel('Time (s)')
            fig[1].set_ylabel('Velocity (m/s) [fwd]')
            fig[1].set_title('Velocity vs. Time')

            # PLOT A-T GRAPH
            g = [m for _ in range(0, 16, 1)]

            fig[2].grid(True, 'both')
            fig[2].set_ylim(0, 80)
            fig[2].set_xlabel('Time (s)')
            fig[2].set_ylabel('Acceleration (m/s^2) [fwd]')
            fig[2].set_title('Acceleration vs. Time')
            fig[2].plot(time, g)
            fig[2].fill_between(time, g, 0, color='skyblue')

            # SEND GRAPHS
            a.set_figwidth(17)

            plt.savefig("graph.png", dpi=300, papertype='a4', orientation='landscape', bbox_inches='tight', pad_inches=0.1)

            embed = discord.Embed(title = ctx.author.name + "'s Ramp Lab", description = "")
            embed.set_image(url = "attachment://graph.png")

            # Calculate Area
            area = 0
            if b>0:
                area = round(((b + (m*time[-1]+b))*(time[-1]-time[0]))/2)
            else:
                x = (0-b)/m
                area = round(((time[-1]-x)*(time[-1]-time[0]))/2)
            
            embed.add_field(name = "Equation of Line of best fit", value = "y = " + str(round(m,2)) + "x + " + str(round(b,2)))
            embed.add_field(name = "Area Under the Curve", value = str(round(area, 2)) + "cm [fwd]", inline = False)
            errorP = abs(((area - position[-1])/position[-1])*100)
            embed.add_field(name = "Error Percent", value = str(round(errorP, 2)) + "%", inline = False)
            await ctx.send(embed=embed, file=discord.File("graph.png"))
    
    @rampLab.error
    async def rampLab_error(self, ctx, error):
        await ctx.send("Please enter a comma-separated list of numbers")
    

def setup(client):
    client.add_cog(RampLab(client))