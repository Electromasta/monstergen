header = "\documentclass[letterpaper,10pt,twoside,twocolumn,openany]{book}\n\\usepackage[english]{babel}\n\\usepackage[utf8]{inputenc}\n\\usepackage{lipsum}\n\\usepackage{listings}\n\\usepackage[bg-print]{dnd}\n\\lstset{\n  basicstyle=\\ttfamily,\n  language=[LaTeX]{TeX},\n}\n\\begin{document}\n\n"
footer = "\n\n\\end{document}"

beginBox = "\\begin{monsterbox}"
endBox = "\end{monsterbox}"

beginAction = "\\begin{monsteraction}"
endAction = "\end{monsteraction}"

textit = "\\textit"
hline = "\hline"
basics = "\\basics"
dice = "\dice"
stats = "\stats"
details = "\details"
stat = "\stat"

space = "	"
newline = "\n"

target = 'http://chisaipete.github.io'
bestiary = target + '/bestiary/'
tagUrl = bestiary + 'tags/'
pages = ['aberration', 'beast', 'celestial', 'construct', 'dragon', 'elemental', 'fey', 'fiend', 'giant', 'humanoid', 'monstrosity', 'ooze', 'plant', 'undead']
dothtml = '.html'

isMonster = '/bestiary/creatures/'

test = 'http://chisaipete.github.io/bestiary/creatures/beldora'

def printToText(fileName, string):
    with open(fileName + ".tex", "w") as text_file:
        print(string, file=text_file)
