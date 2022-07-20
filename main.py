import discord

bot = discord.Client()


@bot.event
async def on_ready():
    print("bot is online")


@bot.event
async def on_message(msg):

    username = msg.author.display_name

    if msg.author == bot.user:
        return
    else:
        if msg.content == "hello":
            await msg.channel.send("hello " + username)

@bot.event
async def on_member_join(member):
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f"Welcome to {guildname}!")






bot.run("OTk4OTAyMzQzNjU3NjA3MjA5.G0BcEL.PZkyiyvmSRRecDfSI1lpCWd-hzMK-ebhUj1HE4")

