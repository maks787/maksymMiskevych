from math import *
from random import *
#1.
print("Puu läbimõõdu arvutamine")
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.
###if C>0:
		#d=round(C/pi,2)
		#print(f"puu labimoot = {d}")
	#else:
		#print("C peab olema suurem kui 0")
#except:
	#print("andmetüüp on vale")
#2 Рассчитайте длину диагонали прямоугольного участка земли размерами Nm x Mm в командной строке Python. N и M спрашивают пользователя.
#print("ristkuliku omadused")
try:
	M=float(input("sisesta M"))
	N=float(input("sisesta N"))
	if M>0 and N>0:
		d=round(sqrt(N**2+M**2),2)
		print(f"ristkülikukujulise maatüki diagonaal on (d)")
	else:
		print("M ja N peab olema suurem kui 0" )
except:
	print("M ja N vaja sisestada")
#print()
try:
	aeg = float(input("mitu tundi kulus soiduks?"))
	teepikkus = float(input("Mitu kilomeetrit soitsid? "))
	if aeg>0 and teepikkus>0:
		kiirus=teepikkus / aeg
		print("sinu kiirus oli " + str(kiirus) + "km/h")
		kiirus = teepikkus / aeg
		print("Siny kiirus oli " + str(kiirus) + " km/h")
	else:
		print("aeg ja teepikkus peab olema suurem kui 0")
except:	
	print("Andmetüüp on vale!")
##4
print("aritmeetiline keskmine")	
try:
	A1=int(input("esimene arv"))
	A2=int(input("Teine arv"))
	A3=int(input("kolmas arv"))
	A4=int(input("neljas arv"))
	A5=int(input("viies arv")) 
	if A1<0 and A2>0 and A3>0 and A4>0 and A5>0:
		Ak=(A1+A1+A3+A4+A5)/5
		print("aritmeetiline keskmine =",Ak)
	else:
		print("andmed peab olema suurem kui 0")
except:	
	print("andmetüüp on vale!")
#print(f"keskmine on {K}")
#5
#print("  @..@ ")
#print(" (----)")
#print(" (\__/)")
#print('^ ^ "" ^ ^')
#6


print("Arvutamine kolmnurga umbermoodu")
try:
	a=randint(0,100)
	b=randint(0,100)
	c=randint(0,100)
	print(f"a={a}\nb={b}\nc={c}")
	P=round(a+b+c,2)
	print("ümbermõõt," P)
except:
	print("andmetüüp on vale")
#7

print("pitsa jootraha arvutamine")

P=randint(1,6)
summa:(12.9*1.1)/P
print(f"{P}-st, igauks maksab {summa}")

#8
#from random import *
#l=float(input("sisestage taidetud kutuse liitrid: "))
#km=float(input("sisestage labitud kilomeetrid: "))
#kulu:(l/km)*100
#print(f"kutusekulu",kulu)
 #9
 #print("rulluisutajad")
 try:
	M=int(input("minutid:"))
	M=M/60
	if M>0:
		tee=M*29.9
		print("andmed peab olema suurem kui 0")
 except: 
	print("andmetüüp on vale!")

 #10
try:
	M=int(input("sisesta aja minutites: "))
	if M>0:
		H=M//60
		M=M%60
		print(f"{H}:{M}")
	else:	
		print("andmed peab olema suurem kui 0")
except: 
	print("andmetüüp on vale!")


print("Ema robot")
a=input("sisesta: ")
print(a.isalpha(), a.isdigit())
if a.isdigit() and int(a)>0 and int(a)<=5:
	a=int(a)
	if a==5:
		pass
	elif a==4:
		pass
	elif a==3:
		pass
	elif a==2 or a==1:
		pass
else:	
	print("Sa valesti vastas")