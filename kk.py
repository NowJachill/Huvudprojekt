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
while True:
    try:
        meny=int(input("Meny - inloggning: \n1: JENSEN\n2: Friläge\n3: Random\n4: Avsluta\n"))
        if meny==1:
            temperatur=150
            kontrollstavar_niva=50
            anrikat_bransle=5
        elif meny==2:
            temperatur=float(input("Temperaturen: "))
            kontrollstavar_niva=float(input("Nivå på kontrollstavar: "))
            anrikat_bransle=float(input("Mängd uran kvar i procent: "))
        elif meny==3:
            temperatur=random.uniform
            kontrollstavar_niva=random.uniform
            anrikat_bransle=random.uniform
        elif meny==4:
            print("Programmet avslutas...")
            break
        else:
            print("Ej gilltig inmatning")
    except ValueError:
        print("Du måste skriva en siffra!")