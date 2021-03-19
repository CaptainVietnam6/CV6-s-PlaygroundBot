#imports related to discord or discord packages
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import cooldown
from discord.ext.commands import BucketType
from discord import FFmpegPCMAudio

#other important imports for system
import os
from os import system
import random
from random import randint
import time
import youtube_dl
import shutil
import asyncio
import PyDictionary
from PyDictionary import PyDictionary

#imports from other files
from keep_alive import keep_alive
from BOT_TOKEN import BOT_TOKEN


'''REFER TO NOTES TO UNDERSTAND CODE BETTER AND USE IT AS A INDEX TO SEE WHERE CERTAIN COMMAND CLASSES ARE'''


'''START OF IMPORTANT STUFF, DEALS WITH BOT AND INTERNAL COMMANDS'''


#INTENTS
intents = discord.Intents().all()


#PREFIX THE BOT USES
bot_prefixes = ["cv6 ", "CV6 ", "cv6", "CV6", "/"]
client = commands.Bot(command_prefix = bot_prefixes, intents = intents)


#REMOVES DEFAULT HELP COMMAND
client.remove_command("help")


#LOAD cog
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


#UNLOAD cog
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


#RELOAD COG
@client.command()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")


#CONNECTS COGS FILE 
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


#ALERTS WHEN CV6's PlaygroundBot IS READY AND JOINS VC ON READY
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game("Programmed by CaptainVietnam6#0001 in Python 3.8.2"))
    await asyncio.sleep(3)
    print("CV6's PlaygroundBot is ready")

    #notifs for CV6's Playground server
    channel = client.get_channel(816179144961818634)
    await channel.send("CV6's PlaygroundBot is online")
    #notifs for CV6's Bots server
    channel = client.get_channel(812974446801059860)
    await channel.send("CV6's PlaygroundBot is online")

    #joins vc on ready
    channel = client.get_channel(815933179378270208)
    await channel.connect()


#RETURNS BOT'S PING IN MILLISECONDS
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong motherfucker {client.latency * 1000}ms")


#SERVER COLOR HEX CODE REMINDER THINGY
@client.command(aliases = ["serhexcode"])
async def _serverhexcode(ctx):
    await ctx.send("the server theme hex code is #ffa500")


#defines bot color for use in embeds
bot_color = 0xffa500


'''END OF IMPORTANT STUFF, DEALS WITH BOT AND INTERNAL COMMANDS'''

'''START OF MODERATION COMMANDS'''


#chat purge command cleared out as suspicion of passing rate limit
'''
#CHAT PURGE COMMAND
@client.command(aliases = ["clear", "Clear", "Purge", "purge"])
@commands.has_any_role("Admin", "Co-admin", "Moderator", "Staff", "staff-in-training")
@cooldown(1, 180, BucketType.default)
async def _chat_clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount + 1)
    await asyncio.sleep(float(1.5))
    await ctx.send (f"cleared {amount} messages from chat")
    await asyncio.sleep(float(0.5))
    await ctx.send("Please wait 3 minutes before using this command again :)")
'''


#AUTOROLE
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = "Playground Member")
    channel = client.get_channel(815915068654223371)
    mention = member.mention

    await member.add_roles(role)
    print("AutoRole: added a role to member")
    await channel.send(f"{mention} Welcome to CaptainVietnam6's playground! please have a look in <#815945790341775391> for our rules and <#816253845758803992> to give yourself some roles!")
    await channel.send("https://tenor.com/view/penguin-hello-hi-hey-there-cutie-gif-3950966")


#SEND BOT INVITE LINK COMMAND
@client.command(aliases = ["botinvite", "BotInvite", "Botinvite", "MBlink", "mblink"])
@cooldown(1, 60, BucketType.default)
async def _sendbotinvite(ctx):
    print("Someone requested bot invite link\n")
    await ctx.send("Sending bot's invite link!")
    await asyncio.sleep(float(0.5))
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=816184765065199667&permissions=0&scope=bot")


#RULES COMMAND
@client.command(aliases = ["rules", "Rules"])
@cooldown(1, 30, BucketType.default)
async def _therules(ctx):
    heart_emoji = "\u2764\ufe0f"
    embed = discord.Embed(
        title = "「Server rules」",
        description = "1. Use the correct channels, although quickly using bot commands in <#815915612378890280> is fine.\n2. Don't spam, use common sense, enforced by everyone.\n3. No nsfw unless in <#816243097716391956>.\n4. Keep your nickname respectful and unoffensive.\n5. Religion and politics are complex and controversial topics therefore should be best kept out of this server.\n6. No racial slurs or other racially offensive terms and or anything resembling it or meant to carry the same meaning.\n7. Be respectful to others, no discrimination unless it's meant as a joke and both parties reconise it as one.\n8. Head over to <#816253845758803992> to select your custom roles.\n9. Use common sense and you'll be fine, don't try find loopholes in my rules and don't be a smartass about it.",
        color = bot_color
    )
    embed.set_footer(text = f"Bot and rules made with love by CaptainVietnam6{heart_emoji}")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/815915612378890280/816274373089951764/20210301_211313.jpg")
    await ctx.send(embed = embed)


