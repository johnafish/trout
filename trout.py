#Trout, written by John Fish. 

import os

fileName = input("What is the file name?")

header = open('header', 'r+')
footer = open('footer', 'r+')

testfile = open('articles/testfile', 'r+')
testhtml = open('htmlArticles/testfile.html', 'w')
testhtml.write(header.read()+'<p>This worked dandily!</p>'+footer.read())
print(testfile.readline())
