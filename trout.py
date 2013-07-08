#Trout, written by John Fish in July 2013.
import os, argparse
#Import headers and footer. Each are seperate text files containing within them the code for the half of the code before and after their respective sides of the article. articleList is the list of written articles (simple enough!)
parser = argparse.ArgumentParser(description="Create a static set of webpages from text files.")
parser.add_argument('-w', nargs=1)
parser.add_argument('-n', nargs=1)
args = parser.parse_args()
curPath = os.getcwd()

def writeFile(fileName):
    article = open(curPath+'/rawarticles/'+fileName, 'r+')
    articleHTML = open(curPath+'/writing/'+fileName+'.html', 'w')
    os.chdir(curPath)
    headerOne = open('headerOne', 'r+')
    headerTwo = open('headerTwo', 'r+')
    footer = open('footer', 'r+')
    articleList = open('articles', 'a')
    articleHTML.write(headerOne.read()+article.readline()+headerTwo.read()+article.read()+footer.read())
        

def resetAll():
    os.chdir("rawarticles")
    for files in os.listdir("."):
        writeFile(files)
        os.chdir("rawarticles")

if args.w[0].lower() == "f":
    if args.n == None:
        fileName = input("What is the file name?")
    else:
        fileName = args.n[0]
    writeFile(fileName)
elif args.w[0].lower() == "r":    
    resetAll()
else:
    input("What would you like to do (f/r) ")
    if input.lower() == "f":
        if args.n == None:
            fileName = input("What is the file name?")
        else:
            fileName = args.n[0]
        writeFile(fileName)
    elif input.lower() == "r":
        resetAll()
    

