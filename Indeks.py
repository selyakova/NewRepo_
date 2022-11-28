from ast import Try
from math import *

print("Tere! Olen sinu sõber - Python!")
nimi=input("Sisesta ona nimi: ")
print(nimi,",oi kui ilus nimi!")
print(nimi, "! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>")
vastus=input("Sisesta 0 või 1: ")
if vastus=="1":
    while True:
        try:
            pikkus=int(input("Sisesta pikkus: "))
            if pikkus>0 and pikkus<273: break
        except:
            print("Error")
    mass=-1
    while mass<0 or mass>400:
        try:
            mass=int(input("Sisesta mass: "))
        except:
            print("Error")
        indeks=round(mass/(0.01*pikkus*pikkus),2)
    print(nimi, "! Sinu keha indeks on: ", indeks)
    if indeks<16:
        print("Tervisele ohtlik alakaal")
    elif indeks>=16 and indeks<19:
        print("Alakaal")
    elif indeks>=19 and indeks<25:
        print("Normaalkaal")
    elif indeks>=25 and indeks<30:
        print("Ülekaal")
    elif indeks>=30 and indeks<35:
        print("Rasvumine")
    elif indeks>=35 and indeks<40:
        print("Tugev rasvumine")
    elif indeks>40:
        print("Tervisele ohtlik rasvumine")
else:
    print("Kahju! See on väga kasulik info!")
print("")
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

arv=input("Arv")
try:
    arv=int(arv)
    print("Int")
except:
    try:
        arv=float(arv)
        print("Float")
    except:
        print:("Tekst")

