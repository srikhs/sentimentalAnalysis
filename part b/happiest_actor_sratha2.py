import sys
import csv

def list_duplicates_of(sequence,item):
    startLocation = -1
    locs = []
    while True:
        try:
            loc = sequence.index(item,startLocation+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            startLocation = loc
    return locs

def main():
    sent_file = open(sys.argv[1])
    csv_file = open(sys.argv[2])
    csv_file2 = open(sys.argv[2])
    file_reader = csv.reader(csv_file)
    file_reader2 = csv.reader(csv_file2)
    
    #TODO: Implement
    scores = {} 
    for line in sent_file: 
    	term, score  = line.split("\t")  
    	scores[term] = float(score) 
    wordList=[]
    userListSet2=[]
    userListSet=[]
    userListIndex=[]
    for i in file_reader:
    	if i[0]!="user_name ":
    		userListSet.append(i[0])
    
    userListSet2=set(userListSet)
    
    
    
    
    
    #print (userListSet2)
    indexList=[]
    actorList=[]
    for i in userListSet2:
    
    	actorList.append(i)
    	indexList.append(list_duplicates_of(userListSet,i))
    #print (actorList)
    #print (indexList)
    noOfTweets=[]
    for i in indexList:
    	noOfTweets.append(len(i))
    for i in file_reader2:
    	wordList.append(i[1].split(" "))
    #print (wordList)
    scoreCardList=[]
    for item in wordList:
    	scoreCard=0
    	for i in item:
    		if i in scores:
    			scoreCard=scoreCard+scores[i]
    			#print (scores[i])
    	scoreCardList.append((scoreCard))
    #print (scoreCardList)
   # for 
    #scoreOfActor=0
    actorScores=[]
    for num in range(len(actorList)):
    	scoreOfActor=0
    	for values in indexList[num]:
    		#print (scoreCardList[values])
    		scoreOfActor=scoreOfActor+scoreCardList[values]
    	actorScores.append(scoreOfActor)
    avgScore=[]
    for i in range(len(actorScores)):
    	avgScore.append(actorScores[i]/noOfTweets[i])
   # print (actorScores)
    s = sorted(zip(avgScore, actorList), reverse=True)
    list_1_sorted = [e[1] for e in s]
    list_2_sorted = [e[0] for e in s]
    for i in range(len(actorList)):
    
    	print (str(list_2_sorted[i])+":",list_1_sorted[i])
    
    
    	
    	

if __name__ == '__main__':
    main()
