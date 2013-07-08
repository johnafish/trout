#Trout, written by John Fish in July 2013.
import os, argparse
#Import headers and footer. Each are seperate text files containing within them the code for the half of the code before and after their respective sides of the article. articleList is the list of written articles (simple enough!)
parser = argparse.ArgumentParser(description="Simulate a coin flip a certain amount of times and display the results.")
parser.add_argument('-w', nargs=1)
parser.add_argument('-n', nargs=1)
args = parser.parse_args()
curPath = os.getcwd()

def write(fileName):
    article = open('rawarticles/'+fileName, 'r+')
    articleHTML = open('writing/'+fileName+'.html', 'w')
    articleHTML.write(headerOne.read()+article.readline()+headerTwo.read()+'<p>'+article.read()+'</p>'+footer.read())

def resetAll():
    os.chdir(curPath+"/rawarticles")
    for file in os.listdir("."):
        write(file)

headerOne = open('headerOne', 'r+')
headerTwo = open('headerTwo', 'r+')
footer = open('footer', 'r+')
articleList = open('articles', 'a')
if args.w[0].lower() == "f":
    if args.n == None:
        fileName = input("What is the file name?")
    else:
        fileName = args.n[0]
    write(fileName)
elif args.w[0].lower() == "r":    
    resetAll()
else:
    input("What would you like to do (f/r) ")
    if input.lower() == "f":
        if args.n == None:
            fileName = input("What is the file name?")
        else:
            fileName = args.n[0]
        write(fileName)
    elif input.lower() == "r":
        resetAll()
    

