"""
PetDropChanceCalc.py
Takes drop chance and threshold to find what odds of certain kc are
"""
from tkinter import *



bosses = {
        "GWD1 - NM" : [5000, 1000],
        "GWD1 - HM" : [1000, 1000],
        "Kalphite Queen" : [2500, 500],
        "KBD" : [2500,500],
        "Dagannoth King" : [2500,1500],
        "Chaos Elemental" : [2500,500],
        "Giant Mole" : [2500,500],
        "Giant Mole - HM" : [500,500],
        "Nex" : [2000,400],
        "AOD" : [3000,600],
        "Corp Beast" : [2500,500],
        "Har-Aken" : [200,40],
        "QBD" : [2500,500],
        "Kalphite King" : [2000,400],
        "Legio" : [1000,1200],
        "Vitalis" : [5000,1000],
        "Rax" : [500,200],
        "BeastMaster" : [300,60],
        "Yakamaru" : [300,60],
        "GWD2 - NM" : [2000,400],
        "GWD2 - HM" : [1000,400],
        "Telos" : [1400,300],
        "Magister" : [1000,200],
        "Solak" : [1200,240],
        "Elite Dungeon - Solo" : [300,60],
        "Elite Dungeon - Duo" : [1000,200],
        "Elite Dungeon - Trio" : [1500, 300],
        "Raksha" : [1000,200],
        "Rex Matriarchs" : [2000,1000],
        "Croesus" : [1000,500],
        "Arch-glacor - HM" : [1000,500],
        "Zuk" : [500,100],
        "Zamorak - Group" : [500,100],
        "Zamorak - Solo" : [300,100],
        "Hermod" : [2000,400],
        "Rasial" : [1500,300],
        "Zemouregal & Vorkath - NM" : [2000,400],
        "Zemouregal & Vorkath - HM" : [1000,400],
        "Nakatra - NM" : [400,80],
        "Nakatra - HM" : [240,80]
    }

def main():

    window = Tk()
    window.title("Pet Drop Chance Calculator")
    window.geometry("600x200")
    window.tk.call('tk', 'scaling', 2.0)

    def getInput():
        KILLCOUNT = kcText.get("1.0","end-1c")
        chance = round(calc(clicked.get(),int(KILLCOUNT)),15)
        outputText.delete(1.0,END)
        outputText.insert(END,chance)


    titleLabel = Label(window, text="Boss Pet Drop Chance Calculator")
    titleLabel.grid(column=1,row=0)
    bossLabel = Label(window,text="Boss: ",justify="right")
    bossLabel.grid(column=0,row=2)
    kcLabel = Label(window,text = "Boss Killcount: ",justify="right")
    kcLabel.grid(column=0,row=3)


    clicked = StringVar(window)
    clicked.set("Boss Name")
    bossText = OptionMenu(window, clicked, *bosses.keys())
    bossText.grid(column=1,row=2)

    kcText = Text(window, height = 1, width = 5)
    kcText.grid(column = 1, row=3)

    getInfoButton = Button(window, height=1,width=15,text ="Get Drop Chance",command=lambda:getInput())
    getInfoButton.grid(column=3,row=2)

    outputLabel = Label(window, text="Chance of not having\npet at this kc: ")
    outputLabel.grid(column=0,row=4)
    outputText = Text(window,height=1,width=15)
    outputText.grid(column=1,row=4)

    window.mainloop()


def calc(boss, kc):
    den = bosses[boss][0]
    thresh = bosses[boss][1]
    currThresh = int(kc/thresh)
    kcAtThresh = kc - currThresh * thresh
    n = 0
    base = (den - 1) / den
    chance = 1
    while n < currThresh:
        base = (den - 1 - n) / den
        chance *= pow(base,thresh)
        n+=1
    chance *= pow(base,kcAtThresh)
    return chance



if __name__ == "__main__":
    main()