from html.entities import codepoint2name
from math import *
from random import *
from stringprep import c22_specials
# Esimene Ülesande

#print("Puu läbimõõdu arvutamine") 
#C=float(input("Anna ümbermõõt: "))
#d=round(C/pi,2)
#print(f"Puu läbimõõt = {d}")


# Teine Ülesasnde

#print("Ristküliku diagonaali arvutamine: ")
#n=float(input("Ristküliku esimene külg: "))
#m=float(input("Ristküliku teine külg: "))
#d=round(sqrt(n**2+m**2),2)
#print(f"Ristkülikukujulise maatüki diagonaal {d}")

# Kolmas Ülesanne

#aeg = float(input("Mitu tundi kulus sõiduks? "))
#teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#kiirus = teepikkus / aeg

#print("Sinu kiirus oli " + str(kiirus) + " km/h")

# Neljadal Ülesanne

#print("Aritmeetiline keskmine")
#A1=int(input("Esimene arv: "))
#A2=int(input("Teine arv: "))
#A3=int(input("Kolmas arv: "))
#A4=int(input("Neljas arv: "))
#A5=int(input("Viies arv: "))
#answer=(A1+A2+A3+A4+A5)/5
#print(f"Aritmeetiline keskmine on {answer}")

# Viies Ülesanne

#print( "   @..@ " )
#print("  (----) ")
#print(" ( \__/ )")
#print("  ^^ "" ^^ ")

#6

#a=randint(0,100)
#b=randint(0,100)
#c=randint(0,100)
#print(f"a={a}\nb={b}\nc={c}")
#answer=a+b+c
#print(f"Ümbermõõt on {answer}")

#7

#P=randint(1,6)
#summa=(12.9*1.1)/P
#print(f"{P}-st, Igaüks maksab {summa}")

#8

#print("Kütusekulu arvutamine")
#l=float(input("Kütse liitride kogus: "))
#km=float(input("Läbitud kilomeetrid: "))
#kulu=(l/km)*100
#print(f"Kütusekulu {kulu}")

#9

#M=int(input("Skol´ko exal?\n:"))
#M=M/60
#tee=M*29.9
#print(f"Skorost´ravna {tee} km")

#10

print("Ajateisendus")
M=int(input("Sisesta aja minutites")) #1h=60min
H=M//60
M=M%60
print(f"{H} : {M}")


