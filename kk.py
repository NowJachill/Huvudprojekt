#Reaktor - Attribut: Temperatur (i celsius), 
# kontrollstavar_nivå (0% till 100%, där 100% är helt inskjutna och stoppar reaktionen), 
# anrikat_bränsle (mängd urvan kvar i procent)
#Matte/logik - Metoder: generera_värme(): 
# värmen ökar baserat på (100 - kontrollsvara_nivå) * bränsle
# om temperaturen blir för hög får man en hårdsmälta
#Kylsystem - Egenskaper: Vattenflöde (liter per sekund), pumpar_status(T/F)
#Matte/logik - kyl_ner(reaktor): sänker reaktorns temp baserat på vattenflöde.
# Ju mer vatten, desto mer värme transporteras till turbinen
#Turbin - Egenskaper: aktuell_effekt (Megawatt, MW)
# total_genererad_el (MWh)
#Matte/logik - producera_el(avledd_värme): räknar ut elektricitet
#Matten här kan vara en verklighetsgrad(t.ex. att 35% av den termiska värmen blir till el).
import random
password="0ab7"
kontrollstavar_niva=100
def temp_check():
    while True:
        try: 
            temperatur=float(input("Vänligen ange en starttemperatur: "))
            if 0 < temperatur < 2000:
                return temperatur
            else:
                print("Temperaturen ej gilltig! Måste vara mellan 0 och 2000!")
        except ValueError:
            print("Vänligen skriv en siffra")
def bransle_check():
    while True:
        try:
            anrikat_bransle=float(input("Mängd uran kvar i procent: "))
            if 0 < anrikat_bransle <= 100:
                return anrikat_bransle
            else:
                print("Ej gilltigt värde! Måste vara mellan 0 och 100")
        except ValueError:
            print("Vänligen ange en siffra")
while True:
    try:
        meny=int(input("Meny - inloggning: \n1: JENSEN\n2: Friläge\n3: Random\n4: Avsluta\n"))
        if meny==1:
            for i in range(5):
                user_password=input(f"Försök kvar: {5-i}\nVänligen ange lösenordet: ")
                if password==user_password:
                    temperatur=150
                    anrikat_bransle=5
                    pumpar_status=True
                    vattenflode=6
                    print("Lyckades!")
                    break
        elif meny==2:
            temperatur=temp_check()
            print(f"Starttemperaturen: {temperatur}°C godkänd")
            anrikat_bransle=bransle_check()
            print(f"Mängd uran kvar: {anrikat_bransle}% godkänd")
        elif meny==3:
            temperatur=random.uniform
            anrikat_bransle=random.uniform
        elif meny==4:
            print("Programmet avslutas...")
            break
        else:
            print("Ej gilltig inmatning")
    except ValueError:
        print("Du måste skriva en siffra!")