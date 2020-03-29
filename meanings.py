
#import nltk
#nltk.download('wordnet')

import sys
sys.setrecursionlimit(500)
from nltk.corpus import wordnet

def text_entry(meaning_list):
	with open('meanings.txt','r') as corpus:
		line=corpus.read().splitlines()
		if(len(line)!=0):
			line_text=line[-1]
			last_number=int(line_text[0:line_text.find('.')].strip())
		else:
			last_number=0
			
		
	with open('meanings.txt','a+') as corpus:
		syns=wordnet.synsets(meaning_list[0])
		if len(syns):
			value=str(last_number+1)+' .'+meaning_list[0]+' :'+syns[0].definition()+' ,'
			corpus.write(value)
			corpus.write('\n')
			print("Meaning written Successfully")
		else:
			print("Unsuccessful Opearion")
			
			
choice=input("Enter 1 to enter the meaning: ")
if choice!="1":
	sys.exit(0)

while(choice=="1"):
    input_word=input("Enter the word here: ")
    meaning_list=[]
    meaning_list.append(input_word)
    text_entry(meaning_list)
    choice=input("Enter 1 to repeat and 2 to exit: ")