import numpy as np
import os

class Deck:
	def __init__(self):
		self.deck = []

	def isEmpty(self):
		return len(self.deck) == 0

	def push(self, card):
		self.deck.append(card)

	def deal(self):
		return self.deck.pop()

	def peek(self):
		return self.deck[len(self.deck)-1]

	def size(self):
		return len(self.deck)

	def print(self):
		for i in range(self.size()):
			print(self.deck[i])

	def shuffle(self):
		np.random.shuffle(self.deck)

class Card:
	def __init__(self, number, suit):
		self.number = number
		self.suit = suit

	def __repr__(self):
		return (str(self.number) + " of " + str(self.suit) + "s")

	def __str__(self):
		return (str(self.number) + " of " + str(self.suit) + "s")

	def __lt__(self, other_card):
		numbers = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
		return numbers.index(self.number) < numbers.index(other_card.number)

class PrivateHand:
	def __init__(self, name):
		self.cards = []
		self.name = name

	def push(self, card):
		self.cards.append(card)

	def print(self):
		print(self.name + "'s Cards: ")
		for i in range(self.size()):
			print(self.cards[i])

	def size(self):
		return len(self.cards)

	def analyze(self):
		if self.cards[0].number == self.cards[1].number:
			print("You have a pair!")
		else:
			print("This is not a pair.")

class CommunityCards:
	def __init__(self):
		self.cards = []
		self.stageCount = 0

	def push(self, card):
		self.cards.append(card)

	def print(self):
		self.stageCount += 1
		if self.stageCount == 1:
			print("The flop: ")
		elif self.stageCount == 2:
			print("The turn: ")
		elif self.stageCount == 3:
			print("The river: ")
		else:
			print("Error: Game should be over")
		for i in range(self.size()):
			print(self.cards[i])
		print()

	def size(self):
		return len(self.cards)

def analyze(hole, community):
	cards = hole.cards + community.cards
	totalClubs = 0
	totalDiamonds = 0
	totalHearts = 0
	totalSpades = 0
	flush = False
	highCard = cards[0]

	for card in cards:
		# Count the number of cards per suit
		if card.suit == "club":
			totalClubs += 1
		elif card.suit == "diamond":
			totalDiamonds += 1
		elif card.suit == "heart":
			totalHearts += 1
		else:
			totalSpades += 1

		# Find high card
		if highCard < card:
			highCard = card

	if totalClubs >= 5 or totalDiamonds >= 5 or totalHearts >= 5 or totalSpades >= 5:
		flush = True


	print("Analyze")
	print(cards)
	print("Clubs: " + str(totalClubs))
	print("Diamonds: " + str(totalDiamonds))
	print("Hearts: " + str(totalHearts))
	print("Spades: " + str(totalSpades))
	print()
	print("Flush: " + str(flush))
	print("High Card: " + str(highCard))

clear = lambda: os.system('clear')
clear()

print("Welcome to Grant's Casino!")
wantToPlay = input("Would you like to play? [y/n] ")
if wantToPlay == "y":
	clear()
	print("Great! Let me shuffle.")

	# Create a shuffled Deck with all 52 cards
	d = Deck()
	numbers = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
	suits = ['club','diamond','heart','spade']
	for j in range(len(suits)):
		for i in range(len(numbers)):
			d.push(Card(numbers[i],suits[j]))
	d.shuffle()

	print("Here are your cards...")
	print()

	# Deal Player 1
	player1 = PrivateHand("Player 1")
	player1.push(d.deal())
	player1.push(d.deal())
	player1.print()
	print()

	player1.analyze()

	print()

	fold = input("Would you like to fold? [y/n] ")
	if fold == "n":
		clear()
		player1.print()
		print()

		# Deal the flop
		CommunityCards = CommunityCards()
		CommunityCards.push(d.deal())
		CommunityCards.push(d.deal())
		CommunityCards.push(d.deal())
		CommunityCards.print()
		analyze(player1, CommunityCards)

		fold = input("Would you like to fold? [y/n] ")
		if fold == "n":
			clear()
			player1.print()
			print()

			# Deal the turn
			CommunityCards.push(d.deal())
			CommunityCards.print()
			analyze(player1, CommunityCards)

			fold = input("Would you like to fold? [y/n] ")
			if fold == "n":
				clear()
				player1.print()
				print()

				# Deal the river
				CommunityCards.push(d.deal())
				CommunityCards.print()
				analyze(player1, CommunityCards)
