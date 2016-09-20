import sys
import json
import re

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    tweet_file2 = open(sys.argv[2])
    wordList=[]
    #TODO: Implement
    
    scores = {} 
    for line in sent_file: 
    	term, score  = line.split("\t")  
    	scores[term] = float(score) 
    #print (scores)
    for i in tweet_file:
    	tweet = json.loads(i)
    	wordList.append(re.sub("[^\\w]", " ",tweet['text'].lower()).split(" "))
    
    #print (wordList)
    #for item in wordList:
    #	for item1 in item:
    #		if ""==item1:
    #			item.remove(item1)
    #print (wordList)
    #for item in wordList:
    scoreCardList=[]
    for item in wordList:
    	scoreCard=0
    	for i in item:
    		if i in scores:
    			scoreCard=scoreCard+scores[i]
    			#print (scores[i])
    	scoreCardList.append((scoreCard))
   
    #print (len(scoreCardList))
    #print (len(wordList))
    #print (scores["rt"])
    newList=[]
    for k in tweet_file2:
    	
    	tweet = json.loads(k)
    	newList.append(tweet['text'])
    #print (newList)
    newList = [w.replace('\n', '') for w in newList]
    #print (newList)
    #print (len(newList))
   
    s = sorted(zip(scoreCardList, newList), reverse=True)
    list_1_sorted = [e[1] for e in s]
    list_2_sorted = [e[0] for e in s]
    

    for i in range(0,10):
    
    	print (str(list_2_sorted[i])+":",list_1_sorted[i])

    for i in range(len(newList)-11,len(newList)-1):
  
    	print (str(list_2_sorted[i])+":",list_1_sorted[i])
if __name__ == '__main__':
    main()