#HELP COMMAND
@client.group(invoke_without_command = True, aliases = ["help", "Help"])
async def _help(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Help command categories**",
        description = "**These are the commands you can run to see the list of commands in each category.**\n\nFun commands: **cv6 help fun**\nMusic commands: **cv6 help music**\nSoundboard commands: **cv6 help sb**\nGame commands: **cv6 help game**\nEmoji commands: **cv6 help emoji**\nModeration commands: **cv6 help mod**\n",
        color = bot_color
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - FUN COMMANDS
@_help.command(aliases = ["fun", "Fun"])
async def _help_fun(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Fun/responses related commands list**",
        description = "**These are commands that relate to fun or responses features of CV6's PlaygroundBot**\n\n8ball command: **cv6 8ball {question}**\nDice command: **cv6 dice**\nFranklin roast meme: **/loc**\nMeme command: **cv6 meme**\nHow-to-use-google: **cv6 google**\nServer daddy: **cv6 daddy**\nBenice to staff: **cv6 benice**\nSend thigh pics: **cv6 thighpics**\nZeroTwo GIF: **cv6 zerotwo**\nDictionary: **cv6 dictionary {word}**\nSynonyms: **cv6 synonym {word}**\nAntonyms: **cv6 antonym {word}**\nRepeat after user: **cv6 repeat**\nWhat-a-legend: **cv6 legend**\nCapt Twitch link: **cv6 twitch**\nEw lightmode: **cv6 lightmode**\nReply spam: **cv6 spam {word}**\nPrint fancy text: **cv6 print {word}**\nSpeedrun profile: **cv6 speedrun {user name}**\nShut up GIF: **cv6 shut**\nDweam: **cv6 dweam**\nSends nothing: **cv6 nothing**\nDiscordmod meme: **cv6 discordmod**\nCusswords: **cv6 cusswords**\nFunny Pinged: **cv6 pinged**\nFair: **fair**\nPog: **pog**\nreee: **cv6 reee**\nSponsorMe: **cv6 sponsorme**\nCalculate Pi: **cv6 pi {enter digits}**",
        color = bot_color
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - MUSIC COMMANDS
@_help.command(aliases = ["music", "Music"])
async def _help_music(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Music related commands list**",
        description = "**These are commands that relate to music features of CV6's PlaygroundBot**\n\nJoin VC: **cv6 join**\nLeave VC: **cv6 leave**\nPlay song: **cv6 play (youtube url)**\nQueue song: **cv6 queue (youtube url)**\nPause music: **cv6 pause**\nResume music: **cv6 resume**\nStop music: **cv6 stop**\n",
        color = bot_color
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - SOUNDBOARD COMMANDS
@_help.command(aliases = ["sb", "Sb", "SB", "soundboard", "SoundBoard", "Soundboard"])
async def _help_soundboard(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Soundboard related commands list**",
        description = "**These are commands that relate to voice channel soundboard features of CV6's PlaygroundBot**\n\nJoin VC: **cv6 join**\nLeave VC: **cv6 leave**\nAirhorn: **cv6 sb airhorn**\nAli-a intro: **cv6 sb alia**\nBegone thot: **cv6 sb begonethot**\nDamn son where'd you find this: **cv6 sb damnson**\nDankstorm: **cv6 sb dankstorm**\nDeez nuts: **cv6 sb deeznuts**\nDeja Vu: **cv6 sb dejavu**\nLook at this dude: **cv6 sb dis_dude**\nAnother fag left the chat: **cv6 sb fleft**\nFart: **cv6 sb fart**\nHah gaaayyy: **cv6 sb hahgay**\nIt's called hentai and it's art: **cv6 sb henart**\nIlluminati song: **cv6 sb illuminati**\nBitch Lasagna: **cv6 sb lasagna**\nLoser: **cv6 sb loser**\nNoob: **cv6 sb noob**\nOof sound: **cv6 sb oof**\nPickle Rick: **cv6 sb picklerick**\nNice: **cv6 sb nice**\nWhy don't we just relax and turn on the radio: **cv6 sb radio**\nRick roll: **cv6 sb rickroll**\nThis is sparta: **cv6 sb sparta**\nTitanic flute fail: **cv6 sb titanic**\nGTA V Wasted: **cv6 sb wasted**\nWide Putin: **cv6 wideputin**\nWubba lubba dub dub: **cv6 sb wubba**\n",
        color = bot_color
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - GAME COMMANDS
@_help.command(aliases = ["game", "Game"])
async def _help_game(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Game related commands list**",
        description = "**These are commands that relate to game features of CV6's PlaygroundBot**\n\n8ball command: **cv6 8ball (your question)**\nDice command, returns 1-6: **cv6 dice**\nFranklin roast meme: **cv6 loc**\nRock Paper Scissors: **cv6 rps (rock, paper, or scissors)**\nMeme command: **cv6 meme**\nHentai command: **cv6 hentai**\n",
        color = bot_color
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - EMOJI COMMANDS
@_help.command(aliases = ["emoji", "Emoji"])
async def _help_emoji(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Emoji related commadns list**",
        description = "**The commands with an $ have an auto detection feature to detect a certain keyword in your message**\n\nSo fake$: **cv6 fake**\nX to doubt$: **cv6 doubt**\nStonks$: **cv6 stonks**\nSimp pill$: **cv6 simp**\nUwU*: **cv6 uwu**\nWat: **cv6 wat**\nAdmin abooz: **cv6 abooz**\n60s Timer$: **cv6 timer**\nThats racist$: **cv6 racist**\nPolice$: **cv6 police**\nF-spam emoji: **cv6 fpsam**\nClap emoji: **cv6 clap**\nYou tried: **cv6 youtried**\nPython logo: **cv6 python**\nPepe pog: **cv6 pepepog**\nGay flag$: **cv6 gay**\nBisexual flag$: **cv6 bisexual**\nTrans flag$: **cv6 trans**",
        color = bot_color
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - MODERATION COMMANDS
@_help.command(aliases = ["mod", "Mod", "moderation", "Moderation"])
async def _help_moderation(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Moderation related commands list**",
        description = "**These are commands that relate to moderation features of CV6's PlaygroundBot, most require administrative powers**\n\nWelcome command: **cv6 welcome**\nDescription command: **cv6 description**\nBot description: **cv6 botdesc**\nKick command: **cv6 kick (tag member, reason)**\nBan command: **cv6 ban (tag member, reason)**\nPurge/clear chat: **cv6 clear (number of messages)**\nBot invite link: **cv6 botinvite**\nHelp directory: **cv6 help**\n",
        color = bot_color
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)


#ANTI-SLUR & SLUR DETECTION COMMAND


'''END OF MODERATION COMMANDS'''

'''START OF TEST-BED COMMANDS OR COMMANDS FOR TESTING'''


#TEST COMMAND
@client.command(aliases = ["ban", "Ban", "kick", "Kick"])
async def _repeat(ctx):
    await ctx.send("shut up.")


#TEST COMMAND 2
@client.command(aliases = ["website", "Website"])
async def _captswebsite(ctx):
    await asyncio.sleep(float(0.1))
    await ctx.send("Sending website...")
    await asyncio.sleep(float(1.5))
    await ctx.send("https://Basic-Website-7.itzkiettttt.repl.co")


'''END OF TEST-BED COMMANDS OR COMMANDS FOR TESTING'''

'''START OF MUSIC AND VOICE CHANNEL RELATED COMMANDS'''


#VOICE CHANNEL JOIN
@client.command(pass_context = True, aliases = ["Join", "join", "j", "J", "connect", "Connect"])
async def _join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send("I have joined your voice channel")
        print("CV6's PlaygroundBot joined a voice channel")


#VOICE CHANNEL LEAVE
@client.command(pass_context = True, aliases = ["Leave", "leave", "L", "l", "Disconnect", "disconnect"])
async def _leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"CV6's PlaygroundBot is disconnected from {channel} voice channel")
        await ctx.send(f"I have left the '{channel}' voice channel")
    else:
        print("command given to leave voice channel but bot wasn't in a voice channel")
        await ctx.send("Invalid command: the bot wasn't in any voice channels")


#VOICE CHANNEL PLAY YOUTUBE URL
@client.command(pass_context = True, aliases = ["play", "Play", "p", "P"])
async def _play(ctx, url: str):
    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_queue = length - 1 #outprints how many are left in queue after new song is played
            try:
                first_file = os.listdir(DIR)[0] #first file inside directory
            except:
                print("No more songs left in queue\n")
                queues.clear
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "//" + first_file)
            
            if length != 0:
                print("Sone finished playing, loading next song\n")
                print(f"Number of songs still in queue: {still_queue}")
                is_song_there = os.path.isfile("song.mp3")
                if is_song_there: 
                    os.remove("song.mp3")
                shutil.move(song_path, main_location) #moves queued song to main directory
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                vcvoice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e: check_queue()) #plays the song
                vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
                vcvoice.source.value = 0.05
            
            else: #if queues = 0, clearns it
                queues.clear()
                return

        else: #is there is no queue folder
            queues.clear()
            print("No songs queued after the last song\n")

    #end of queue section thingy for play command
    is_song_there = os.path.isfile("song.mp3")
    try: #code will try to remove song, if it's playing then no remove
        if is_song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed an old song file")
    except PermissionError:
        print("Failed to remove song file, song file in use")
        ctx.send("Error: song file cannot be removed because it's currently playing")
        return

    #this section is here to remove the old queue folder
    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:   #if there is an old queue file, it will try to remove it
            print("Removed old queue folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old queue folder")

    #rest of play command to play songs
    await ctx.send("Getting everything ready to play, this may take a bit to load")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "512",
        }], #code above to specify options in ydl
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloaded audio file\n")
        ydl.download([url])
    #renames file name 
    for file in os.listdir("./"): #./ for current directory
        if file.endswith(".mp3"):
            audio_file_name = file
            print(f"Renamed File {file}\n")
            os.rename(file, "song.mp3")
    #checks to see if audio has finished playing, after then it will print
    vcvoice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e: check_queue())
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05
    new_name = audio_file_name.rsplit("-", 2)
    await ctx.send(f"Now Playing {new_name}")
    print("playing\n")


#VOICE CHANNEL MUSIC PAUSE COMMAND
@client.command(pass_context = True, aliases = ["pause", "Pause"])
async def _pause(ctx):
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    
    if vcvoice and voice.is_playing():
        vcvoice.pause()
        print("Music paused")
        await ctx.send("Music paused")
    else:
        print("Music wasn't playing but there was a request to pause music")
        await ctx.send("There was no music wasn't playing so i can't pause it")


