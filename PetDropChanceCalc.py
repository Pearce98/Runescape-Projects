"""
PetDropChanceCalc.py
Takes drop chance and threshold to find what odds of certain kc are
"""
from tkinter import *



bosses = {
        "GWD1 - NM" : [5000, 1000],
        "GWD1 - HM" : [1000, 1000],
    }

def main():

    window = Tk()
    window.title("Pet Drop Chance Calculator")
    window.geometry("600x600")
    window.tk.call('tk', 'scaling', 2.0)

    titleLabel = Label(window, text="Boss Pet Drop Chance Calculator")
    titleLabel.grid(column=1,row=0)
    bossLabel = Label(window,text="Boss: ",justify="right")
    bossLabel.grid(column=0,row=2)
    kcLabel = Label(window,text = "Boss Killcount: ",justify="right")
    kcLabel.grid(column=0,row=3)


    clicked = StringVar()
    clicked.set("Boss Name")
    bossText = OptionMenu(window, clicked, *bosses.keys())
    bossText.grid(column=1,row=2)

    kcText = Text(window, height = 1, width = 5)
    kcText.grid(column = 1, row=3)

    getInfoButton = Button()

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