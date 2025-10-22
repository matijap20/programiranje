"""
broj = 10  #int
ime = "Ana"  #string
znak = 'a'  #char (character)
cijena = 19.99  #float (decimalni broj)
istina = True  #bool (boolean)

if broj > 5:
    print("Broj je veći od 5.")
elif broj == 5:
    print("Broj je jednak 5.")
else:
    print("Broj je manji 5.")

if broj != 5:
    print("Broj nije jednak 5.")

if istina:
    print("True.")
else:
    print("False.")
""" 
#zadatak 2
"""
print("unesi temperaturu")
temperatura = input()
temperatura = int(temperatura)
temperatura = int(input("unesi temperaturu: "))
if temperatura <=  0:
    print("ledenica")
elif temperatura > 0 and temperatura <= 15:
    print("hladno")
elif temperatura > 15 and temperatura <= 25:
    print("ugodno")
else:
    print("vruće")
    """
"""
#petlje
for i in range(10):
    print(i)
for slovo in "bok":
    print(slovo)

brojac = 0
while brojac < 11:
    print(brojac)
    brojac += 1
"""
#zadatak 3: Napišite program koji ispisuje sve parne brojeve od 2 do 20 i 20.
for broj in range(2, 21,):
    if broj % 2 == 0:
        print(broj)
    else:
        continue