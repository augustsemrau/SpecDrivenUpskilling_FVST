# Kiro Læringsforløb — Spec-Drevet Udvikling med AI

Velkommen til dette læringsforløb. Du er ved at lære, hvordan man bruger **Kiro** og **spec-drevet udvikling** til at bygge og videreudvikle softwaresystemer med hjælp fra AI.

Dette materiale er lavet til medarbejdere hos Fiskeristyrelsen — uanset om du er projektleder, ny udvikler, eller blot nysgerrig på, hvordan AI indgår i vores arbejdsproces.

> 🚀 **Kom i gang:** Læs [OPSAETNING.md](./OPSAETNING.md) for at hente projektet og sætte dit miljø op — det tager ca. 15 minutter.

---

## Hvad er formålet med dette forløb?

Vi arbejder med en tilgang vi kalder **spec-drevet udvikling**. I stedet for at bede en AI om at "bare skrive noget kode", starter vi med at formulere en præcis **specifikation** (en "spec") — en struktureret beskrivelse af hvad systemet skal kunne, hvilke krav det skal opfylde, og hvilke opgaver det skal udføre.

Derefter lader vi Kiro omsætte den spec til faktisk kode.

Denne tilgang giver os:
- **Sporbarhed** — vi kan altid se, *hvorfor* koden ser ud som den gør
- **Kvalitet** — AI'en arbejder ud fra klare krav frem for løse beskrivelser
- **Samarbejde** — udviklere, projektledere og fagspecialister kan alle bidrage til specs uden at skrive kode

---

## Hvad er Kiro?

Kiro er et AI-drevet udviklingsmiljø (en IDE) bygget ovenpå VS Code. Det understøtter spec-drevet udvikling ved at have et indbygget spec-system i mappen `.kiro/specs/`. Kiro bruger AWS Bedrock med Claude som sprogmodel i baggrunden.

Tænk på Kiro som en meget kompetent udvikler-assistent, der:
- Kan læse og forstå specs
- Kan skrive kode baseret på specs
- Kan forklare, hvad den har gjort og hvorfor
- Arbejder *med* dig, ikke i stedet for dig

---

## Hvad kan dette forløb — og hvad kan det ikke?

### Dette forløb **kan**:
- Lære dig at læse og forstå en spec
- Lære dig at skrive en spec selv (med og uden hjælp fra Kiro)
- Lære dig at bede Kiro om at implementere en spec
- Give dig et realistisk billede af, hvad spec-drevet AI-udvikling indebærer

### Dette forløb **kan ikke**:
- Erstatte egentlig programmeringsundervisning — du behøver ikke at kende kode for at komme i gang, men dybere forståelse kræver mere
- Garantere at Kiros output altid er korrekt — AI kan lave fejl, og menneskelig review er altid nødvendig
- Dække alle Kiros funktioner — vi fokuserer på spec-workflow

### Vigtige begrænsninger at kende:
> ⚠️ **AI er et værktøj, ikke en erstatning for faglig vurdering.** Al kode som Kiro genererer skal gennemgås af en udvikler, inden den tages i brug i et rigtigt system.

> ⚠️ **Send aldrig rigtige persondata eller følsomme oplysninger ind i Kiro.** Al kode og data i dette forløb er fiktiv.

---

## Hvad indeholder dette repository?

```
kiro-laeringsforloeb/
│
├── README.md                  ← Du er her
├── OPSAETNING.md              ← Sådan sætter du miljøet op
│
├── app/                       ← Den fiktive applikation (FangstLog)
│   ├── src/
│   │   ├── __init__.py        ← Python-pakke markør
│   │   ├── main.py            ← FastAPI applikation (skelet — udfyldes i øvelse 3)
│   │   └── models.py          ← Pydantic datamodeller (skelet — udfyldes i øvelse 3)
│   ├── tests/
│   │   ├── __init__.py        ← Python-pakke markør
│   │   └── test_placeholder.py ← Placeholder-test (erstattes i øvelse 3)
│   └── pytest.ini             ← Pytest-konfiguration
│
├── .kiro/
│   ├── steering/              ← Vedvarende regler for Kiro (påvirker alle AI-samtaler)
│   │   └── coding-standards.md
│   └── specs/                 ← Færdige eksempel-specs (start her!)
│       ├── fangst-registrering/
│       │   ├── requirements.md
│       │   ├── design.md
│       │   └── tasks.md
│       └── rapport-generering/
│           ├── requirements.md
│           ├── design.md
│           └── tasks.md
│
├── .gitignore                 ← Python/Node.js/Kiro gitignore
│
└── oevelser/
    ├── 01-laes-en-spec/       ← Begynder: forstå hvad en spec er
    ├── 02-bed-kiro-skrive-spec/ ← Let øvet: lad Kiro skrive en spec
    ├── 03-udvid-feature/      ← Øvet: tilføj en ny funktion (inkl. hints.md)
    ├── 04-node-refaktorering/ ← Avanceret: Python → Node.js (inkl. package-template.json)
    └── eksempel-specs/        ← Ekstra eksempel-specs til reference
        └── bruger-autentificering.md
```

---

## Rækkefølge

Vi anbefaler at gennemgå øvelserne i rækkefølge:

| # | Øvelse | Niveau | Sprog | Hvad du lærer |
|---|--------|--------|-------|---------------|
| 1 | Læs en spec | Begynder | — | Hvad en spec er og indeholder |
| 2 | Bed Kiro skrive en spec | Let øvet | — | Kiro som spec-forfatter |
| 3 | Udvid en feature | Øvet | Python | Spec → kode → test |
| 4 | Node.js refaktorering | Avanceret | Node.js | Migrering med AI |

---

## Kom i gang

Har du allerede sat miljøet op? Start med [Øvelse 1 →](./oevelser/01-laes-en-spec/README.md)

Mangler du opsætning? Se [OPSAETNING.md](./OPSAETNING.md).

> 💡 **Tip:** Hvis Kiro giver et svar der slet ikke matcher det forventede (fx forkert sprog, forkerte filer, eller helt irrelevant kode), start en ny chat-session og vær mere specifik. Referer direkte til filnavne og spec-stier — det hjælper Kiro med at forstå konteksten.

> ⚠️ **Vigtigt om Kiros opførsel:** Kiro skelner mellem *undersøgelse* og *rettelser* — men det gør den kun, hvis du er tydelig. Hvis du skriver "jeg tror der er et problem i main.py", vil Kiro ofte begynde at ændre filen med det samme. Vil du kun have en analyse, så sig det eksplicit: "Analyser main.py for problemer, men lav ingen ændringer." Denne forskel er vigtig at kende fra starten.

---

*Dette læringsforløb er udviklet af Trustworks som en del af IT-fundament projektet hos Fiskeristyrelsen. Applikationen og data er fiktive og har ingen tilknytning til Fiskeristyrelsens faktiske systemer.*
