import rich.color
import rich.style
import rich.themes
from __init__ import *
import threading

console = Console()

DELAY = 2 # seconds

def try_to_int(x):
    try:
        return int(x)
    except:
        return False
    
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
        
def delay(seconds):
    time.sleep(seconds)

def ask(question, choices=None, style="bold blue", type=str, range=None):
            
    if range != None:
        answer = Prompt.ask(f"{question} [bright_magenta][{range[0]}-{range[1]}][/]", choices=choices)
    else:
        answer = Prompt.ask(question, choices=choices)
        
    if try_to_int(answer):
        if range != None:
            if range:
                if range[0] <= int(answer) <= range[1]:
                    return answer
                else:
                    console.print(Align.center(Panel("Invalid choice! Please try again.", style="bold red", expand=False)))
                    return ask(question, choices, style, type, range)
            else:
                return answer
        return answer
    elif type == str:
        return answer
    else:
        return ask(question, choices, style, type, range)
                
            
        

class User:
    def __init__(self, username, ip, port):
        self.username = username
        self.ip = ip
        self.port = port
        
class Settings:
    def __init__(self, text_color, text_background_color):
        self.text_color = text_color
        self.text_background_color = text_background_color
    
    def __call__(self, console):
        console.style = f"{self.text_color} on {self.text_background_color}"
        
class Message:
    def __init__(self, user, message):
        self.user = user
        self.message = message
        
    def __call__(self):
        return f"[{self.user.username}]{self.user.username}[/]: {self.message}"

class ColorTable:
    def __init__(self, title="Available Colors"):
        self.table = Table(title=title)
            
        for i in range(0,7):
            self.table.add_column("Color")
            self.table.add_column("Color Code")
        

        
        row1, row2, row3, row4, row5, row6, row7 = (([]) for i in range(7))
        
        for color in list(rich.color.ANSI_COLOR_NAMES)[:38]:
            row1.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))
        for color in list(rich.color.ANSI_COLOR_NAMES)[38:77]:
            row2.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))
        for color in list(rich.color.ANSI_COLOR_NAMES)[77:115]:
            row3.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))
        for color in list(rich.color.ANSI_COLOR_NAMES)[115:154]:
            row4.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))
        for color in list(rich.color.ANSI_COLOR_NAMES)[154:193]:
            row5.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))
        for color in list(rich.color.ANSI_COLOR_NAMES)[193:232]:
            row6.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))
        for color in list(rich.color.ANSI_COLOR_NAMES)[232:]:
            row7.append((f"[{color}]{color}[/]", str(rich.color.ANSI_COLOR_NAMES[color])))
        
        row7.append("")
        
        for i in range(0,38):
            self.table.add_row(*row1[i], *row2[i], *row3[i], *row4[i], *row5[i], *row6[i], *row7[i if i < 3 else 3])
            
    def __call__(self):
        return self.table
        
        
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
    
user_settings = Settings("white", "black")
    
def welcome():
    cls()
    console.print(Align.center(Panel(text2art("Console Chat 2.0!"), title="Welcome to", style="bold yellow", expand=False, border_style="red")))
    console.print(Align.center(Panel("              A simple chat application using Python and Socket Programming               ", title="Description", style="bold green", expand=False)))
    console.print(Align.center(Panel("Developed by: HellSAS", title="Developer", style="bold blue", expand=False, border_style="blue")))
    
    console.print(Align.center("1. Start Server"))
    console.print(Align.center("2. Join Server"))
    console.print(Align.center("3. Settings"))
    console.print(Align.center("4. Exit"))
    match ask("Enter your choice", ["1", "2", "3", "4"]):
        case "1":
            start_server()
        case "2":
            join_server()
        case "3":
            settings()
        case "4":
            exit()
        case _:
            console.print(Align.center(Panel("Invalid choice! Please try again.", style="bold red", expand=False)))
            welcome()
    
def settings():
    def change_username():
        cls()
        console.print(Align.center(Panel("Change Username", style="bold green", expand=False)))
        User.name = Prompt.ask("Enter new username", default="User")
        console.print(Align.center(Panel("Username changed successfully!", style="bold green", expand=False)))
        settings()
        
    def change_theme():
        cls()
        console.print(Align.center(Panel("Settings", style="bold green", expand=False)))
        console.print(Align.center("1. Change text color"))
        console.print(Align.center("2. Change text background color"))
        console.print(Align.center("3. Back"))
        
        table = ColorTable()
        
        def change_color():
            console.print(table())
            answer = ask("Enter the color code of the text you want to set", type=int, range=[0, 255])
            if int(answer) in rich.color.ANSI_COLOR_NAMES.values():
                    color_name = list(rich.color.ANSI_COLOR_NAMES.keys())[list(rich.color.ANSI_COLOR_NAMES.values()).index(int(answer))]
                    console.print(f"The color code [white]{answer}[/] corresponds to the color [{color_name}]{color_name}[/{color_name}].")
                    console.print(Align.center(Panel("Color changed successfully!", style="bold green", expand=False)))
                    return color_name
            else:
                console.print(Align.center(Panel("Invalid color code! Please try again.", style="bold red", expand=False)))
                delay(DELAY)
                change_theme()
        
        match ask("Enter your choice", ["1", "2", "3"]):
            case "1":
                answer = change_color()
                user_settings.text_color = answer
                user_settings(console)
                delay(DELAY)
                settings()
            case "2":
                answer = change_color()
                user_settings.text_background_color = answer
                user_settings(console)
                delay(DELAY)
                settings()
            case "3":
                settings()
                    
        
    cls()
    console.print(Align.center(Panel("Settings", style="bold green", expand=False)))
    console.print(Align.center("1. Change Username"))
    console.print(Align.center("2. Change Theme"))
    console.print(Align.center("3. Back"))
    
    match ask("Enter your choice", ["1", "2", "3"]):
        case "1":
            change_username()
        case "2":
            change_theme()
        case "3":
            welcome()
        case _:
            console.print(Align.center(Panel("Invalid choice! Please try again.", style="bold red", expand=False)))
            settings()
            
    
def receive_messages(client, address):
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                console.print(f"Message from {address}: {message}")
        except Exception as e:
            print(f"Error receiving message from {address}: {e}")
            break

def start_server():
    cls()
    console.print(Align.center(Panel("Start Server", style="bold green", expand=False)))
    server_ip = Prompt.ask("Enter the IP address of the server", default="localhost")
    server_port = Prompt.ask("Enter the port number of the server", default="12345")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((server_ip, int(server_port)))
    except Exception as e:
        print(f"Error binding server: {e}")
        return

    cls()
    server_clients = []
    while True:
        server.listen()
        client, address = server.accept()
        server_clients.append(client)
        print(f"Connection from {address} has been established!")
        
        client.send("Welcome to the server!".encode())

        threading.Thread(target=receive_messages, args=(client, address), daemon=True).start()

        # Внутри цикла сервера добавляем возможность отправки сообщений
        while True:
            message = input("Enter your message (type 'exit' to stop): ")
            if message.lower() == "exit":
                break
            for c in server_clients:
                c.send(message.encode())

def join_server():
    cls()
    console.print(Align.center(Panel("Join Server", style="bold green", expand=False)))
    server_ip = Prompt.ask("Enter the IP address of the server", default="localhost")
    server_port = Prompt.ask("Enter the port number of the server", default="12345")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((server_ip, int(server_port)))
        threading.Thread(target=receive_messages, args=(client, (server_ip, server_port)), daemon=True).start()
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return
    
    cls()
    while True:
        message = input("Enter your message: ")
        client.send(message.encode())
    

welcome()