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
            v1: Option(float, "Initial Velocity in m/s", required=False),
            v2: Option(float, "Final Velocity in m/s", required=False),
            d: Option(float, "Displacement in m", required=False),
            a: Option(float, "Acceleration in m/s^2", required=False),
            t: Option(float, "Time in s", required=False),
            ):
        print(v1, v2, d, a, t)

def setup(client):
    client.add_cog(Equation(client))
