# Elpriskollen och reaktorsimulatorn

Ett litet Pythonprojekt med två delar i en Jupyter Notebook: en pedagogisk simulering av en reaktor och en analys av svenska spotpriser från Elpriset just nu.

## Projektfiler

- `Elpriskollen_och_reaktorsimulator.ipynb` - notebook med förklaringar, körbar kod, resultat och grafer.
- `kk.py` - ursprunglig fristående reaktorsimulator, bevarad separat.
- `README.md` - projektbeskrivning och instruktioner.

Notebooken är den samlade, interaktiva versionen. Simulatorn i `kk.py` har inte ändrats.

## Kom igång

1. Öppna `Elpriskollen_och_reaktorsimulator.ipynb` i VS Code eller Jupyter.
2. Välj en Python-kärna.
3. Installera paketen om de saknas:

   ```bash
   python -m pip install requests matplotlib
   ```

4. Kör cellerna uppifrån och ned. Kör om notebooken en annan dag för att hämta dagens priser.

## Notebookens innehåll

### Reaktorsimulator

En deterministisk exempelmodell med starttemperatur, bränslenivå, styrstavarnas nivå och kylflöde. Indata kontrolleras, resultat skrivs ut och temperaturen visas i en graf. Koefficienter och överhettningsgräns är pedagogiska exempel, inte verkliga reaktordata eller ett verktyg för säkerhetsbedömning.

### Elpriskollen

Notebooken hämtar dagens prislista för valt svenskt elområde (`SE1`, `SE2`, `SE3` eller `SE4`) från:

```text
https://www.elprisetjustnu.se/api/v1/prices/ÅÅÅÅ/MM-DD_OMRÅDE.json
```

Den visar lägsta, högsta, medel- och medianpris samt en graf över dagens prisperioder. Priserna visas i kr/kWh. API:t kan returnera flera perioder per timme.

Om API:t inte kan nås används syntetiska exempelvärden så att grafen och analyscellerna fortfarande går att köra. Notebooken markerar då datakällan som `Exempeldata (offline/demo)`; dessa värden är inte aktuella elpriser. Spotpriset omfattar inte nödvändigtvis elhandlarpåslag, skatt eller moms.

## Källa

Livepriser tillhandahålls av [Elpriset just nu](https://www.elprisetjustnu.se). Ange källan om resultaten publiceras: **Elpriser tillhandahålls av Elpriset just nu.se**.
