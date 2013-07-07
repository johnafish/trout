#Trout, written by John Fish in July 2013.
import os
#Import headers and footer. Each are seperate text files containing within them the code for the half of the code before and after their respective sides of the article. articleList is the list of written articles (simple enough!)
headerOne = open('headerOne', 'r+')
headerTwo = open('headerTwo', 'r+')
footer = open('footer', 'r+')
articleList = open('articleList', 'r+')

fileName = input("What is the file name?")

article = open('articles/'+fileName, 'r+')
articleHTML = open('htmlArticles/'+fileName+'.html', 'w')

articleHTML.write(headerOne.read()+article.readline()+headerTwo.read()+'<p>'+article.read()+'</p>'+footer.read())
