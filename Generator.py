import random
import itertools
import time
import collections

players = ["Bibin", "Debu", "Kunal", "Nishtha", "Pragad" ,"Prajwal", "Sathya", "Shibil","Suneesh"]
#players = ["Bibin", "Debu", "Kunal", "Nishtha", "Pragad"]
unmatched = []
matchhash = []
maxmatchhash = 3 if len(players)>5 else 2
def get_random_pairs(players):
  pairs = list(itertools.combinations(players, 2))
  random.shuffle(pairs)
  return pairs

teams=get_random_pairs(players)
no_of_teams=len(teams)

groups = []
orderedgroups = []	
originalgroups = []
def get_groups(teams):
	if len(teams) <=2:
		return
	match = []
	firstteam = teams[0]
	match.append(firstteam)
	for secondteam in teams:
		if firstteam[0] == secondteam[0] or firstteam[0] == secondteam[1] or firstteam[1] == secondteam[1] or firstteam[1] == secondteam[0]:
			continue
		matchhash.append(firstteam[0]+secondteam[0])
		matchhash.append(secondteam[0]+firstteam[0])
		matchhash.append(firstteam[0]+secondteam[1])
		matchhash.append(secondteam[1]+firstteam[0])
		matchhash.append(firstteam[1]+secondteam[0])
		matchhash.append(secondteam[0]+firstteam[1])
		matchhash.append(firstteam[1]+secondteam[1])
		matchhash.append(secondteam[1]+firstteam[1])
		match.append(secondteam)
		groups.append(match)
		teams.remove(firstteam)
		teams.remove(secondteam)
		break
	try:
		get_groups(teams)
	except RecursionError as er:
		#print("Cannot compute fixture :",teams)
		#No need to handle this as it will be handled by the while loop below
		return
#To make the matches in sequence so that no players' matches clash
def SequenceMatches(groups):
	orderedgroups.clear()
	
	for match1 in groups:
		for match2 in groups:
			if bool(set(match1[0]+match1[1]).intersection(set(match2[0]+match2[1]))):
				continue
			else:
				orderedgroups.append(match1)
				orderedgroups.append(match2)
				groups.remove(match2)
				groups.remove(match1)
				break

#This loop handles the below
#1. Firsttime invocation of getgroups
#2. Any recursion exceptions for the above method
#3. In case if just 2 teams are left unmatched, check if they can be matched, if not run the pgm again
while len(teams) >= 2:
	if len(teams) == 2:
		firstteam = teams[0]
		secondteam = teams[1]
		if firstteam[0] == secondteam[0] or firstteam[0] == secondteam[1] or firstteam[1] == secondteam[1] or firstteam[1] == secondteam[0]:
			#teams have common player, re iterate the algorithm by resetting
			groups.clear()
			matchhash.clear()
			teams=get_random_pairs(players)
			get_groups(teams)
			counter=collections.Counter(matchhash)
			
			if all(i<=maxmatchhash for i in counter.values()):
				print("==2Not more than 2/3 matches with same opponent, we are good", len(groups), "teams=" , teams)
			else:
				groups.clear()
				matchhash.clear()
				teams=get_random_pairs(players)
				continue
		else:
			#make a match from the last available 2 teams
			match = []
			matchhash.append(firstteam[0]+secondteam[0])
			matchhash.append(secondteam[0]+firstteam[0])
			matchhash.append(firstteam[0]+secondteam[1])
			matchhash.append(secondteam[1]+firstteam[0])
			matchhash.append(firstteam[1]+secondteam[0])
			matchhash.append(secondteam[0]+firstteam[1])
			matchhash.append(firstteam[1]+secondteam[1])
			matchhash.append(secondteam[1]+firstteam[1])
			match.append(firstteam)
			match.append(secondteam)
			groups.append(match)
			teams.remove(firstteam)
			teams.remove(secondteam)
	elif len(teams) > 2:
		groups.clear()
		matchhash.clear()
		teams=get_random_pairs(players)
		get_groups(teams)
		counter=collections.Counter(matchhash)
		if all(i<=maxmatchhash for i in counter.values()):
			print(">2 Not more than 3 matches with same opponent, we are good", len(groups), "teams=" , teams)
		else:
			groups.clear()
			matchhash.clear()
			teams=get_random_pairs(players)
			continue
	
	originalgroups.clear()
	originalgroups = groups.copy() 
	SequenceMatches(originalgroups)
	if len(orderedgroups) < (len(groups)/2):
		groups.clear()
		matchhash.clear()
		teams=get_random_pairs(players)


print ("Matches in sequence")
for match in orderedgroups:
	print (match[0], "vs" , match[1])

print ("Unsorted Original groups")
for match in groups:
	print (match[0], "vs" , match[1])

print ("Printing Remainging groups")
for match in originalgroups:
	print (match[0], "vs" , match[1])

#print ("printing number of teams")
#print (no_of_teams)
#print ("printing number of groups")
#print (len(groups))
#print ("Remaining Teams")
#print (teams)