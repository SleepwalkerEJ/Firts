import time

class myRobot():
	def __init__(self):
		pass

	def autonomo(self, i):
		if i <= 100:	
			print 'El robot al milisegundo ' + str(i) + ' esta ' + 'encendiendo'
		elif i <= 500:
			print 'El robot al milisegundo ' + str(i) + ' esta ' + 'comiendo'
		elif i <= 700:
			print 'El robot al milisegundo ' + str(i) + ' esta ' + 'programando'	
		elif i <= 900:
			print 'El robot al milisegundo ' + str(i) + ' esta ' + 'dormido'

Robocop = myRobot()

i = 0 
while True:
	Robocop.autonomo(i)
	time.sleep(0.01)
	i += 1
	if i >= 1000:
		break





