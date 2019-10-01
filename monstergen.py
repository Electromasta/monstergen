from threading import Thread
from constants import *
from monster import *
from crawl import *
from testmonster import *

def main():
    #graveyard = singleCrawl()
    #graveyard.append(testCreateMonster())

    for p in pages:
        t = Thread(target=webToTex, args=(p,))
        t.start()

def webToTex(url):
    out = header
    
    graveyard = crawl(url + dothtml)

    for m in graveyard:
        out += createMonster(m)
    
    out += footer
    printToText(url, out)
    
main()