#VOICE CHANNEL MUSIC RESUME COMMAND
@client.command(pass_context = True, aliases = ["resume", "Resume"])
async def _resume(ctx):
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    
    if vcvoice and voice.is_paused():
        vcvoice.resume()
        print("Music resumed")
        await ctx.send("Music has been resumed pogs")
    else:
        print("Music was not paused but a request was sent for music pause")
        await ctx.send("Music was playing, can't be resumed if it wasn't paused")


#VOICE CHANNEL MUSIC STOP COMMAND
@client.command(pass_context = True, aliases = ["stop", "Stop"])
async def _stop(ctx):
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    queues.clear() #clears queue when stop command ran

    if vcvoice and voice.is_playing():
        vcvoice.stop()
        print("Music stopped")
        await ctx.send("Music stopped")
    else:
        print("Music could not be stopped")
        await ctx.send("Music can't be stopped if there isn't music playing")


#VOICE CHANNEL MUSIC queue
#this command is for music to be queued up if you use the "cv6 play" multiple times while music is still playing
queues = {}

@client.command(pass_context = True, aliases = ["Queue", "queue", "Q", "q"])
async def _queue(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")      #sees if there is any song files in queue, if there is any then it counts them
    DIR = os.path.abspath(os.path.realpath("Queue"))
    queue_num = len(os.listdir(DIR)) #gets/counts ammount of files in the queue
    queue_num += 1 #adds another to queue
    add_queue = True
    while add_queue:
        if queue_num in queues:
            queue_num += 1
        else:
            add_queue = False
            queues[queue_num] = queue_num

    queue_path = os.path.abspath(os.path.realpath("Queue") + f"//song{queue_num}.%(ext)s")
    #takes the real path of song in queue and number of it
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl" : queue_path,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "512",
        }], #code above to specify options in ydl
    }
    #downloads song and puts into queue path above ^
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloaded audio file\n")
        ydl.download([url])
    await ctx.send("Adding song " + str(queue_num) + " to the queue")
    print("added a song to queue\n")


'''END OF MUSIC AND VOICE CHANNEL RELATED COMMANDS'''

'''START OF VOICE CHANNEL SOUNDBOARD COMMANDS'''


#old soundboard command, this is a singular command and doesn't rely on groups and subcommands
'''
@client.command(pass_context = True, aliases = ["airhorn", "Airhorn"])
async def _soundboard_airhorn(ctx):
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/airhorn.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05
'''

#soundboard command format; copy for future use, switch out airhorn with whatever, 2nd one already has that done
'''
@_soundboard.command(aliases = ["airhorn", "Airhorn"])
async def _soundboard_airhorn(ctx):
    await ctx.send("Playing **airhorn** sound effect from soundboard")
    print("\nPlayed airhorn sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/airhorn.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

@_soundboard.command(aliases = [""])
async def _soundboard_(ctx):
    await ctx.send("Playing **** sound effect from soundboard")
    print("\nPlayed  sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05
'''


#SOUNDBOARD COMMAND GROUP & HELP
@client.group(invoke_without_command = True, aliases = ["sb", "SB", "soundboard", "Soundboard", "SoundBoard"])
async def _soundboard(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Soundboard commands list**",
        description = "**These are commands that relate to voice channel soundboard features of CV6's PlaygroundBot**\n\nJoin VC: **cv6 join**\nLeave VC: **cv6 leave**\nAirhorn: **cv6 sb airhorn**\nAli-a intro: **cv6 sb alia**\nBegone thot: **cv6 sb begonethot**\nDamn son where'd you find this: **cv6 sb damnson**\nDankstorm: **cv6 sb dankstorm**\nDeez nuts: **cv6 sb deeznuts**\nDeja Vu: **cv6 sb dejavu**\nLook at this dude: **cv6 sb dis_dude**\nAnother fag left the chat: **cv6 sb fleft**\nFart: **cv6 sb fart**\nHah gaaayyy: **cv6 sb hahgay**\nIt's called hentai and it's art: **cv6 sb henart**\nIlluminati song: **cv6 sb illuminati**\nBitch Lasagna: **cv6 sb lasagna**\nLoser: **cv6 sb loser**\nNoob: **cv6 sb noob**\nOof sound: **cv6 sb oof**\nPickle Rick: **cv6 sb picklerick**\nNice: **cv6 sb nice**\nWhy don't we just relax and turn on the radio: **cv6 sb radio**\nRick roll: **cv6 sb rickroll**\nThis is sparta: **cv6 sb sparta**\nTitanic flute fail: **cv6 sb titanic**\nGTA V Wasted: **cv6 sb wasted**\nWide Putin: **cv6 wideputin**\nWubba lubba dub dub: **cv6 sb wubba**\n",
        color = bot_color
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)


