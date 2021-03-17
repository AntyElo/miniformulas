#Sp Formula File 03 floatly, d=xx.06.2020

toP32 = 4294967296
toM16 = 0.000015

s = int(input("s ~"))
e = ""

while s != 0 and e != "exit": 
	e = input()
	if e != "exit":
		s = s - 1
		x = float(input( "x ~" ))
		a = float(input( "a ~" ))
		b = float(input( "b ~" ))
		print( "" )
									
		while ( x < toP32 and x > toM16) and ( a != 0 and a != 1 ): 
			print( str(x) )
			x = a * x + b
		if x > toP32 or x < toM16:
			print( "[sys] X big" )
		elif a == 0 or a == 1:
			print( "[sys] a gliched" )
