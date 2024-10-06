"""
RuneScapeExpTracker.py
Shows RuneScape experience player historicals
"""

import requests
import tkinter as tk


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



getCurrentExp("peeperwop")