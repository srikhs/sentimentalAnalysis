import sys
import json
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
    tweet_file = open(sys.argv[2])
    #TODO: Implement
    scores = {} 
    for line in sent_file: 
    	term, score  = line.split("\t")  
    	scores[term] = float(score) 
    stateList=[]
    stateListFirst=[]
    tweetList=[]
    uniqueStateList=[]
    indexList=[]
    stateCode=["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    stateName=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia',
'Hawaii','Idaho', 'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine' 'Maryland',
'Massachusetts','Michigan','Minnesota','Mississippi', 'Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South  Carolina',
'South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
    for i in tweet_file:
    	tweet = json.loads(i)
    	place1=tweet['place']
	
    	if place1 is not None:
    		if place1['country_code']=='US':
    			if ',' in place1['full_name']:
	    			stateListFirst.append(place1['full_name'].split(", ")[0])
	    			
    				if (place1['full_name'].split(", ")[1]) in stateCode:
		    			stateList.append(place1['full_name'].split(", ")[1])
		    			tweetList.append(tweet['text'])
    			
    #print (stateList)
    #print (tweetList)
   
    #print (stateCode)
    for i in range(len(stateList)):
    	if stateList[i] not in stateCode:
    		#print(stateListFirst[i])
    		#print (stateCode[stateName.index(stateListFirst[i])])
    		#if stateList[i] in stateName:
    		stateList[i]=stateCode[stateName.index(stateListFirst[i])]
    #print (stateList)
    
    
    s = sorted(zip(stateList, tweetList))
    list_1_sorted = [e[1] for e in s]
    list_2_sorted = [e[0] for e in s]
    #print (list_2_sorted)
    uniqueStateList=set(list_2_sorted)
    #print (uniqueStateList)
    for i in uniqueStateList: 
    	indexList.append(list_duplicates_of(list_2_sorted,i))
   # print (indexList)
    

   

    noOfTweets=[]
    wordList=[]
    for i in indexList:
    	noOfTweets.append(len(i))
    for i in list_1_sorted:
    	wordList.append(i.split(" "))
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
    for num in range(len(uniqueStateList)):
    	scoreOfActor=0
    	for values in indexList[num]:
    		#print (scoreCardList[values])
    		scoreOfActor=scoreOfActor+scoreCardList[values]
    	actorScores.append(scoreOfActor)
    avgScore=[]

    for i in range(len(actorScores)):
    	avgScore.append(actorScores[i]/noOfTweets[i])
   # print (actorScores)
 
    s = sorted(zip(avgScore, uniqueStateList), reverse=True)
    list_11_sorted = [e[1] for e in s]
    list_22_sorted = [e[0] for e in s]
    for i in range(0,len(uniqueStateList)):
    
    	print (str(list_22_sorted[i])+":",list_11_sorted[i])
    #for i in range(len(uniqueStateList)-1,len(uniqueStateList)-6,-1):
    #	print (str(list_22_sorted[i])+":",list_11_sorted[i])

    

    
    			
    			
        		

    		
    			

if __name__ == '__main__':
    main()
