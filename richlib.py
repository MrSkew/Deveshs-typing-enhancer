from random import randint
import time
from time import sleep
from rich.console import Console
from rich.progress import track
lap = 0
from rich import print as rprint
names=["Jack","Jim","John","Devesh","Karthik","Rushikesh","Sumita","Rita","Bhavesh","Rishabh","Sudhanshu","Austin"]
verbs=["was", "is","might be","should be"]
nouns=["talking", "dancing", "speaking","programming","singing","cooking","studying","thinking","dreaming","sleeping","playing call of duty","playing CS:GO"]
console = Console()

console.print("Welcome! ", style="blue" ,end="")
time.sleep(1.6)
console.print("This is Devesh's typing enhancer! (beta)",style="blue")
time.sleep(2)
console.print("Initialising...",style="blue")
time.sleep(1.5)
console.print("Handy Tip: type \"help\" as a response for quick docs",style="green")
time.sleep(3.5)
def process_data():
    sleep(0.002)
for _ in track(range(100), description='[yellow]Processing data'):
    process_data()
response = input("Would you like to start typing now? y/n ")
if response == "y":
    console.print("Press enter after typing each sentence. There will be 5 laps. START!", style="purple")
    while lap != 5:
        print(names[randint(0, len(names) - 1)] + " " + verbs[randint(0, len(verbs) - 1)] + " " + nouns[
            randint(0, len(nouns) - 1)])
        starttime = time.time()
        lasttime = starttime
        sent = input()
        totaltime = round((time.time() - starttime), 2)
        totaltime = str(totaltime)
        lapplusone = lap+1
        lapplusone = str(lapplusone)
        console.print("It took you "+totaltime+"s for lap" + lapplusone)
        lap+=1
        totaltime = float(totaltime)
        lapplusone = int(lapplusone)
elif response == "n":
    for lol in track(range(200), description='[yellow]Sending Crash Report'):
        process_data()
    for ulol in track(range(200), description='[red]Quitting Application'):
        process_data()
    exit()
elif response == "help":
    for help in track(range(300), description='[blue]Gathering Docs!'):
        process_data()
    console.print("No Docs Available At The Movement! Error 1D1Ot",style="red")
