
x1 = 3
x2 = 0

y1 = 5
y2 = 1

x = int(raw_input ('Dame el punto x '))
y = int(raw_input ('Dame el punto y '))

newPoint = (x, y)


xdentro = x >= min(x1, x2) and x <= max(x1, x2)
ydentro = y >= min(y1, y2) and y <= max(y1, y2)

if xdentro and ydentro:
	print 'Esta dentro.' 
else:
	print 'No ta dentro' 


