import os

header = "<!DOCTYPE HTML>\n<html>\n    <head>\n        <link rel='stylesheet' type='text/css' href='style.css'>\n        <title>TEST</title>\n    </head>\n<body>\n"
footer = "\n</body>\n</html>"

testfile = open('articles/testfile', 'r+')
testhtml = open('htmlArticles/testfile.html', 'w')
testhtml.write(header+'<p>This worked dandily!</p>'+footer)
print(testfile.read())
