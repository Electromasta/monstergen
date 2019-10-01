from constants import *
from monster import *

def testCreateMonster():
    d1 = detail("skills", "Perception +3")
    d2 = detail("senses", "Darkvision 60ft")
    a1 = action("Keen Sight and Smell", "The owlbear has advantage on Wisdom (Perception) checks that rely on sight or smell.")
    a2 = action("Multiattack", "The owlbear makes two attacks: one with its beak and one with its claws.")
    a3 = action("Beak", "+7 (1d10+5) Piercing")
    a4 = action("Claws", "+7 (2d8+5) Slashing")

    m = monster()
    m.name = "Owlbear"
    m.cr = "3"
    m.catagory = "Large Monstrosity,unaligned"
    m.ac = "13"
    m.pp = "11"
    m.hp = "7d10+21"
    m.speed = "40 ft"
    m.attributes = ["20", "12", "17", "3", "12", "7"]
    m.details = [d1, d2]
    m.actions = [a1, a2, a3, a4]
    return m
