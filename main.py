import random

import discord

token = ""

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
spots = ["Glenn L Martin", "Ellicott/Stadium Garage", "PSC Rail Spot", "Tawes/Art Soc", "Nyumburu Amphitheater",
                 "Cecil/Montgomery", "Van Munching", "McKeldin Mall", "Tydings", "St. Mary's", "Armory", "Yahenta Stairs",
                 "Rossborough Inn", "Plant Science/Hornbake", "Bagels N Grinds/The Hotel", "LeFrak Hall", "Queen Anne's",
         "Kim Engineering", "nowhere; decide yourself"]
pool = list(spots)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    # print("message received")
    username = str(message.author).split("#")[0]
    # print(message)
    user_message = str(message.content)
    channel = str(message.channel.name)
    # print(f'{username}: {user_message} ({channel})');

    if message.author == client.user:
        return
    elif user_message.lower() == "^decide":
        num = random.randrange(0, len(spots), 1)
        await message.channel.send(f"Foolish indecisive monkes, you will be monkeying at {spots[num]}!!!")
        return
    elif user_message.lower() == "^sample":
        if len(pool) == 0:
            for spot in spots:
                pool.append(spot)
            await message.channel.send(f"Pool emptied, refilling")
        num = random.randrange(0, len(pool), 1)
        await message.channel.send(f"Foolish indecisive monkes, you will be monkeying at {pool[num]}!!! ({pool[num]} removed from pool)")
        pool.remove(pool[num])
        return
    elif user_message.lower() == "^pool":
        messageStr = ""
        for x in pool:
            messageStr += x +"\n"
        await message.channel.send(f"Foolish indecisive monkes, here is a list of spots to practice at: \n" + messageStr)
    elif user_message.lower()[0:5] == "^pick":
        choices = user_message.lower()[5:].strip().split(",")
        num = random.randrange(0, len(choices), 1)
        await message.channel.send(
            f"Foolish slightly decisive monkes, you will be monkeying at {choices[num].strip()}!!!")
        return
    elif user_message.lower()[0:6] == "^order":
        choices = user_message.lower()[6:].strip().split(",")
        messageStr = ""
        while len(choices) > 0:
            num = random.randrange(0, len(choices), 1)
            messageStr += str(choices[num]) + ", "
            choices.pop(num)
        await message.channel.send(
            f"Foolish indecisive monkes, here is your random order of items: {messageStr.strip(', ')}!!!")
        return
    elif user_message.lower()[0:7] == "^random":
        bounds = user_message.lower()[7:].strip().split(",")
        messageStr = "Your indecisive random number is: "
        if len(bounds) == 1:
            messageStr += str(random.randrange(0, int(bounds[0])) + 1)
        elif len(bounds) > 2:
            messageStr = "No indecisive random number for you because you're foolish and put in too many parameters";
        else:
            messageStr += str(random.randrange(int(bounds[0]), int(bounds[1])))
        await message.channel.send(messageStr)
        return
    elif user_message.lower() == "^list":
        messageStr = ""
        for x in spots:
            messageStr += x +"\n"
        await message.channel.send(f"Foolish indecisive monkes, here is a list of spots to practice at: \n" + messageStr)
    elif user_message.lower() == "^help":
        await message.channel.send(
            f"Foolish indecisive monkes, here are my commands:\n\
- ^decide: Selects from a set list of practice locations (with replacement)\n\
- ^sample: Selects a spot from a pool of practice locations (without replacement)\n\
- ^pool: Displays the current pool of spots that ^sample calls from\n\
- ^pick (a, b, c): Selects from given parameters (separate with commas)\n\
- ^random (a,b): Selects a random number between a and b (or 0 and a if b not given)\n\
- ^order (a,b,c): Returns a random ordering of given items (separate with commas)\n\
- ^list: Returns a list of spots to practice at")
        return

client.run(token)
