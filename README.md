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

## Tekniska val
Jag började med att koda huvudmenyn, då det ommedelbart ger mig en visuell grund för hur jag kan skapa programmet. Då kunde jag komma på de olika alternativen för menyn, en profil med redan fördefinierade värden, som om att man börjar där man sist la av (vilket jag sedan gjort också krävde ett lösenord för att det skulle kännas mer realtistiskt, lösenord ofta förekommer program som innehåller just liknande profiler), ett friläge, där man själv väljer värdena på variablerna på nytt varje gång, varpå man måste definiera gränsvärdena, och sedan ett random läge där värden genereras baserat på gränsvärdena.
**Val av gränsvärden:**
Temperatur måste vara mellan 0 och 2000, vilket jag valde för att vatten förfryser under 0 grader, vilket gör att reaktorn inte hade kunnat fungera då, och 2000 eftersom det då i verkligheten har uppstått en hårdsmälta.
Bränslet fungerar båda enhetligt och procentuellt, vilket är därför jag valde mellan 0 och 100, då 50 av 100 är också 50%, vilket är logiskt till hur man tänker gällande till exempel bilbränsle.
Pumpar statusen är True eller False, då man inte måste ha den på, samt att vattenflödet är mellan 1 och 1500, i och med att vanliga svenska kärnkraftverk har ett vattenflöde på ungefär 1500 m^3/s, vilket kopplar ihop det med den tidigare nämnda realism.
Kontrollstavars värde anges endast i simulationen. Är procentuella för att reflektera hur stängda kontrollstavarna är, utanför simulationen sitter de alltid på 100%, alltså helt stängda.
**Struktur och Matte**
Basmålet ligger på 5000 då det finns sektorer som alltid måste ha el, även om begäran är låg. Därför kan inte all el stängas av, alltså att målet ligger på 0, då detta inte hade angett el till dessa ställen, och simulationen hade varit för kort och förlorat sitt syfte utan ett högt värde.
snittpriset räknas ut med hjälp av formeln (snittpris * 25), då detta speglar hur verkligheten ser ut i en marknadsekonomi, där reglerkrafter fungerar. Alltså, ju högre pris, kommer målet (och incitamentet) att bli mer. Detta inenbär också att priset reagerar portportionellt, liten uppgång av priset, innebär liten ökning av målet och produktionen. På grund av detta får vi alltså vårt dynamiska mål, när vi lagt till vårt basmål, och incitamentet för produktionen, vilket är mest realistiskt. Samtidigt bör det förklaras att kärnkraftverk inte reglerar på samma sätt som vattenkraftverk, syftet är däremot med denna simulationen att kombinera kärnkraftverkens kylnings- och bränslelogik, med kontrollen över vattenflödet och priskänslighet. 
Random värdena på 5% för att en pump går sönder, och 25% för att den lagas, handlar om dynamikens skull i simulationen. I ett riktigt kärnkraftverk, är det mycket mindre sannolikt att pumpen går sönder. Däremot handlar detta om att läsa mönster, och om ett särskild incident har för låg sannolikhet att ske, är det mycket svårare att lära sig utav den incidenten, samt att det gör det möjligt att bara kunna kontrollera allt, kontrollstavar och vattenflöde, och att snabbt kunna klara av simulationen, när man inte alltid kommer ha lika bred kontroll. Detta är inte är verklighetstrogen realism, detta är för simulationens realism, och dess mönster. 
Funktionen: (100 - kontrollstavars_niva) * anrikat_bransle * 0.5
var ett medvetet val, då man måste ta hänsyn till nivån av kontrollstavarna, om de är helt inskjutna, är det svårt att producera el på detta sätt, därför blir det 0 producerat, även med god anrikat bränsle. I verkligheten ger högre kvalitet på bränsle också högre potentiell värmeutveckling, viket är matematisk och fysikaliskt korrekt. Samtidigt som en kärnreaktor inte omvandlar inte allt från den nukleära omvandlingen till ren el, redo att användas. 0.5 ser till att den generereade värmen hamnar på en rimlig nivå till simulationens andra variabler. Utan det skulle det blir svårt att balansera matematiskt.
bortford_varme=vattenflode * 0.2, innebär att ju högre vattenflöde, desto mer termisk energi kan transporteras bort. Konstanten 0.2 fungerar som vattnets specifika värmekapacitet och värmeöverföringskoefficient. Den bestämmer hur effektivt vatten kyler. Detta är realistiskt, då i en riktig reaktor är det kylvattnet som strömar som kyler ner systemet genom att ta upp värmen och omvandla den till ånga.
temperatur = temperatur + genererad-varme - bortford_varme. Tillämpning av termodynamikens första huvudsats (energiprincipen). Förändringen i systemets interna energi (temperaturen) är skillnaden mellan tillförd energi (genererad varme) och bortförd energi (bortford_varme). Om genererad värme är exakt lika stor som bortförd värme blir förändringen noll. Temperaturen ligger då helt stabil, vilket är det absoluta målet vid normal drift av ett kärnkraftverk.
Aktuell_effekt=bortford_varme * 0.35 Ett kärnkraftverk kan aldrig omvandla all värme från reaktorn till ren elektricitet. En stor del av energin försvinner som spillvärme i kylvattnet. Den Termiska verklighetsgraden i riktiga svenska kärnkraftverk har liknande värde, ungefär mellan 30% och 35%.
total_genererad_el+=aktuell_effekt. Simulationen körs i tidssteg, därför är totala producerade energin summan av effekten i varje givet ögonblick
if kontrollstavar < 100: anrikat_bransle -=0.1. Detta är realistiskt då, så länge reaktorn inte är helt avstängd pågår en nukleär kedjereaktion som förbrukar uranatomerna. I verkligheten beror dock bränsleförbrukningen på den exakta effektnivån, men som spelmekanik sätter detta en realistisk tidsfrist för spelaren innan bränslet tar slut.


## Github länk
https://github.com/NowJachill/Huvudprojekt

## För att köra
För att köra programmet behöver man installera det externa biblioteket requests, denna kod finns i programmet som gör detta: %pip install requests

Live-priser tilhandahålls av Elpriset just nu:
(https://www.elprisetjustnu.se)

## Relevanta certifikat för yrkesrollen
Under utbildningen till AI-utvecklare ligger fokus på praktisk kodning och problemlösning, men i arbetslivet är det vanligt att komplettera sin kompetens med externa branschcertifieringar. Detta projekt bygger på logistik, API-hantering och datastrukturering, vilket är grundläggande kunskaper som testas i följande internationellt erkända certifikat:

**Microsoft Certified: Azure AI Fundamentals (AI-901):** Detta certifikat validerar grundläggande förståelse för maskininlärning och AI-koncept. Det ställer krav på grundläggande Python-kunskaper och förståelse för REST API:er – vilket har tillämpats direkt i detta projekt genom integrationen mot elpris-API:t.
**AWS Certified AI Practitioner:** En certifiering från Amazon Web Services som intygar att man förstår hur man bygger och automatiserar datadrivna beslutsprocesser och styrsystem i molnmiljöer.
**Elements of AI (Helsingfors universitet):** En akademisk certifiering som bekräftar djupgående förståelse för hur AI-logik och algoritmer kan appliceras för att lösa komplexa samhälls- och branschproblem, exempelvis optimering av energisystem.