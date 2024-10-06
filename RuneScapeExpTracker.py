"""
RuneScapeExpTracker.py
Shows RuneScape experience player historicals
"""

import requests
from tkinter import *


headers = {
    'From': 'email@gmail.com'
}

skills = ["Overall","Attack","Defence","Strength","Constitution","Ranged","Prayer","Magic","Cooking","Woodcutting","Fletching","Fishing","Firemaking","Crafting","Smithing","Mining","Herblore","Agility","Thieving","Slayer","Farming","Runecrafting","Hunter","Construction","Summoning","Dungeoneering","Divination","Invention","Archaeology","Necromancy"]
playerExp = {}
playerLevels = {}
playerRanks = {}

def getCurrentExp(name):
    urlString = "https://secure.runescape.com/m=hiscore/index_lite.ws?player=" + name
    response = requests.get(urlString, headers=headers)
    n = 0
    splitResponse = response.text.split("\n")
    for i in skills:
        current = splitResponse[n].split(",")
        playerRanks[i] = current[0]
        playerLevels[i] = current[1]
        playerExp[i] = current[2]
        n+=1
    for k in playerExp:
       print(k,playerExp[k])


def main():
    
    window = Tk()
    window.title("RuneScapeExpTracker")
    window.geometry('600x1000')
    window.tk.call('tk', 'scaling', 2.0)

    enterNameLbl = Label(window, text="Enter Username: ")
    enterNameLbl.grid(column=1, row=0)
    userTextBox = Text(window, height=1, width=15)
    userTextBox.grid(column=2, row=0)
    getInfoButton = Button(window, height=0, width=10, text="Get Info", command=getCurrentExp(userTextBox.get("1.0","end-1c")))
    getInfoButton.grid(column=4,row=0,padx=10)

    enterNameLbl.pack()
    userTextBox.pack()
    getInfoButton.pack()

    window.mainloop()


if __name__ == "__main__":
    main()