#Sp Formula File 02 eclipse, d=xx.06.2020

s = int(input("s ~"))
e = ""

while s != 0 and e != "exit": 
	e = input()
	if e != "exit":
		s = s - 1
		x = int(input( "x ~" ))
		a = int(input( "a ~" ))
		b = int(input( "b ~" ))
		print( "" )

		while x < 18446744073709552000 and a > 1: 
			print( str(x) )
			x = a * x + b
		if x > 18446744073709552000:
			print( "[sys] X big" )
		else:
			print( "[sys] a > 1" )
