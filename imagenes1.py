f1 = open('images/d1', 'r')
f2 = open('images/de1.txt', 'w')
f3 = open('images/de2.txt', 'w')
f4 = open('images/de3.txt', 'w')

a=0
lineas=0
#8-32
#38-62
#68-92
max=30
min=6
max1=60
min1=36
max2=90
min2=66
lineasMin=3
for line in f1:
	a=0
	lineas=lineas+1
	if (lineas>=lineasMin and lineas<(lineasMin+16)):
		for car in line:
			a=a+1
			if(a<=max and a>min):
				if ((car==' ')|(car=='\'')|(car==';')|(car==':')|(car==',')|(car=='.')):
					f2.write('0;')
				else:
					f2.write('1;')
			#segundo		
			if(a<=max1 and a>min1):
				if ((car==' ')|(car=='\'')|(car==';')|(car==':')|(car==',')|(car=='.')):
					f3.write('0;')
				else:
					f3.write('1;')	
			#tercer		
			if(a<=max2 and a>min2):
				if ((car==' ')|(car=='\'')|(car==';')|(car==':')|(car==',')|(car=='.')):
					f4.write('0;')
				else:
					f4.write('1;')		
		f2.write('\n')
		f3.write('\n')
		f4.write('\n')


f1.close()
f2.close()
f3.close()
f4.close()
