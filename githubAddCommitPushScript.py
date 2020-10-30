import random
import datetime
import time
import os
import subprocess
import json


delay  = 2 #The time between each commit
lineChangeMin,lineChangeMax = 10,40 #the number of line changesn per commit
minCommitCount,maxCommitCount = 7,15 # The number of commits per push
text = "Im Batman" # if youd like this, just go and erase line 21

listOfQuotesTakenFromJSON=[]
with open('quotes.json','r') as quotesList:
	quotesJSON = json.load(quotesList)
for quote in quotesJSON['quotes']:
	listOfQuotesTakenFromJSON.append(quote)

def execute_shell_command(cmd, work_dir):
    pipe = subprocess.Popen(cmd, shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print (out, error)
    pipe.wait()

def updateFileForLineChanges():
	f=open('sampleTextFile.txt',"w")
	randomRangeTextLineChange = random.randint(lineChangeMin,lineChangeMax)
	for i in range(randomRangeTextLineChange):
		randomQuoteSelection = random.randint(1,len(listOfQuotesTakenFromJSON)-1)
		text = listOfQuotesTakenFromJSON[randomQuoteSelection]+"\n"
		f.write(text)
	f.close()
	time.sleep(delay)

def performGreenificationOnce():
	updateFileForLineChanges()
	execute_shell_command("git add .",".")
	commitText = "git commit -m \" commited at "+str(time.time())+"\""
	execute_shell_command(commitText,".")

def repeatCommitsForHarderGreenification():
	randomRangeCommit = random.randint(minCommitCount,maxCommitCount)
	for i in range(randomRangeCommit):
		performGreenificationOnce()
	execute_shell_command("git push",".")

repeatCommitsForHarderGreenification()

