import openai
import discord

openai.api_key = "YOUR_OPENAI_API_KEY"

client = discord.Client()

@client.event
async def on_message(message):
    # Only respond to messages from other users, not the bot itself
    if message.author == client.user:
        return

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{message.author.mention} says: {message.content}\n",
        max_tokens=1024,
        temperature=0.5,
    ).get("choice").get("text")

    await message.channel.send(response)

client.run("DISCORD_BOT_TOKEN")
