
class Player:
	def __init__ (self, name, hp, atk, mp=0):
		self.name = name
		self.hp = hp
		self.atk = atk
		self.mp = mp

	def attack (self, enemy):
		enemy.hp -= self.atk

	def heal (self):
		print self.name + 'is healing'
		self.hp += self.mp	

	def isDead (self):
		return self.hp <= 0

def fight (player1, player2):
	while True: 
		action = raw_input ('attack or heal/n')
		if action == 'heal':
			player1.heal()

		else:

			player1.attack(player2)
			if player2.isDead():
				return player1

			player2.attack(player1)
			if player1.isDead():
				return player1

			if player1.isDead():
				return player2		


hero = Player('El hero', 100, 30, 20)

goblin = Player('Joshua',5 ,3)
beast = Player('Snart beast', 10, 5)
darklord = Player('Ivanok', 2, 100)
dragon = Player('Smaug', 20, 20)

enemies = [goblin, beast, darklord, dragon]

def play ():
	for enemy in enemies:
		print hero.name + 'vs' + enemy.name
		winner = fight(hero, enemy)
		if winner.name != 'El hero':
			print 'Perdites'
			return False
	print 'Ganates'		