#SB AIRHORN 
@_soundboard.command(aliases = ["airhorn", "Airhorn"])
async def _soundboard_airhorn(ctx):
    await ctx.send("Playing **airhorn** sound effect from soundboard")
    print("\nPlayed airhorn sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/airhorn.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB ALI-A SOUNDTRACK
@_soundboard.command(aliases = ["ali_a", "alia", "Ali-a", "Alia"])
async def _soundboard_ali_a(ctx):
    await ctx.send("Playing **ali_a** sound effect from soundboard")
    print("\nPlayed ali_a sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/ali_a.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB BEGONE THOT
@_soundboard.command(aliases = ["begone_thot", "begonethot", "Begone_thot", "Begonethot"])
async def _soundboard_begone_thot(ctx):
    await ctx.send("Playing **begone_thot** sound effect from soundboard")
    print("\nPlayed begone_thot sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/begone_thot.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DAMN SON WHERE'D U FIND THIS
@_soundboard.command(aliases = ["damn_son", "Damn_son", "damnson", "Damnson"])
async def _soundboard_damn_son(ctx):
    await ctx.send("Playing **damn_son** sound effect from soundboard")
    print("\nPlayed damn_son sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/damn_son.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DANKSTORM
@_soundboard.command(aliases = ["dankstorm", "Dankstorm"])
async def _soundboard_dankstorm(ctx):
    await ctx.send("Playing **dankstorm** sound effect from soundboard")
    print("\nPlayed dankstorm sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/dankstorm.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DEEZNUTS
@_soundboard.command(aliases = ["deez_nuts", "deeznuts", "Deez_nuts", "Deeznuts"])
async def _soundboard_deez_nuts(ctx):
    await ctx.send("Playing **deez_nuts** sound effect from soundboard")
    print("\nPlayed deez_nuts sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/deez_nuts.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DEJA VU
@_soundboard.command(aliases = ["deja_vu", "dejavu", "Deja_vu", "Dejavu"])
async def _soundboard_deja_vu(ctx):
    await ctx.send("Playing **deja_vu** sound effect from soundboard")
    print("\nPlayed deja_vu sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/deja_vu.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB LOOK AT THIS DUDE
@_soundboard.command(aliases = ["dis_dude", "this_dude", "disdude", "thisdude", "Dis_dude", "This_dude", "Disdude", "Thisdude" ])
async def _soundboard_this_dude(ctx):
    await ctx.send("Playing **dis_dude** sound effect from soundboard")
    print("\nPlayed dis_dude sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/dis_dude.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB ANOTHER FAG LEFT THE CHAT
@_soundboard.command(aliases = ["f_left", "fleft", "F_left", "Fleft"])
async def _soundboard_f_left(ctx):
    await ctx.send("Playing **f_left** sound effect from soundboard")
    print("\nPlayed f_left sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/f_left.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB FART
@_soundboard.command(aliases = ["fart", "Fart"])
async def _soundboard_fart(ctx):
    await ctx.send("Playing **fart** sound effect from soundboard")
    print("\nPlayed fart sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/fart.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB HAH GAAAYY
@_soundboard.command(aliases = ["hah_gay", "hahgay", "Hah_gay", "Hahgay"])
async def _soundboard_hah_gay(ctx):
    await ctx.send("Playing **hah_gay** sound effect from soundboard")
    print("\nPlayed hah_gay sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/hah_gay.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB IT'S CALLED HENTAI, AND IT'S ART
@_soundboard.command(aliases = ["hen_art", "henart", "Hen_art", "Henart"])
async def _soundboard_hentai_art(ctx):
    await ctx.send("Playing **henart (hentai art)** sound effect from soundboard")
    print("\nPlayed henart sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/hen_art.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB ILLUMINATI X-FILES SOUNDTRACK
@_soundboard.command(aliases = ["illuminati", "Illuminati"])
async def _soundboard_illuminati(ctx):
    await ctx.send("Playing **illuminati** sound effect from soundboard")
    print("\nPlayed illuminati sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/illuminati.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB BITCH LASAGNA
@_soundboard.command(aliases = ["lasagna", "Lasagna", "bitch_lasagna", "Bitch_lasagna"])
async def _soundboard_bitch_lasagna(ctx):
    await ctx.send("Playing **bitch_lasagna** sound effect from soundboard")
    print("\nPlayed bitch_lasagna sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/lasagna.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB LOOSER
@_soundboard.command(aliases = ["looser", "Looser", "loser", "Loser"])
async def _soundboard_loser(ctx):
    await ctx.send("Playing **loser** sound effect from soundboard")
    print("\nPlayed loser sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/loser.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB NOOB 
@_soundboard.command(aliases = ["noob", "Noob"])
async def _soundboard_noob(ctx):
    await ctx.send("Playing **noob** sound effect from soundboard")
    print("\nPlayed noob sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/noob.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB OOF SOUND
@_soundboard.command(aliases = ["oof", "Oof"])
async def _soundboard_oof(ctx):
    await ctx.send("Playing **oof** sound effect from soundboard")
    print("\nPlayed oof sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/oof.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB I'M PICKLE RICKKKK
@_soundboard.command(aliases = ["pickle_rick", "Pickle_rick", "picklerick", "Picklerick"])
async def _soundboard_pickcle_rick(ctx):
    await ctx.send("Playing **pickle_rick** sound effect from soundboard")
    print("\nPlayed pickle_rick sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/pickle_rick.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB *POP* NICE  
@_soundboard.command(aliases = ["nice", "Nice"])
async def _soundboard_nice(ctx):
    await ctx.send("Playing **nice** sound effect from soundboard")
    print("\nPlayed nice sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/nice.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB WHY DON'T WE JUST RELAX, TURN ON THE RADIO, WOULD YOU LIKE AM OR FM
@_soundboard.command(aliases = ["radio", "Radio"])
async def _soundboard_radio(ctx):
    await ctx.send("Playing **radio** sound effect from soundboard")
    print("\nPlayed radio sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/radio.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB RICKROLL
@_soundboard.command(aliases = ["rick_roll", "Rick_roll", "rickroll", "Rickroll"])
async def _soundboard_rick_roll(ctx):
    await ctx.send("Playing **rick_roll** sound effect from soundboard")
    print("\nPlayed rick_roll sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/rick_roll.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB SPARTA
@_soundboard.command(aliases = ["sparta", "Sparta"])
async def _soundboard_sparta(ctx):
    await ctx.send("Playing **sparta** sound effect from soundboard")
    print("\nPlayed sparta sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/sparta.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB TITANIC FLUTE MEME
@_soundboard.command(aliases = ["titanic", "Titanic"])
async def _soundboard_titanic(ctx):
    await ctx.send("Playing **titanic** sound effect from soundboard")
    print("\nPlayed titanic sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/titanic.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB GTAV WASTED SOUND
@_soundboard.command(aliases = ["wasted", "Wasted"])
async def _soundboard_wasted(ctx):
    await ctx.send("Playing **wasted** sound effect from soundboard")
    print("\nPlayed wasted sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/wasted.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#WIDE PUTIN SONG
@_soundboard.command(aliases = ["wideputin", "Wideputin"])
async def _soundboard_wideputin(ctx):
    await ctx.send("Playing **wideputin** sound effect from soundboard")
    print("\nPlayed wubba sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/wideputin.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB RICK & MORTY WUBBA LUBBA DUB DUB
@_soundboard.command(aliases = ["wubba", "Wubba"])
async def _soundboard_wubba(ctx):
    await ctx.send("Playing **wubba** sound effect from soundboard")
    print("\nPlayed wubba sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/wubba.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05


'''END OF VOICE CHANNEL SOUNDBOARD COMMANDS'''

'''START OF GAME RELATED COMMANDS'''


#8BALL COMMAND
@client.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, user_question):
    author_name = ctx.author.display_name
    responses = [
        "As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes – definitely.",
        "You may rely on it.",
        "No it'll never happen give up.",
        "It might happen but ehhhhhhh.",
        "stfu i aint god."]
    final_response = random.choice(responses)
    embed = discord.Embed(
        title = "8ball command",
        description = f"Question: **{user_question}**\nAnswer: **{final_response}**",
        color = bot_color
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)


#DICE COMMAND; 1-6
@client.command()
async def dice(ctx):
    dice_number = randint(1,6)
    await ctx.send(dice_number)


#GTA V ROAST MEME FRANKLIN SIDE
@client.command(aliases = ["loc", "Loc", "LOC", "crib", "Crib", "gtavroast", "GTAVroast"])
async def _locfranklin(ctx):
    await asyncio.sleep(float(1.4))
    await ctx.send("Man, fuck you.")
    await asyncio.sleep(float(0.6))
    await ctx.send("I'll see you at work.")
    await asyncio.sleep(float(6.5))
    await ctx.send("What?!?")
    await asyncio.sleep(float(0.5))
    await ctx.send("Argh, motherfucker.")


#GTA V ROAST MEME LAMAR SIDE
#blanked out since it's hosted on Neko's bot
'''
#GTA V roast meme LAMAR SIDE
@client.command(aliases = ["loc", "Loc", "LOC", "crib", "Crib", "gtavroast", "GTAVroast"])
async def _loclamar(ctx):
    await asyncio.sleep(float(0))
    await ctx.send(f"Wassup, can a loc come up in your crib?\n")
    await asyncio.sleep(float(2.5))
    await ctx.send("Ah, n-word, don't hate me 'cause I'm beautiful, n-word.")
    await asyncio.sleep(float(0.5))
    await ctx.send("Maybe if you got rid of that old yee-yee ass haircut you got")
    await asyncio.sleep(float(0.5))
    await ctx.send("you'd get some bitches on your dick.")
    await asyncio.sleep(float(0.5))
    await ctx.send("Oh, better yet,")
    await asyncio.sleep(float(0.25))
    await ctx.send("maybe Tanisha'll call your dog-ass")
    await asyncio.sleep(float(0.50))
    await ctx.send("if she ever stop fucking with that brain surgeon or lawyer she fucking with")
    await asyncio.sleep(float(0.75))
    await ctx.send("N-word")
'''


'''
@client.command(aliases = ["rps", "RPS", "Rps", "rockpaperscissors", "Rockpaperscissors", "RockPaperScissors", "rockpaperscissor", "Rockpaperscissor", "RockPaperScissor"])
@cooldown(5, 10, BucketType.default)
async def _rpsgame(ctx, user_rps_input):
    print("someone used the rps command")
    bot_rps_list = ["rock", "paper", "scissors"]
    bots_rps_choice = random.choice(bot_rps_list)
    print(f"bot chose {bots_rps_choice} in rps game")

    if user_rps_input == "rock" or "Rock" or "ROCK" or "paper" or "Paper" or "PAPER" or "scissors" or "Scissors" or "SCISSORS" or "scissor" or "Scissor" or "SCISSOR":
        if user_rps_input == bots_rps_choice:
            print("Tied")
            await ctx.send(f"Tie! Your picked {user_rps_input} and I picked {bots_rps_choice} which results in a tie")
        else:
            if user_rps_input == "rock" or "Rock" or "ROCK":
                if bots_rps_choice != "paper":
                    print("Bot lost")
                    await ctx.send(f"You win! You picked {user_rps_input} and I picked {bots_rps_choice}")
                else:
                    print("Bot won")
                    await ctx.send(f"I win! You picked {user_rps_input} and I picked {bots_rps_choice}")

            elif user_rps_input == "paper" or "Paper" or "PAPER":
                if bots_rps_choice != "scissors":
                    print("Bot lost")
                    await ctx.send(f"You win! You picked {user_rps_input} and I picked {bots_rps_choice}")
                else:
                    print("Bot won")
                    await ctx.send(f"I win! You picked {user_rps_input} and I picked {bots_rps_choice}")

            elif user_rps_input == "scissors" or "Scissors" or "SCISSORS" or "scissor" or "Scissor" or "SCISSOR":
                if bots_rps_choice != "paper":
                    print("Bot lost")
                    await ctx.send(f"You win! You picked {user_rps_input} and I picked {bots_rps_choice}")
                else:
                    print("Bot won")
                    await ctx.send(f"I win! You picked {user_rps_input} and I picked {bots_rps_choice}")
    else:
        await ctx.send("Please use a valid syntax! e.g '/rps rock'")
'''


#MEME COMMAND
@client.command(aliases = ["meme", "Meme"])
async def _sendsmeme(ctx):
    random_meme_number = randint(1,5000)
    embed = discord.Embed(
        color = bot_color
    )
    embed.set_image(url = f"https://ctk-api.herokuapp.com/meme/{random_meme_number}")
    await ctx.send(embed = embed)


'''END OF GAME RELATED COMMANDS'''

'''START OF RESPONSES OR RELATED COMMANDS'''


#WELCOME
@client.command(aliases = ["welcome", "Welcome"])
async def _welcomecommand(ctx):
    embed = discord.Embed(
        title = "Welcome!",
        description = "Welcome to CaptainVietnam6's Playground! Please read our rules and have fun!",
        color = bot_color
    )
    await ctx.send(embed = embed)


#DESCRIPTION
@client.command(aliases = ["description", "Description"])
async def _descriptioncommand(ctx):
    embed = discord.Embed(
        title = "Server description",
        description = "This server is CaptainVietnam6's private server, ping any staff members if you have questions.",
        color = bot_color
    )
    await ctx.send(embed = embed)


#BOT DESCRIPTION COMMAND 
@client.command(aliases = ["BotDesc", "botdesc", "BotDescription", "Botdescription", "botdescription"])
async def _botdescription(ctx):
    await ctx.send("Hi! I am a bot known as CV6's PlaygroundBot. I have been programmed by CaptainVietnam6 in Python, JavaScript, and DBscript. My task is to watch over the server!")


#GOOGLE COMMAND  
@client.command(aliases = ["google", "Google", "GOOGLE"])
async def _googlelinklmao(ctx):
    await ctx.send("<https://searchengineland.com/guide/how-to-use-google-to-search>")


#DADDY PINGS CAPTAIN
# <a:emoji_name:emoji_id> for animated
@client.command(aliases = ["daddy", "Daddy", "DADDY"])
async def _pingcaptdaddy(ctx):
    await ctx.send("<@467451098735837186>")


#BENICE SEND FUNNY 'BE NICE TO SERVER STAFF'
@client.command(aliases = ["benice", "Benice", "BeNice"])
async def _benicetoserverstaff(ctx):
    await ctx.send("https://media.discordapp.net/attachments/709672550707363931/721226547817873519/tenor.gif")


#REPLIES SEND THIGH PICS
@client.command(aliases = ["thighpics", "thigh_pics", "thighpic", "thigh_pic"])
async def _thighpics(ctx):
    await ctx.send("send thigh pics uwu")


#CV6's PlaygroundBot COUNTS FOR 24 HOURS
@client.command(aliases = ["count", "Count"])
@cooldown(1, 86400, BucketType.default)
async def _count(ctx):
    CV6_count = 0
    print("someone activated the count feature")
    while CV6_count != 86400:
        await asyncio.sleep(1)
        await ctx.send(CV6_count)
        CV6_count = CV6_count + 1


#ZERO TWO GIF
@client.command(aliases = ["zerotwo", "02", "ZeroTwo", "zero two", "Zero Two", "Zero two", "Zerotwo"])
async def _zerotwo(ctx):
    await ctx.send("bruh-")
    await asyncio.sleep(float(0.5))
    await ctx.send("https://tenor.com/view/darling-in-the-franxx-zero-two-dance-gif-14732606")
    print("someone's being a simp")
    await asyncio.sleep(float(1.5))
    await ctx.send("fuckin simp lmfao")


#DICTIONARY COMMAND, GIVES YOU THE DEFINITION, SYNONYM, ANTONYM, AND LINK OF THE WORD MENTIONED
@client.command(aliases = ["Dictionary", "dictionary", "Dict", "dict"])
@cooldown(3, 30, BucketType.default)
async def _dictionarycommand(ctx, user_dictionary_request):
    dictionary = PyDictionary
    print(f"Someone used the dictionary command for the word {user_dictionary_request}")

    author_name = ctx.author.display_name
    word_meaning = dictionary.meaning(user_dictionary_request)
    word_synonym = dictionary.synonym(user_dictionary_request)
    word_antonym = dictionary.antonym(user_dictionary_request)

    embed = discord.Embed(
        title = f"Dictionary definition, synonym, and antonym for the word {user_dictionary_request}",
        description = f"**Meaning:** {word_meaning}\n\n**Synonyms:** {word_synonym}\n\n**Antonyms:** {word_antonym}",
        color = bot_color
    )
    embed.set_footer(text = f"Requested by {author_name}")

    await ctx.send(f"Getting you the definition of the word **{user_dictionary_request}**")
    await asyncio.sleep(float(0.5))
    await ctx.send(embed = embed)
    await asyncio.sleep(float(0.5))
    await ctx.send(f"Here is the link:\nhttps://www.dictionary.com/browse/{user_dictionary_request}?s=t")


#SYNONYM COMMAND, GIVES YOU THE SYNONYM OF THE WORD MENTIONED
@client.command(aliases = ["synonym", "Synonym"])
@cooldown(3, 30, BucketType.default)
async def _synonymcommand(ctx, user_synonym_request):
    dictionary = PyDictionary
    print(f"Someone used the synonym command for the word {user_synonym_request}")

    author_name = ctx.author.display_name
    word_synonym = dictionary.synonym(user_synonym_request)

    embed = discord.Embed(
        title = f"Synonyms for the word **{user_synonym_request}**",
        description = f"**Synonyms:** {word_synonym}",
        color = bot_color
    )
    embed.set_footer(text = f"Requested by {author_name}")

    await ctx.send(f"Getting you the synonyms for the word {user_synonym_request}")
    await asyncio.sleep(float(0.5))
    await ctx.send(embed = embed)


#ANTONYM COMMAND, GIVES YOU THE ANTONYM OF THE WORD MENTIONED
@client.command(aliases = ["antonym", "Antonym"])
@cooldown(3, 30, BucketType.default)
async def _antonymcommand(ctx, user_antonym_request):
    dictionary = PyDictionary
    print(f"Someone used the antonym command for the word {user_antonym_request}")

    author_name = ctx.author.display_name
    word_antonym = dictionary.antonym(user_antonym_request)

    embed = discord.Embed(
        title = f"Antonyms for the word **{user_antonym_request}**",
        description = f"**Antonyms:** {word_antonym}",
        color = bot_color
    )
    embed.set_footer(text = f"Requested by {author_name}")

    await ctx.send(f"Getting you the antonyms for the word {user_antonym_request}")
    await asyncio.sleep(float(0.5))
    await ctx.send(embed = embed)


#REPEAT COMMAND; BOT REPEATS AFTER USER
@client.command(aliases = ["repeat", "Repeat", "say", "Say"])
@cooldown(5, 60, BucketType.default)
async def _repeat_after_user(ctx, *, user_repeat_input):
    await ctx.send(f"{user_repeat_input}")


#LEGEND REPLY COMMAND THINGY
@client.command(aliases = ["Legend", "legend"])
async def _legendlol(ctx):
    await ctx.send("WHAT AN ABSOLUTE LEGEND. WHAT A GOD. HOLY SHIT PRAISE THIS MAN HE'S THE GOD OF EVERYTHING HOLY SHIT WOW THAT WAS SO AMAZING EVEN I'M SHOCKED WOW. EVERYONE ON THE EARTH SHOULD PRAISE THIS MAN WOW THAT WAS DAMN GODLY\n")


#TWITCH LINK COMMAND
@client.command(aliases = ["twitch", "Twitch"])
async def _twitchlink(ctx):
    await ctx.send("https://twitch.tv/captainvietnam6")


#EW LIGHTMODE BADDDDDD
@client.command(aliases = ["lightmode", "Lightmode", "discordlightmode", "Discordlightmode"])
@cooldown(1, 5, BucketType.default)
async def _ewlightmode(ctx):
    await ctx.send("eW liGht mOdE bAd DarK MOdE GOoD")


#REPLY SPAM COMMAND
#spams what you type after "/spam" 5 times
@client.command(aliases = ["spam", "Spam"])
@cooldown(1, 60, BucketType.default)
async def _replyspam(ctx, *, user_spam_input):
    print("Someone activated the reply spam command")
    for i in range(5):
        await ctx.send(f"{user_spam_input}")
        await asyncio.sleep(float(0.1))
    await asyncio.sleep(float(0.25))
    print("Reply spam command ended")
    await ctx.send("Please wait 60 seconds to use this command again.")


#PRINT COMMAND; SENDS A FANCY EMBED IMAGE WITH AUTHOR'S MESSAGE
@client.command(aliases = ["print", "Print"])
@cooldown(1, 15, BucketType.default)
async def _printmessage(ctx, *, user_print_message):
    embed = discord.Embed(
        color = bot_color
    )
    embed.set_image(url = f"https://flamingtext.com/net-fu/proxy_form.cgi?script=crafts-logo&text={user_print_message}+&_loc=generate&imageoutput=true")
    await ctx.send(embed = embed)


#SENDS SPEEDRUN.COM PROFILE OF USER
@client.command(aliases = ["speedrun", "Speedrun"])
async def _speedrunprofile(ctx, user_speedrun_input):
    await ctx.send(f"Sending {user_speedrun_input}'s profile...")
    await asyncio.sleep(float(1.5))
    await ctx.send(f"https://speedrun.com/user/{user_speedrun_input}")


#SHUT UP COMMAND
@client.command(aliases = ["shut", "Shut"])
async def _shutupcommand(ctx):
    await ctx.send("https://tenor.com/view/meryl-streep-shut-up-yell-gif-15386483")


#DWEAM COMMAND LOL
@client.command(aliases = ["dweam", "Dweam"])
async def _dweamlolcommand(ctx):
    await ctx.send("In this video, me and my friends coded it so that we're all anime cat girls, this was INSANE! To make it harder, we decided to give ourselves nicknames, so in the video we will be calling ourselves Dweam, Gogy and Sapcat. Can we beat Minecraft? You're about to find out. Also only a small percentage of people that watch my videos are actually subscribed so if you end up liking this video consider subscribing, it's free and you can always change your mind in the future, we are getting so close to 69420 million subscribers. Enjoy the video!")


#SEND NOTHING COMMAND
@client.command(aliases = ["nothing"])
async def _sendnothinglol(ctx):
    await ctx.send("⠀⠀⠀⠀⠀")


#DISCORDMOD FUNNY
@client.command(aliases = ["discordmod", "Discordmod"])
async def _funnydiscordmod(ctx):
    await ctx.send("https://i.kym-cdn.com/entries/icons/original/000/035/767/cover4.jpg")


#CUSSWORDS FUNNY
@client.command(aliases = ["cusswords", "cussword", "Cusswords", "Cussword"])
async def _funnycusswords(ctx):
    await ctx.send("no more saying cuss words! it. is. not. good. i'm putting a video on youtube about no more saying cuss words. no more saying cuss words, guys! it's inappropriate, and violent! if you say a cuss word then you're like.... going to jail and you're.. like... when you go to jail.. if u- when you go to jail if you say.. if you say a cuss word you go to jail and when you go to jail, you said a cuss word.. then you're only gonna eat broccoli and other vegetables for your whole life. you don't wanna eat vegetables sometimes people like eating sweets but... i eat broccoli.. so, i'm okay with broccoli but i do not wanna go to jail.")


#FUNNY PINGED
@client.command(aliases = ["pinged", "Pinged"])
async def _funnygotpinged(ctx):
    await ctx.send("I GOT PINGED FUCK SHIT SHIT SHIT MY PC IS GONNA EXPLODE IM GONNA DIE IM GONNA BE HOMLESS NOW WHY DID YOU DO THIS TO ME MY PC MADE A SMALL DING NOISE AHHHHHHHHHHHHHHHHHHHHHHHHHH WHY WHY WHY WHY IM SO SAD YOU BESTOWED THIS ANCIENT FORM OF TORTURE UPON ME YOU SHOULD BE UNMODDED AND BANNED IMMDIATELY WHYYYYYYYYYYYYYYYY")


#/REEE COMMAND; FUNNY THING BY BLUEISH
@client.command(aliases = ["reee", "REEE"])
async def _reeefunnyblueish(ctx):
    await ctx.send("Hey guys if your enjoying this video then SMASH THAT LIKE BUTTON AND DONT FORGET TO SUBSCRIBE BECAUSE ACCORDING TO UTUBES STATISTICS ONLY FUCKING 2.6796291 OF MY VIEWERS ARE SUBSCRIBED AND WITH FURTHER A DO LETS GET RIGHT INTO THE VIDEOOOOOOOOO")


#SPONSOR ME COMMAND
@client.command(aliases = ["sponsorme", "sponserme"])
async def _sponsormefunnaeblueish(ctx):
    await ctx.send("Oh and also HAVE U HEARD ABOUT RAYCON EARBUDS???? THEYRE JUST SAMSUNG GALAXY EARBUDS BUT FATTER AND LESS EXPENSIVE GO BUY THEM WITH MY DISCOUNT CODE AT RAYCON.COM/IFUCKEDURMOM I REPEAT RAYCON.COM/IFUCKEDURMOM GO BUY THEM RIGHT NOW")


#PI CALCULATE COMMAND TO REQUESTED DIGITS
@client.command(aliases = ["pi", "Pi", "PI", "π"])
async def _pi_digits_calc(ctx, pi_digits):
    DIGITS = int(pi_digits)
    decimal_places = DIGITS - 1
    author_name = ctx.author.display_name

    if DIGITS > 0 and DIGITS <= 2000:
        def pi_digits(x):
            #Generate x digits of Pi
            k,a,b,a1,b1 = 2,4,1,12,4
            while x > 0:
                p,q,k = k * k, 2 * k + 1, k + 1
                a,b,a1,b1 = a1, b1, p*a + q*a1, p*b + q*b1
                d,d1 = a/b, a1/b1

                while d == d1 and x > 0:
                    yield int(d)
                    x -= 1
                    a,a1 = 10*(a % b), 10*(a1 % b1)
                    d,d1 = a/b, a1/b1

        digits = [str(n) for n in list(pi_digits(DIGITS))]
        pi_output = "%s.%s\n" % (digits.pop(0), "".join(digits))

        embed = discord.Embed(
            title = f"Pi to the {decimal_places}th decimal place (or {DIGITS} digits)",
            description = f"{pi_output}",
            color = bot_color
        )
        embed.set_footer(text = f"Requested by {author_name}")
        
        print(f"Someone used the Pi calculator command to {DIGITS} digits")
        await ctx.send(f"Calculating Pi to {DIGITS} digits...")
        await asyncio.sleep(float(0.5))
        await ctx.send(embed = embed)
    
    elif DIGITS < 0:
        print("Pi calculator error: requested digits under 0")
        await ctx.send("Error: requested digits cannot be under 0 or be negative")
    
    elif DIGITS > 2000:
        print("Pi calculator error: requested digits over 2000")
        await ctx.send("Error: requested digits cannot be over 2000 (this is to reduce calculation times and load on server)")


#BELOW HERE IS THE ALWAYS ACTIVE CLIENT.LISTEN AND ON_MESSAGE COMMANDS


#FAIR
@client.listen("on_message")
async def replyping(message):
    if message.author.bot:   #ends command if "fair" is detected from a bot, this stops spam loops
        return
    if "fair" in message.content:   #if "fair" is in a message the member sends, it replies with "fair"
        await message.channel.send("fair")


#POG REPLY
@client.listen("on_message")
async def replypog(message):
    pog_responses = ["pog", "poggers", "pogsss", "pogs", "pogs?"]

    if message.author.bot:
        return
    if "pog" in message.content:
        await message.channel.send(random.choice(pog_responses))
    if "POG" in message.content:
        await message.channel.send(random.choice(pog_responses))
    if "Pog" in message.content:
        await message.channel.send(random.choice(pog_responses))


#CAPT GET PINGED ANGR
@client.listen("on_message")
async def captgetpinged(message):
    pinged_reply_messages = ["uh oh capt got pingo", "dingus why would you ping the server owner", "capt got pinged lmao"]
    capt_got_pinged_message = random.choice(pinged_reply_messages)
    if message.author.bot:
        return
    #mobile varient
    if "<@467451098735837186>" in message.content:
        await message.channel.send(f"{capt_got_pinged_message}")
    #PC varient
    if "<@!467451098735837186>" in message.content:
        await message.channel.send(f"{capt_got_pinged_message}")


#CV6 PlaygroundBot GETS PINGED ANGR
@client.listen("on_message")
async def cv6getpiged(message):
    if message.author.bot:
        return
    #mobile varient
    if "<@816184765065199667>" in message.content:
        await message.channel.send("fuck off why ping")
    #PC varient
    if "<@!816184765065199667>" in message.content:
        await message.channel.send("fuck off why ping")


#REPLY GOODNIGHT IF SOMEONE SAYS GOODNIGHT OR SIMILAR
@client.listen("on_message")
async def _replygoodnight(message):
    if message.author.bot:
        return
    if "goodnight" in message.content:
        await message.channel.send("goodnight!")
    if "Goodnight" in message.content:
        await message.channel.send("goodnight!")
    if "gn " in message.content:
        await message.channel.send("goodnight!")
    if "Gn" in message.content:
        await message.channel.send("goodnight!")
    if "GN" in message.content:
        await message.channel.send("goodnight!")


#DETECTS CODE
@client.listen("on_message")
async def _detects_code(message):
    if message.author.bot:
        return
    if "```py" in message.content:
        await message.channel.send("woah python code")
    if "```java" in message.content:
        await message.channel.send("woah java code")
    if "```js" in message.content:
        await message.channel.send("woah JavaScript code")
    if "```javascript" in message.content:
        await message.channel.send("woah JavaScript code")
    if "```ruby" in message.content:
        await message.channel.send("woah ruby code")
    if "```cpp" in message.content:
        await message.channel.send("woah C++ code")
    if "```c++" in message.content:
        await message.channel.send("woah C++ code")
    if "```c" in message.content:
        await message.channel.send("woah C code")
    if "```kotlin" in message.content:
        await message.channel.send("woah kotlin code")
    if "```go" in message.content:
        await message.channel.send("woah go code")
    if "```swift" in message.content:
        await message.channel.send("woah swift code")
    if "```rust" in message.content:
        await message.channel.send("woah rust code")
@client.listen("on_message")
async def _detects_code2(message):
    if message.author.bot:
        return
    if "```html" in message.content:
        await message.channel.send("wow HTML code")
    if "```css" in message.content:
        await message.channel.send("wow CSS code")



#RANDOM CHANCE ANNOYED RESPONSE THING
#whenever the bot detects a message by a person there is a 2% chance it replies
@client.listen("on_message")
async def _random_annoyed(message):
    mention = message.author.id
    annoyed_responses_list = [
        "you should talk less",
        "you talk too much",
        "ugh, stop talking already",
        "you're so annoying tbh",
        "shut up already",
        "goddamn you're annoying",
        "you done talking?"
    ]
    annoyed_responses = random.choice(annoyed_responses_list)

    if message.author.bot:
        return
    else:
        if random.randint(0, 100) < 2:
            await message.channel.send(f"<@{mention}> {annoyed_responses}")


#REPLIES STFU COMMAND
@client.listen("on_message")
async def _ramdon_stfu_detect(message):
    mention = message.author.id
    stfu_reponses_list = [
        "you stfu",
        "bruh who you telling to stfu",
        "YOU stfu",
        "i think it's you who needs to shut up",
        "maybe you should shut up instead",
        "idot you stfu"
    ]

    stfu_responses = random.choice(stfu_reponses_list)

    if message.author.bot:
        return
    else:
        if "stfu" in message.content:
            await message.channel.send(f"<@{mention}> {stfu_responses}")
        if "STFU" in message.content:
            await message.channel.send(f"<@{mention}> {stfu_responses}")
        if "Stfu" in message.content:
            await message.channel.send(f"<@{mention}> {stfu_responses}")
        if "shut up" in message.content:
            await message.channel.send(f"<@{mention}> {stfu_responses}")
        if "Shut up" in message.content:
            await message.channel.send(f"<@{mention}> {stfu_responses}")
        if "SHUT UP" in message.content:
            await message.channel.send(f"<@{mention}> {stfu_responses}")


'''END OF RESPONSES OR RELATED COMMANDS'''

'''START OF NSFW COMMANDS'''


#HENTAI COMMAND
@client.command(aliases = ["hentai", "Hentai"])
async def _hentai_nsfw_command(ctx):
    website_num = random.randint(1, 5)

    if website_num == 1:
        post_num = random.randint(1000000, 3000000)
        embed = discord.Embed(
            title = f"Hentai post #{post_num} from danbooru.me",
            color = bot_color
        )
        embed.set_image(url = f"http://danbooru.me/posts/{post_num}")

    elif website_num == 2:
        post_num = random.randint(50, 755000)
        embed = discord.Embed(
                title = f"Hentai post #{post_num} from yande.re",
                color = bot_color
            )
        embed.set_image(url = f"https://yande.re/post/show/{post_num}")

    elif website_num == 3:
        post_num = random.randint(1000000, 5000000)
        embed = discord.Embed(
                title = f"Hentai post #{post_num} from gelbooru.com",
                color = bot_color
            )
        embed.set_image(url = f"https://gelbooru.com/index.php?page=post&s=view&id={post_num}")
    
    elif website_num == 4:
        post_num = random.randint(1, 500000)
        embed = discord.Embed(
                title = f"Hentai post #{post_num} from nhentai.net",
                color = bot_color
            )
        embed.set_image(url = f"https://nhentai.net/g/{post_num}/1/")
    
    elif website_num == 5:
        post_num = random.randint(1, 40)
        embed = discord.Embed(
                title = f"Hentai post #{post_num} from commentseduire.net",
                color = bot_color
            )
        embed.set_image(url = f"http://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-{post_num}.gif")

    if ctx.channel.is_nsfw():
        await ctx.send(embed = embed)
    else:
        await ctx.send("This command can only be used in a NSFW channel")


'''END OF NSFW COMMANDS'''


'''START OF EMOJI RESPONSES COMMANDS'''

#SAMPLE ON MESSAGE CODE
'''
@client.listen("on_message")
async def _(message):
    if message.author.bot:
        return
    if "" in message.content:
        await message.channel.send("")
    if "" in message.content:
        await message.channel.send("")
'''

#SAMPLE RESPONSE COMMAND CODE
'''
@client.command(aliases = ["", ""])
async def _(ctx):
    await ctx.send("")
'''

#FULL SET
'''
@client.listen("on_message")
async def _(message):
    if message.author.bot:
        return
    if "" in message.content:
        await message.channel.send("")
    if "" in message.content:
        await message.channel.send("")

@client.command(aliases = ["", ""])
async def _(ctx):
    await ctx.send("")
'''


#SO FAKE EMOJI
@client.listen("on_message")
async def _sofakeemoji(message):
    if message.author.bot:
        return
    if "fake" in message.content:
        await message.channel.send("<:cv6_so_fake:812995927605903400>")
    if "Fake" in message.content:
        await message.channel.send("<:cv6_so_fake:812995927605903400>")

@client.command(aliases = ["fake", "Fake"])
async def _sofakeemojisend(ctx):
    await ctx.send("<:cv6_so_fake:812995927605903400>")


#DOUBT EMOJI
@client.listen("on_message")
async def _doubtemoji(message):
    if message.author.bot:
        return
    if "Doubt" in message.content:
        await message.channel.send("<:cv6_X_doubt:812995858781438022>")
    if "doubt" in message.content:
        await message.channel.send("<:cv6_X_doubt:812995858781438022>")

@client.command(aliases = ["doubt", "Doubt"])
async def _doubtemojisend(ctx):
    await ctx.send("<:cv6_X_doubt:812995858781438022>")


#STONKS EMOJI
@client.listen("on_message")
async def _stonksemoji(message):
    if message.author.bot:
        return
    if "stonk" in message.content:
        await message.channel.send("<:cv6_stonks:812995837613309992>")
    if "Stonk" in message.content:
        await message.channel.send("<:cv6_stonks:812995837613309992>")

@client.command(aliases = ["stonks", "stonk", "Stonks", "Stonk"])
async def _stonksemojisend(ctx):
    await ctx.send("<:cv6_stonks:812995837613309992>")


#SIMP PILLS EMOJI
@client.listen("on_message")
async def _simppills(message):
    if message.author.bot:
        return
    if "simp" in message.content:
        await message.channel.send("<:cv6_simp_pills:812995814904561695>")
    if "Simp" in message.content:
        await message.channel.send("<:cv6_simp_pills:812995814904561695>")

@client.command(aliases = ["simp", "Simp"])
async def _simppillsemojisend(ctx):
    await ctx.send("<:cv6_simp_pills:812995814904561695>")


#UWU EMOJI
@client.listen("on_message")
async def _uwuemoji(message):
    if message.author.bot:
        return
    if "uwu" in message.content:
        await message.channel.send("uwu daddy smack me harder <:cv6_uwu:812995744247447563>")
    if "UwU" in message.content:
        await message.channel.send("uwu daddy smack me harder <:cv6_uwu:812995744247447563>")

@client.command(aliases = ["uwu", "UwU"])
async def _uwuemojisend(ctx):
    await ctx.send("uwu daddy smack me harder <:cv6_uwu:812995744247447563>")


#WAT EMOJI
@client.command(aliases = ["what", "What", "wat", "Wat"])
async def _watemojisend(ctx):
    await ctx.send("<:cv6_wat:812995793278468117>")


#ADMIN ABOOZ EMOJI
@client.command(aliases = ["abooz", "Abooz"])
async def _adminaboozemojisend(ctx):
    await ctx.send("<:cv6_abooz:812995683740418068>")


#60S TIMER EMOJI
@client.listen("on_message")
async def _timeremoji(message):
    if message.author.bot:
        return
    if "timer" in message.content:
        await message.channel.send("<a:cv6_60s_timer:812995903421022221>")
    if "Timer" in message.content:
        await message.channel.send("<a:cv6_60s_timer:812995903421022221>")

@client.command(aliases = ["timer", "Timer"])
async def _timeremojisend(ctx):
    await ctx.send("<a:cv6_60s_timer:812995903421022221>")


#RACIST EMOJI
@client.listen("on_message")
async def _racistemoji(message):
    if message.author.bot:
        return
    if "racist" in message.content:
        await message.channel.send("<:cv6_rascist:812995663817342986>")
    if "Racist" in message.content:
        await message.channel.send("<:cv6_rascist:812995663817342986>")

@client.command(aliases = ["racist", "Racist"])
async def _racistemojisend(ctx):
    await ctx.send("<:cv6_rascist:812995663817342986>")


#GAY EMOJI
@client.listen("on_message")
async def _gayemoji(message):
    if message.author.bot:
        return
    if "gay" in message.content:
        await message.channel.send("<:cv6_gay:812995646919147550>")
    if "Gay" in message.content:
        await message.channel.send("<:cv6_gay:812995646919147550>")

@client.command(aliases = ["gay", "Gay"])
async def _gayemojisend(ctx):
    await ctx.send("<:cv6_gay:812995646919147550>")


#BISEXUAL EMOJI
@client.listen("on_message")
async def _bisexualemoji(message):
    if message.author.bot:
        return
    if "bisexual" in message.content:
        await message.channel.send("<:cv6_bisexual:812995628950618112>")
    if "Bisexual" in message.content:
        await message.channel.send("<:cv6_bisexual:812995628950618112>")

@client.command(aliases = ["Bisexual", "bisexual", "bi", "Bi"])
async def _bisexualemojisend(ctx):
    await ctx.send("<:cv6_bisexual:812995628950618112>")


#TRANS EMOJI
@client.listen("on_message")
async def _transemoji(message):
    if message.author.bot:
        return
    if "transgender" in message.content:
        await message.channel.send("<:cv6_trans:812995611270840371>")
    if "Transgender" in message.content:
        await message.channel.send("<:cv6_trans:812995611270840371>")
    if "trans" in message.content:
        await message.channel.send("<:cv6_trans:812995611270840371>")
    if "Trans" in message.content:
        await message.channel.send("<:cv6_trans:812995611270840371>")

@client.command(aliases = ["transgender", "Transgender", "Trans", "trans"])
async def _transemojisend(ctx):
    await ctx.send("<:cv6_trans:812995611270840371>")


#POLICE EMOJI
@client.listen("on_message")
async def _policeemoji(message):
    if message.author.bot:
        return
    if "police" in message.content:
        await message.channel.send("<a:cv6_police:812995767639212032>")
    if "Police" in message.content:
        await message.channel.send("<a:cv6_police:812995767639212032>")

@client.command(aliases = ["police", "Police"])
async def _policeemojisend(ctx):
    await ctx.send("<a:cv6_police:812995767639212032>")


#Fspam EMOJI
@client.command(aliases = ["fspam", "Fspam"])
async def _fspamemojisend(ctx):
    await ctx.send("<a:cv6_Fspam:812995726710669342>")


#CLAP EMOJI
@client.command(aliases = ["clap", "Clap"])
async def _clapemojisend(ctx):
    await ctx.send("<a:cv6_clap:812995595613896714>")


#YOU TRIED EMOJI
@client.command(aliases = ["youtried", "Youtried"])
async def _uoutriedemojisend(ctx):
    await ctx.send("<a:cv6_youtried:812995570906038292>")


#PYTHON EMOJI SEND
@client.listen("on_message")
async def _pythonemoji(message):
    if message.author.bot:
        return
    if "python" in message.content:
        await message.channel.send("<a:cv6_python:812995549414162474>")
    if "Python" in message.content:
        await message.channel.send("<a:cv6_python:812995549414162474>")

@client.command(aliases = ["python", "Python"])
async def _pythonemojisend(ctx):
    await ctx.send("<a:cv6_python:812995549414162474>")


#PEPEfog emoji
@client.command(aliases = ["pepepog", "Pepepog"])
async def _pepefogemojisend(ctx):
    await ctx.send("<a:cv6_pepepog:812995528081276958>")


'''END OF EMOJI RESPONSE COMMANDS'''

'''FINAL IMPORTANT FUNCTIONS AND IMPORTANT STUFF'''
#KEEP ALIVE COMMAND FOR WEBSERVER
keep_alive()

#BOT TOKEN TO CONNECT TO DISCORD'S API
client.run(BOT_TOKEN) #token can be found in 'BOT_TOKEN.py'
