# Hints til Øvelse 3

Sidder du fast? Her er nogle hints der kan hjælpe dig videre — uden at afsløre løsningen.

---

## Hint 1: Kiro skriver ikke altid kode første gang

Hvis Kiro giver dig en forklaring i stedet for at skrive kode, så prøv at være mere direkte. Sig fx: "Implementér koden nu og skriv den i filen `app/src/main.py`." Kiro reagerer bedre på konkrete instruktioner end åbne spørgsmål.

---

## Hint 2: Hvis tests fejler

Kopiér hele fejloutputtet fra terminalen og send det til Kiro i chatten. Kiro er god til at læse fejlbeskeder og rette koden. Skriv fx: "Jeg fik denne fejl da jeg kørte pytest — kan du rette det?"

---

## Hint 3: FR-08 filtrering på fiskeart

Tænk over, hvordan de eksisterende query-parametre (`fra_dato`, `til_dato`) er implementeret i `GET /fangster`. Din nye parameter følger samme mønster — den skal bare filtrere på et andet felt. Kig på hvordan `fra_dato` bruges som inspiration.

---

## Hint 4: Applikationen starter ikke

Tjek at du har aktiveret conda-miljøet (`conda activate kiro-laering`) og at du står i `app/`-mappen, når du kører `uvicorn src.main:app --reload`.

---

## Hint 5: Import-fejl

Hvis du ser `ModuleNotFoundError`, skyldes det sandsynligvis at du kører uvicorn fra den forkerte mappe. Du skal stå i `app/`-mappen (ikke i `app/src/`).
