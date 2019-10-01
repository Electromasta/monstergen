from constants import *

class monster:
    name = "Test"
    cr = "0"
    catagory = "Small Test Creature"
    ac = "10"
    pp = "10"
    hp = "2d6"
    speed = "30"
    attributes = ['10', '10', '10', '10', '10', '10']
    details = []
    actions = []

class action:
    title = ""
    desc = ""
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

class detail:
    title = ""
    desc = ""
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

def createMonster(m):
    result = ""

    result += beginBox + contain(m.name) + contain(m.cr) + newline

    result += space + textit + contain(m.catagory) + "\\\\" + newline
    result += space + hline + newline
    result += space + basics + box(createBasics(m)) + newline
    result += space + hline + newline
    result += space + stats + box(createAttributes(m.attributes)) + newline
    result += space + hline + newline
    result += space + details + box(createDetails(m.details)) + newline
    result += space + hline + " \\\\" + box("1mm") + newline

    result += space + newline
    result += createActions(m.actions)

    result += endBox + newline + newline + newline
    
    return result

def createDetails(d):
    result = newline

    for x in d:
        result += space + space + x.title + " = " + contain(x.desc) + "," + newline
    
    return result + space

def createAttributes(a):
    result = newline

    result += space + space + "STR = " + stat + contain(a[0]) + "," + newline
    result += space + space + "DEX = " + stat + contain(a[1]) + "," + newline
    result += space + space + "CON = " + stat + contain(a[2]) + "," + newline
    result += space + space + "INT = " + stat + contain(a[3]) + "," + newline
    result += space + space + "WIS = " + stat + contain(a[4]) + "," + newline
    result += space + space + "CHA = " + stat + contain(a[5]) + newline + space

    return result

def createBasics(m):
    result = newline

    result += space + space + "armorclass = " + m.ac + "," + newline
    result += space + space + "passiveperception = " + m.pp + "," + newline
    result += space + space + "hitpoints = " + dice + contain(m.hp) + "," + newline
    result += space + space + "speed = " + m.speed + newline + space

    return result

def createActions(actions):
    result = ""

    for x in actions:
        result += space + beginAction + box(x.title)+ newline
        result += space + space + x.desc + newline
        result += space + endAction + newline + newline
    
    return result

def contain(x):
    return "{" + x + "}"

def box(x):
    return "[" + x + "]"

