from rich.console import Console
from random import choice
from time import sleep
console = Console()
userscore = 0 
compScore = 0
console.print("[green]Are You ready for a match?[green] ")
console.print('''How to play?
    --> For Scissor, Enter [bold red]S[/bold red]
    --> For paper, Enter [bold blue]P[/bold blue]
    --> For rock, Enter [bold green]R[/bold green] \n''')

def choose():
    pick = input("Enter your choice: ").upper()
    print()
    if pick not in ['S','P','R']:
        console.print (f"[bold red]'{pick}' IS INVALID [bold red]" )
        console.print('''How to play?
    --> For Scissor, Enter [bold red]S[/bold red]
    --> For paper, Enter [bold blue]P[/bold blue]
    --> For rock, Enter [bold green]R[/bold green] \n''')
        return choose()
    else:
        return pick
    
def naming(received):
    if received == 'R':
        return 'ROCK 🪨'
    elif received == 'S':
        return 'SCISSORS ✂️'
    else:
        return 'PAPER 📄'
    
rounds = int(input("How Many Rounds Would You Like: "))
print()

count = 1
while count<=rounds:
    sleep(0.5)
    console.print(f"[bold]ROUND {count}[bold]")
    count = count + 1
    pick = choose()
    x = choice(['S','P','R'])
    if pick == x:
        x = naming(x)
        console.print (f"[bold yellow]DRAW YOU AND COMPUTER BOTH CHOSE[/bold yellow] {x}")
        compScore +=1
        userscore +=1

    elif x == 'S' and pick =="R" or x == 'P' and pick == 'S' or x == 'R' and pick =='P':
        x = naming(x)
        pick = naming(pick)
        console.print(f'''[bold green]YOU WON [/bold green]
            COMPUTER --> {x}
            YOU --> {pick}''')
        userscore +=1

    else:
        x = naming(x)
        pick = naming(pick)
        console.print(f'''[bold red]YOU LOST [/bold red]
            COMPUTER --> {x}
            YOU --> {pick}''')
        compScore +=1
    print()
    print (f"""SCORE
COMPUTER --> {compScore}
USER ------> {userscore} \n""")
    
if compScore == userscore:
    console.print("[bold yellow]THE GAME WAS A DRAW [/bold yellow]")
elif compScore> userscore:
    console.print("[bold RED]YOU LOST[/bold RED]")
else:
    console.print("[bold GREEN]You Won[/bold GREEN]")

