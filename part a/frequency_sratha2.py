import sys
import json
import re

def main():
    tweet_file = open(sys.argv[2])
    stop_words = open(sys.argv[1])	
    #TODO: Implement
    wordList=[]
    wordListFinal=[]
    cleanedWordList=[]
    for i in tweet_file:
    	tweet = json.loads(i)
    	#output = re.sub("[^\\w]", "", s)
    	wordList.append(re.sub("[^\\w]", " ",tweet['text'].lower()).split(" "))
    #	print (tweet['text'])
    stopList=[]
    for i in stop_words:
    	stopList.append(i.strip())
    #print (stopList)
    wordListFinal.append(sum(wordList, []))
    #print (wordListFinal)
    for i in range(len(wordListFinal[0])):
    	if wordListFinal[0][i]!="" and wordListFinal[0][i]!="t" and wordListFinal[0][i]!="https" and wordListFinal[0][i]!="co" and wordListFinal[0][i]!="m" and wordListFinal[0][i] not in stopList:
    		cleanedWordList.append((wordListFinal[0][i]))
    #print (len(cleanedWordList))
    wordDictionary={}
    wordDictionaryCount={}
    for i in cleanedWordList:
    	if i in wordDictionary.keys():
    		wordDictionary[i]+=1
    	else:
    		wordDictionary[i]=1
    for k in wordDictionary.keys():
    	#print (wordDictionary[k])
    	wordDictionaryCount[k]=wordDictionary[k]/len(cleanedWordList)
    #sorted(wordDictionaryCount.items(), key=lambda x: x[1])
    #print (wordDictionaryCount)
    #items=wordDictionaryCount.items()
    #backitems=[ [v[1],v[0]] for v in items]
    #backitems.sort()
    #sortedlist=[ backitems[i][1] for i in range(0,len(backitems))]
    #print (sortedlist)
    	#print (k, wordDictionaryCount[k],wordDictionary[k])
    finalList=[(k,v) for v,k in sorted([(v,k) for k,v in wordDictionaryCount.items()],reverse=True)]

   
    for i in finalList:
    	print (i[0], i[1])
	

    

    

    


if __name__ == '__main__':
    main()
