import requests
from lxml import *
from lxml import html
from monster import *
from constants import *

def singleCrawl():
    graveyard = []
    
    try:
        graveyard.append(killMonster(test))
    except:
        print("===ERROR===" + reactionTest)
    
    return graveyard

def crawl(suffix):
    graveyard = []
    monsterList = []
    
    r = requests.get(tagUrl + suffix)
    t = html.fromstring(r.content)
    a = t.xpath('//a/@href')

    for x in a:
        if x[:len(isMonster)] == isMonster:
            monsterList.append(x)

    #monsterList = monsterList[:5]
    
    for m in monsterList:
        print(target + m)
        try:
            graveyard.append(killMonster(target + m))
        except:
            print("===ERROR===" + target + m)
    
    return graveyard

def killMonster(url):
    m = monster()
    m.attributes = ['10', '10', '10', '10', '10', '10']
    m.details = []
    m.actions = []
    r = requests.get(url)
    t = html.fromstring(r.content)

    m.name = t.xpath('//h1[@class="post-title"]/text()')[0]

    strong = t.xpath('//strong/text()')
    m.catagory = strong[0]

    p = t.xpath('//p/text()')
    m.ac = p[0].replace(" ", "")[:2]
    m.hp = p[1][p[1].find("(")+1:p[1].find(")")]
    m.speed = p[2].replace(",", "")

    perception = ""

    actionIndex = 0
    for i, x in enumerate(strong[4:]):
        if (x == 'Challenge'):
            m.cr = stripPara(p[i+3])
        elif (x == 'Actions'):
            actionIndex = i+3
        elif (x == 'Legendary Actions'):
            actionIndex = actionIndex
        elif (x == 'Reactions'):
            actionIndex = actionIndex
        else:
            d = detail(x.replace(" ", "").lower(), p[i+3])
            m.details.append(d)
            if (x == 'Skills'):
                skillList = p[i+3].split(",")
                for x in skillList:
                    if x.find("Perception +") > 0:
                        perception = str(10 + int(x[x.find("+")+1:]))

    td = t.xpath('//td/text()')
    for i, x in enumerate(td):
        m.attributes[i] = stripPara(x)
        if i == 4 and perception == "":
            perception = str(int(((int(m.attributes[i])-10)/2))+10)

    m.pp = perception

    e = t.xpath('//p')
    for i, x in enumerate(e[actionIndex+1:len(e)-3]):
        y = x.find('strong');
        if y is None:#No text at all
            y = ""
        else:#there is text
            if y.text is None:#if text isn't strong
                y = x.find('strong').find('em')
                if y is None:#if text isn't EM
                    y = ""
                else:#if text is EM
                    y = y.text
            else:#if the text is strong
                y = y.text
        if (y == 'Actions'):
            actionIndex = actionIndex-1
        elif (y == "Legendary Actions"):
            a = action(y.replace(".", ""), "")
            m.actions.append(a)
            actionIndex = actionIndex-1
        elif (y == "Reactions"):
            reaction = e[actionIndex+i+3].find('strong').find('em').text
            a = action(y.replace(".", "") + ", " + reaction.replace(".", ""), clean(p[i+actionIndex]))
            m.actions.append(a)
            break
        else:
            a = action(y.replace(".", ""), clean(p[i+actionIndex]))
            m.actions.append(a)
    
    return m

def clean(s):
    return s.replace("/", "//").replace("’", "'").replace('“', '"').replace('”', '"').replace("’", "'").replace("’", "'")

def stripPara(s):
    return s[:s.find("(")].replace(" ", "")
