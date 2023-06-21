import discord
import schedule
import asyncio
import random
from discord.ext import commands

TOKEN = 'TOKEN DO BOT'
CHANNEL_ID = ID DO CANAL DO DISCORD  # ID do canal onde as mensagens serão enviadas

daily_messages = [
   "<@318561613403783178> Olá Raphael Anazario Rodrigues, vou esfaquear você :) :smiling_imp: ",
    "<@318561613403783178> Vamos todos esfaquear o Raphael!!! ",
    "<@318561613403783178> O Rato Morreeeeeeeeeeeeeeeeeu !!!!!!!!!!!!!!!!!!! ",
    "<@318561613403783178> Bom dia a todos, e vamos nos lembrar de que todo dia é dia de matar o raphael !!",
    "<@318561613403783178> Bom dia a todos, e vamos lembrar de mandar o rato ir tomar no cu !",
    "<@318561613403783178> Raphel anazario hoje é o dia de sua morte",
    "<@318561613403783178> Bom dia meu pratinha preferido",
    "<@318561613403783178> Que um missil caia na casa de raphael anazario :pray: :heart_eyes:",
]

rato_messages = [
    "<@318561613403783178> Oi Raphael",
    "<@318561613403783178> Morra R4to Johnsons MORRAAAAAAAAAAAAAAAAAAAAAAAA",
    "<@318561613403783178> VA PARA O INFERNO RAPHAELLLLLLL!",
    "<@318561613403783178> Querido deus boa noite, queria que o Rato fosse morto com 26 tiros de glock no peito e morresse e que ele ficasse ensanguentado no chão enquanto alguem filmasse, muito obrigado amem! :pray:",
    "<@318561613403783178> Acordei no dia de hoje com um sentimento de satisfaçao imenso deus, sim o senhor me deu o prazer de ter um sonho no qual o sr raphael anazario estava em uma prisao com 4 condenados a prisao perpetua escondendpo 25 celulares no orificio anal dele e chamando ele de meu amor",
    "<@318561613403783178> Eu tenho mais que certeza que no dia que o R4to johnson tiver um carro só dele, ele vai comer travesti",
    "<@318561613403783178> Rato? a pior samira? kkkkkk :clown:",
    "<@318561613403783178> ESPERO QUE ALGUEM VEJA O R4TO JOHNSON NA RUA E JOGUE UM PARALELEPIPEDO NA CABEÇA DE CAIXA D'ÁGUA DELE, E VEJA ELE SANGRAR",
    "<@318561613403783178> Raphael? aquele lá que tem a pior samira conhecida de são paulo??? kkkkkkkkkkkkkkkkkkkk",
    "<@318561613403783178> Ouvi dizer que o raphael finalmente tirou a armadura prateada, ta otimo hein hahahaha",
    "<@318561613403783178> Alguem viu o Shawn Mendes Anazario? KKKKkk",
 ]

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True  # Habilita a leitura de mensagens
intents.guilds = True  # Habilita o acesso a informações dos servidores
intents.message_content = True  # Habilita a leitura do conteúdo das mensagens

bot = commands.Bot(command_prefix='!', intents=intents)


async def send_daily_message():
    try:
        channel = bot.get_channel(CHANNEL_ID)
        message = random.choice(daily_messages)
        await channel.send(message)
    except discord.HTTPException:
        print('Erro ao enviar mensagem diária')


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    schedule_daily_messages()


def schedule_daily_messages():
    loop = asyncio.get_running_loop()
    loop.create_task(run_schedule())


async def run_schedule():
    while True:
        await asyncio.sleep(1)
        schedule.run_pending()


@bot.command(name='rato')
async def rato_command(ctx):
    try:
        channel = bot.get_channel(CHANNEL_ID)
        message = random.choice(rato_messages)
        await channel.send(message)
    except discord.HTTPException:
        print('Erro ao enviar mensagem do comando !rato')


schedule.every().day.at("01:33").do(asyncio.create_task, send_daily_message())  # Agendamento diário para as 08:00
schedule.every().day.at("04:00").do(asyncio.create_task, send_daily_message())  
schedule.every().day.at("08:00").do(asyncio.create_task, send_daily_message())
schedule.every().day.at("12:00").do(asyncio.create_task, send_daily_message())
schedule.every().day.at("14:30").do(asyncio.create_task, send_daily_message())
schedule.every().day.at("16:00").do(asyncio.create_task, send_daily_message())
schedule.every().day.at("18:30").do(asyncio.create_task, send_daily_message())
schedule.every().day.at("19:40").do(asyncio.create_task, send_daily_message())
schedule.every().day.at("21:00").do(asyncio.create_task, send_daily_message())
schedule.every().day.at("00:00").do(asyncio.create_task, send_daily_message())


bot.run(TOKEN)
