import random
from operator import itemgetter

class hootgame:
	def __init__(self):
		self.board = 'ygobprbprygborpygobprgyobprygborpygborp'
		self.makeDeck()
		self.owls = range(0,6)
		self.card = ''
		self.NEST = len(self.board)

	def makeDeck(self):
		cards = 'rrrrrrooooooyyyyyyggggggbbbbbbpppppp'
		self.deck = ''.join(random.sample(cards,len(cards)))

	def nextCard(self):
		if len(self.deck) == 0:
			self.makeDeck()
		self.card = self.deck[0:1]
		self.deck = self.deck[1:]
		return self.card

	def isSpaceOccupied(self, index):
		if index == self.NEST:
			return False
		for owlPosition in self.owls:
			if owlPosition == index:
				return True
		return False

	def indexOfNextColor(self, color, owlPosition):
		while self.isSpaceOccupied(owlPosition):
			owlPosition = self.board.find(color, owlPosition + 1)
			if owlPosition == -1:
				owlPosition = self.NEST
		return owlPosition

	def isWon(self):
		return min(self.owls) == self.NEST
		

	def moveOwl(self, owlIndex):
		self.owls[owlIndex] = self.indexOfNextColor(self.card, self.owls[owlIndex])

	def printBoard(self):
		print self.card + "-" * len(self.board)
		spaces = list(' ' * len(self.board))
		for x in self.owls:
			if x < self.NEST:
				spaces[x] = 'X'
		print "".join(spaces)
		print self.board

class randomowlstrategy:
	def name(self):
		return "Random"

	def owlToMove(self, game):
		while True:
			n = random.randint(0,5)
			if game.owls[n] < game.NEST:
				return n

class lastowlstrategy:
	def name(self):
		return "Last"

	def owlToMove(self, game):
		return min(enumerate(game.owls), key=itemgetter(1))[0] 

class farthestowlstrategy:
	def name(self):
		return "Farthest"

	def owlToMove(self, game):
		maxDistance = 0
		maxIndex = -1
		for owlIndex in range(0, 6):
			currentIndex = game.owls[owlIndex]
			nextIndex = game.indexOfNextColor(game.card, currentIndex)
			distance = nextIndex - currentIndex
			if distance > maxDistance:
				maxIndex = owlIndex
				maxDistance = distance
		return maxIndex


def playGame(strategy):
	game = hootgame()
	i = 0
	while not game.isWon():
		game.nextCard()
		owlIndex = strategy.owlToMove(game)
		game.moveOwl(owlIndex)
		#game.printBoard()
		i += 1
	return i

def testStrategy(strategy):
	x = 1000
	totalMoves = 0
	for i in range(0,x):
		totalMoves += playGame(strategy)
	print "%s average moves %.1f" % (strategy.name(), totalMoves/float(x))


testStrategy(lastowlstrategy())
testStrategy(farthestowlstrategy())
testStrategy(randomowlstrategy())






