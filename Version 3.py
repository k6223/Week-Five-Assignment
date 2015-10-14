#Kollin Schalhamer
#CIS-125
#Collorated with Sam and Danny

import random	

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
		if gameCounter> 1000:
			print("draw")
			break
	
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	
	
def playRound(PlayerA, PlayerB):
	aCard = PlayerA.pop()
	bCard = PlayerB.pop()
	aRank = getRank(aCard)
	bRank = getRank(bCard)
	if aRank> bRank:
    	#a wins
		PlayerA.insert(0, aCard)
		PlayerA.insert(0, bCard)
	elif aRank< bRank:
    	#b wins
		PlayerB.insert(0, aCard)
		PlayerB.insert(0, bCard)
	else:
		PlayerA, PlayerB = WAR(PlayerA, PlayerB)
    	
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
	# See the README.md file for instructions on coding 
	# This module.
	if len(PlayerA) > 5 and len(PlayerB) > 5:
		AHand = [] 
		BHand = []
		for y in range(5):
			AHand.append(PlayerA.pop())
			BHand.append(PlayerB.pop())
			
		if getRank(AHand[4]) > getRank(BHand[4]):
			PlayerA = AHand + BHand + PlayerA
		elif getRank(AHand[4]) < getRank(BHand[4]):
			PlayerA = AHand + BHand + PlayerB
		else: 
			PlayerA, PlayerB = Lose(PLayerA, PlayerB)
	return PlayerA, PlayerB
	
def Loser(PlayerA, PlayerB):
	#lose cards
	return PlayerA, PlayerB

	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()