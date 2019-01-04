import random
import itertools
import time

numbers = ["Bibin", "Debu", "Kunal", "Nishtha", "Pragad" ,"Prajwal", "Sathya", "Shibil","Soumen","Suneesh"]
unmatched = []

def get_random_pairs(numbers):
  pairs = list(itertools.combinations(numbers, 2))
  random.shuffle(pairs)
  return pairs

teams=get_random_pairs(numbers)
no_of_teams=len(teams)
#print no_of_teams
#print(teams)
groups = []


def get_groups(teams):
	if len(teams) <=2:
		#print ("Unused teams")
		#print (unmatched)
		return
	match = []
	firstteam = teams[0]
	match.append(firstteam)
	#unmatched.append(firstteam)
	
	for secondteam in teams:
		if firstteam[0] == secondteam[0] or firstteam[0] == secondteam[1] or firstteam[1] == secondteam[1] or firstteam[1] == secondteam[0]:
			continue
		match.append(secondteam)
		groups.append(match)
		#unmatched.remove(firstteam)
		teams.remove(firstteam)
		teams.remove(secondteam)
		break
	try:
		get_groups(teams)
	except RecursionError as er:
		print("Cannot compute fixture :",teams)
		return
get_groups(teams)
#print(groups)
#def calibrate_grps(numbers):
#	if len(unmatched) < 2:
#			return
	#else:
	#	groups.clear()
#		unmatched.clear()
#		teams = get_random_pairs(numbers)
#		get_groups(teams)
		#calibrate_grps(numbers)
#	return
#calibrate_grps(numbers)

print ("Printing groups")
for match in groups:
	print (match[0], "vs" , match[1])
print ("printing number of teams")
print (no_of_teams)
print ("printing number of groups")
print (len(groups))
print ("Remaining Teams")
print (teams)