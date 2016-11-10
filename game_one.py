import random

plays = ['piedra', 'papel', 'tijeras']
computer = plays[random.randint(0, 2)]

jugada = raw_input('Chose your weapon: \n')

def play_game ():
	
	if jugada == computer:
		print 'Empate, play again'
		return

	elif jugada == 'piedra' and computer == 'papel':
		print 'papel envuelve a piedra'
		print 'You lose dude'

	elif jugada == 'piedra' and computer == 'tijeras':	
		print 'piedra rompe tijeras'
		print 'You win pal'

	elif jugada == 'tijeras' and computer == 'piedra':
		print 'piedra rompe tijeras'
		print 'You lose dude'

	elif jugada == 'tijeras' and computer == 'papel':
		print 'tijeras corta papel'
		print 'You win pal'

	elif jugada == 'papel' and computer == 'piedra':
		print 'papel envuelve a piedra'
		print 'You win pal'

	elif jugada == 'papel' and computer == 'tijeras':
		print 'tijeras corta papel'
		print 'You lose dude'	

print computer	
play_game()	