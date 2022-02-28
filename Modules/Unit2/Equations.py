from typing_extensions import Required
import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from typing import Optional

class Equation(commands.Cog):
    

    def __init__(self, client):
        self.client = client


    @slash_command(
        name="ueq",
        description="Using Any of the values you have given, solve the rest.",
    )
    async def ueq(
            self, 
            ctx,
            v1: Option(float, "Initial Velocity in m/s", required=False) = None,
            v2: Option(float, "Final Velocity in m/s", required=False) = None,
            d: Option(float, "Displacement in m", required=False) = None,
            a: Option(float, "Acceleration in m/s^2", required=False) = None,
            t: Option(float, "Time in s", required=False) = None,
            ):
        #V1, v2, d, a, t
        if v1 and a and t:
            v2 = v1 + a*t
            d = v1*t + 0.5*a*t**2
        elif v1 and v2 and d:
            a = (v2 - v1)/t
            t = d/v1 - 0.5*a*t
        elif v1 and v2 and a:
            t = (v2 - v1)/a
            d = v1*t + 0.5*a*t**2
        elif v1 and d and a:
            t = d/v1 - 0.5*a*t
            v2 = v1 + a*t
        elif v1 and d and t:
            v2 = v1 + a*t
            a = (v2 - v1)/t
        elif v1 and v2 and t:
            a = (v2 - v1)/t
            d = v1*t + 0.5*a*t**2
        elif t and d and v2:
            v1 = v2 - a*t
            a = (v2 - v1)/t
        embed = discord.Embed(title="Uniform Equation", description="", color=0x00ff00)
        embed.add_field(name="Initial Velocity", value=f"{v1} m/s", inline=False)
        embed.add_field(name="Final Velocity", value=f"{v2} m/s", inline=False)
        embed.add_field(name="Acceleration", value=f"{a} m/s^2", inline=False)
        embed.add_field(name="Time", value=f"{t} s", inline=False)
        embed.add_field(name="Displacement", value=f"{d} m", inline=False)
        await ctx.respond(embed=embed)
        

def setup(client):
    client.add_cog(Equation(client))
