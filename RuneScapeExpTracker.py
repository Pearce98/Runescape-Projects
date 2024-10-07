"""
RuneScapeExpTracker.py
Shows RuneScape total level, exp, and ranks for each skill
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
    playerExp.clear()
    playerLevels.clear()
    playerRanks.clear()
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


def main():
    
    window = Tk()
    window.title("RuneScapeExpTracker")
    window.geometry('575x1000')
    window.tk.call('tk', 'scaling', 2.0)

    def getInput():
        INPUT = userTextBox.get("1.0","end-1c")
        getCurrentExp(INPUT)
        for i in range(len(rankText)):
            rankText[i].delete(1.0,END)
            rankText[i].insert(END,playerRanks[skills[i]])
            levelText[i].delete(1.0,END)
            levelText[i].insert(END,playerLevels[skills[i]])
            expText[i].delete(1.0,END)
            expText[i].insert(END,playerExp[skills[i]])

    enterNameLbl = Label(window, text="Enter Username: ")
    enterNameLbl.grid(column=1, row=0)
    userTextBox = Text(window, height=1, width=12)
    userTextBox.grid(column=2, row=0)
    getInfoButton = Button(window, height=0, width=10, text="Get Info", command=lambda:getInput())
    getInfoButton.grid(column=3,row=0,padx=5)

    skillLabel = Label(window, text="Skill")
    skillLabel.grid(column=1,row=1)
    rankLabel = Label(window,text="Rank")
    rankLabel.grid(column=2,row=1)
    levelLabel = Label(window, text="Level")
    levelLabel.grid(column=3,row=1)
    expLabel = Label(window, text="Experience")
    expLabel.grid(column=4,row=1)

    rankText = []
    levelText = []
    expText = []

    overall = Label(window,text="Overall: ")
    overall.grid(column=1,row=2,padx=5)
    overallRank = Text(window, height=1, width=12, bg="light cyan")
    overallRank.grid(column=2,row=2,padx=5)
    rankText.append(overallRank)
    overallLevel = Text(window, height=1, width=12, bg="light cyan")
    overallLevel.grid(column=3,row=2,padx=5)
    levelText.append(overallLevel)
    overallExp = Text(window, height=1, width=12, bg="light cyan")
    overallExp.grid(column=4,row=2,padx=5)
    expText.append(overallExp)

    atk = Label(window,text="Attack: ")
    atk.grid(column=1,row=3)
    atkRank = Text(window, height=1, width=12, bg="light cyan")
    atkRank.grid(column=2,row=3)
    rankText.append(atkRank)
    atkLevel = Text(window, height=1, width=12, bg="light cyan")
    atkLevel.grid(column=3,row=3)
    levelText.append(atkLevel)
    atkExp = Text(window, height=1, width=12, bg="light cyan")
    atkExp.grid(column=4,row=3)
    expText.append(atkExp)

    defe = Label(window,text="Defence: ")
    defe.grid(column=1,row=4)
    defRank = Text(window, height=1, width=12, bg="light cyan")
    defRank.grid(column=2,row=4)
    rankText.append(defRank)
    defLevel = Text(window, height=1, width=12, bg="light cyan")
    defLevel.grid(column=3,row=4)
    levelText.append(defLevel)
    defExp = Text(window, height=1, width=12, bg="light cyan")
    defExp.grid(column=4,row=4)
    expText.append(defExp)

    stre = Label(window,text="Strength: ")
    stre.grid(column=1,row=5)
    strRank = Text(window, height=1, width=12, bg="light cyan")
    strRank.grid(column=2,row=5)
    rankText.append(strRank)
    strLevel = Text(window, height=1, width=12, bg="light cyan")
    strLevel.grid(column=3,row=5)
    levelText.append(strLevel)
    strExp = Text(window, height=1, width=12, bg="light cyan")
    strExp.grid(column=4,row=5)
    expText.append(strExp)

    constit = Label(window,text="Constitution: ")
    constit.grid(column=1,row=6)
    constitRank = Text(window, height=1, width=12, bg="light cyan")
    constitRank.grid(column=2,row=6)
    rankText.append(constitRank)
    constitLevel = Text(window, height=1, width=12, bg="light cyan")
    constitLevel.grid(column=3,row=6)
    levelText.append(constitLevel)
    constitExp = Text(window, height=1, width=12, bg="light cyan")
    constitExp.grid(column=4,row=6)
    expText.append(constitExp)

    ranged = Label(window,text="Ranged: ")
    ranged.grid(column=1,row=7)
    rangeRank = Text(window, height=1, width=12, bg="light cyan")
    rangeRank.grid(column=2,row=7)
    rankText.append(rangeRank)
    rangeLevel = Text(window, height=1, width=12, bg="light cyan")
    rangeLevel.grid(column=3,row=7)
    levelText.append(rangeLevel)
    rangeExp = Text(window, height=1, width=12, bg="light cyan")
    rangeExp.grid(column=4,row=7)
    expText.append(rangeExp)

    pray = Label(window,text="Prayer: ")
    pray.grid(column=1,row=8)
    prayRank = Text(window, height=1, width=12, bg="light cyan")
    prayRank.grid(column=2,row=8)
    rankText.append(prayRank)
    prayLevel = Text(window, height=1, width=12, bg="light cyan")
    prayLevel.grid(column=3,row=8)
    levelText.append(prayLevel)
    prayExp = Text(window, height=1, width=12, bg="light cyan")
    prayExp.grid(column=4,row=8)
    expText.append(prayExp)

    mage = Label(window,text="Magic: ")
    mage.grid(column=1,row=9)
    mageRank = Text(window, height=1, width=12, bg="light cyan")
    mageRank.grid(column=2,row=9)
    rankText.append(mageRank)
    mageLevel = Text(window, height=1, width=12, bg="light cyan")
    mageLevel.grid(column=3,row=9)
    levelText.append(mageLevel)
    mageExp = Text(window, height=1, width=12, bg="light cyan")
    mageExp.grid(column=4,row=9)
    expText.append(mageExp)

    cook = Label(window,text="Cooking: ")
    cook.grid(column=1,row=10)
    cookRank = Text(window, height=1, width=12, bg="light cyan")
    cookRank.grid(column=2,row=10)
    rankText.append(cookRank)
    cookLevel = Text(window, height=1, width=12, bg="light cyan")
    cookLevel.grid(column=3,row=10)
    levelText.append(cookLevel)
    cookExp = Text(window, height=1, width=12, bg="light cyan")
    cookExp.grid(column=4,row=10)
    expText.append(cookExp)

    wood = Label(window,text="Woodcutting: ")
    wood.grid(column=1,row=11)
    woodRank = Text(window, height=1, width=12, bg="light cyan")
    woodRank.grid(column=2,row=11)
    rankText.append(woodRank)
    woodLevel = Text(window, height=1, width=12, bg="light cyan")
    woodLevel.grid(column=3,row=11)
    levelText.append(woodLevel)
    woodExp = Text(window, height=1, width=12, bg="light cyan")
    woodExp.grid(column=4,row=11)
    expText.append(woodExp)

    fletch = Label(window,text="Fletching: ")
    fletch.grid(column=1,row=12)
    fletchRank = Text(window, height=1, width=12, bg="light cyan")
    fletchRank.grid(column=2,row=12)
    rankText.append(fletchRank)
    fletchLevel = Text(window, height=1, width=12, bg="light cyan")
    fletchLevel.grid(column=3,row=12)
    levelText.append(fletchLevel)
    fletchExp = Text(window, height=1, width=12, bg="light cyan")
    fletchExp.grid(column=4,row=12)
    expText.append(fletchExp)

    fish = Label(window,text="Fishing: ")
    fish.grid(column=1,row=13)
    fishRank = Text(window, height=1, width=12, bg="light cyan")
    fishRank.grid(column=2,row=13)
    rankText.append(fishRank)
    fishLevel = Text(window, height=1, width=12, bg="light cyan")
    fishLevel.grid(column=3,row=13)
    levelText.append(fishLevel)
    fishExp = Text(window, height=1, width=12, bg="light cyan")
    fishExp.grid(column=4,row=13)
    expText.append(fishExp)

    window.mainloop()


if __name__ == "__main__":
    main()