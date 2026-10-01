# Kärnkraftsimulation baserat på elpriser

## Mål
Målet med detta projekt är att adressera den potentiell ekonomisk balansering och optimering av elproduktion, samt visa ett exempel på hur ett kärnkraftverk baserat på begäran av elprisen skulle kunna se ut. Lite el baserat på efterfrågan leder till dyrare el i sig. Alltså, om begäran på elpriset är högt skulle kärnkraftverk kunna jobba för att minska det, genom att producera mer el när det faktiskt behövs, samtidigt som om begäran är låg sikta på ett basmål för produktionen. AI-utvecklare kan förväntas ta hand om mängder olika sorters projekt, skapa lösning via kod för att kunna reda ut de bästa besluten som möjligt, vilket är det som jag också "simulerar" inom detta projekt. Samtidigt finns det ett personligt intresserat mål att göra det likt en spelsimulation, för att göra informationen om hur kärnkraftverk fungerar mer begriplig. På grund av detta är projektet ett mer förenklat exempel av hur ett kärnkraft fungerar. 

## Metod
För att utveckla simulationen har information från elpriskollens öppna API hämtats och analyserars i JSON-format. För att kunna använda detta, och sedan utveckla ett dynamiskt mål av elproduktionen baserat på elpriserna, har det externa bibioteket requests installerats. För att baserat det på varje dag har det interna biblioteket datetime använts. I spelstrukturen används även biblioteket random, för en mer dynamiskt simulation.
För att kolla gränsvärdena på alla delar som finns inom ett kärnkraft, har funktioner som validerar värdena på bränslet, kontrollstavarnas nivå samt pumpar statusen och vattenflödet som kommer i och med om den är igång eller inte. Sedan för att beräkna för användaren att värdena som angetts är korrekta har en funktion som printar ut att de är godkända. Själva spelstrukren är också en funktion, då det underlättar rejält att man kan kalla den på samma sätt under varje val i menyn, utan att behöva skriva om kod.
Klassen Incident har skapat, där alla sorters incidenter inom kärnkraftverkets teknik sker, och skickar ut ett VMA om det skulle ske, från basklassen, medan alla incidenters individuella meddelanden sker i barnklasserna, men ärver fortfarande ett VMA där förklaring till varför incidenten har skett förklaras.
Huvudmenyn kopplar samman allt, där användarens input ställer över med villkor (och om inte det gör det fångas det upp av try/except). Alla värdena valideras igenom tidigare nämnda funktionerna, för att målet sedan ska genereras baserat på dagens elpriser, varpå simulation fortsätter via loop, till en allvarlig incident sker, tillräckligt med el skapats, eller användaren väljer att avsluta.
(Länk till API:n för nuvarande datumet som detta skrivs: https://www.elprisetjustnu.se/api/v1/prices/2026/10-01_SE3.json)

## Resultat
Resultatet blev en spelsimulation, vars egenskaper går att begripa, men är ändå inte för förenklat. Efter validering i huvudmenyn startar simulationen:

Starttemperaturen: 50.0°C godkänd
Mängd uran kvar: 74.0% godkänd
Status: Pump igång: False, aktuellt flöde: 0.0 l/s

(Validering av värdena)

Hämtade elpriser lyckades!
Dagens snittpris på elbörsen: 76.2 öre/kWh

(Dynamiskt mål aktiverat)

Runda: 1
Temperatur: 50.0
Vattenflöde: 0.0 l/s (Pump: Ej igång)
Uran kvar: 74.0
Kontrollstavar: 100% inskjutna
Antal el producerad: 0.0 MWh
0.0% av målet - 6905 MWh
Vad vill du göra?
1: Ändra kylsystem (pump/flöde)
2: Justera kontrollstavar
3: Gå till nästa runda
4: Avsluta spelet

(Spelstrukturen med val)
Ju mer öppna kontrollstavarna är, desto mer värme produceras. Vattenflödet, om pumpen är igång, för bort värme och skapar energi av det. Det liknar ett klassiskt spel, för användarens förståelse.

## Analys
Ett väldigt omtalat problem är hur dyr elen är. Många produktioner använder redan elpriser för att styra hur mycket man kan producera, baserat på dyr eller billig el, så varför inte göra det med produktionen av el också? När elen är dyr kommer många produktioner att försvagas, medan produktioner av el kan öka för att det ändå kommer finnas en begäran på el. Numera är kärnkraftverken inte optimerat på detta system, vilket gör att det kan förekomma brister inom stabiliteten av elnäten, då elpriserna varierar så mycket. 
Om man tänker på det i en helbild, så finner vi ett tydligt mönster, där dyr el innebär högre produktionsgrad av ny el. Simuleringar, likt den som gjorts här, passar väl med AI-utvecklingen, då AI lär sig känna mönster och lär sig ta beslut baserat på tidigare data.
Dynamiska målen inom programmet följer elpriset konkret, men AI:s inlärda mönster kan expanderas för att ta hänsyn till fler saker, såsom årstid, väder, klimat, befolkning och veckodag. Alltså, på flera grader än det som använts inom detta program kan AI:s mönster lära sig att ta bäst ekonomiskt beslut för att höja eller minska produktionen av el, även något som kan vara betydligt svårare att analysera för människor. Detta projekt kan ses som en startskott för att se vad AI kan göra för att lära sig, inte bara inom kärnkraft, utan alla mönster i sig.

## Reflektion
**Vad gick bra:**
Att kunna göra en balans mellan begripelse och realism kan ofta vara svårt att greppa, men lösningen blev tillfredsställe utifrån förväntningarna som hades. Alltså, spelsimulationen lyckades förenkla kärnkraftverk tillräkligt, passar till själva "speldelen", utan att bli för orealistisk, passar till själva "simulationsdelen."
**Vad var svårt:**
Generellt sett mycket kod att ha reda på. Även om det stod var exakt fel uppstod, var det inte allt lika lätt att hitta som man skulle velat. Det var svårt på sätt och vis svårt att inte göra något alltför ambitiöst, vilket skulle göra att koden blev ännu längre
**Vad jag skulle kunna göra annorlunda:**
Skulle kunna se till att planering sker mer i ett stadie där man sortera koden mer smidigt. Som sagt, problem uppstod med att hitta i den långa koden, detta förlättades til viss del av de olika cellerna i Jupyter Notebook, men ändå, extra planering skulle göra att koden blev mer clean, till exempel som att göra fler klasser och funktioner tidigare, för att till exempel se till att koden för strukturen och menyn inte blir lika stora, men ändå fungerar

## Github länk
https://github.com/NowJachill/Huvudprojekt

## För att köra
För att köra programmet behöver man installera det externa biblioteket requests, denna kod finns i programmet som gör detta: %pip install requests

Live-priser tilhandahålls av Elpriset just nu:
(https://www.elprisetjustnu.se)