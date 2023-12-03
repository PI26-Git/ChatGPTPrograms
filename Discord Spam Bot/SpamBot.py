import discord
import asyncio

# Your Discord bot token
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# Create an instance of Intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent, required for reading message content

# Create a Discord client with Intents
client = discord.Client(intents=intents)

# The channel ID where you want the bot to send messages
channel_id = 123456789012345678  # Replace with your channel ID

# The time interval in seconds between messages
interval_seconds = 60  # Replace with your desired interval

# Function to send a message to the specified channel
async def send_message():
    channel = client.get_channel(channel_id)
    await channel.send("Hello, this is a scheduled message!")

# Event triggered when the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # Schedule the initial message
    await send_message()

    # Schedule repeated messages
    while True:
        await asyncio.sleep(interval_seconds)
        await send_message()

# Run the bot with the specified token
client.run(TOKEN)
