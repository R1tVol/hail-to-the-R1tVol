import discord
from discord.ext import commands
import subprocess

# Botunuzun token'ı
TOKEN = 'MTI3MDAxMDQ1MjIzOTMyMzIyOQ.GA7SH3.VC8sKjK_OqYpCc5Iu0XcHWVbzaw--Gyno9j3pI'  

# Botunuzu tanımlayın
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Sorular ve cevaplar
questions = [
    {"question": "Which year did R1tVol born?", "answer": "2008"},
    {"question": "Which hospital did R1tVol born?", "answer": "Samatya"},
    {"question": "How old is R1tVol now?", "answer": "16"},
    {"question": "Which country is R1tVol currently living in?", "answer": "Turkey"},
    {"question": "Is R1tVol awesome? (y/n)", "answer": "yes"},
    {"question": "How old was R1tVol when we wrote his first virus?", "answer": "10"},
    {"question": "R1tVol was chosen as the youngest ... member. Fill in the blank.", "answer": "AFAD"},
    {"question": "What's the name of R1tVol's first virus?", "answer": "The Omphena"},
    {"question": "Did he create a bot also named The Omphena? (y/n)", "answer": "yes"},
    {"question": "What's the name of the dog toy that R1tVol envied?", "answer": "Benekli"}
]


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command(name='startquiz')
async def start_quiz(ctx):
    print("Exam is about to start")
    score = 0
    for q in questions:
        await ctx.send(q['question'])
        
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        try:
            msg = await bot.wait_for('message', timeout=30.0, check=check)
            if msg.content.strip().lower() == q['answer'].lower():
                score += 1
        except discord.TimeoutError:
            await ctx.send("You cannot answer the quesiton when time's out..")

    if score >= 5:
        await ctx.send(f"True answers: {score}. `game.bat` is activated.")
        subprocess.run(['game.bat'], shell=True)
    else:
        await ctx.send(f"True answers: {score}. `game.bat` is not activated.")

# Botu çalıştır
bot.run(TOKEN)
