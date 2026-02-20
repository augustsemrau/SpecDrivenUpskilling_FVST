# Instruktion til Underviser

Intern vejledning til facilitering af Kiro-læringsforløbet. Denne fil er ikke beregnet til deltagerne.

---

## Estimeret tidsplan

| Øvelse | Estimeret tid | Bemærkninger |
|--------|--------------|--------------|
| Opsætning | 15–20 min | Kan tage længere hvis conda ikke er installeret |
| Øvelse 1: Læs en spec | 20–30 min | Velegnet til alle niveauer |
| Øvelse 2: Bed Kiro skrive en spec | 30–45 min | Kræver lidt tålmodighed med iteration |
| Øvelse 3: Udvid en feature | 45–60 min | Den mest tekniske øvelse |
| Øvelse 4: Node.js refaktorering | 60–90 min | Kun for erfarne deltagere |

Samlet forløb: ca. 3–4 timer inkl. pauser. Planlæg en pause efter øvelse 2.

---

## Kendte steder hvor Kiro kan give mangelfulde svar

### Øvelse 2: Spec-generering
- Kiro glemmer nogle gange at inkludere ikke-funktionelle krav. Bed deltagerne tjekke dette specifikt.
- Fejlmeddelelser kan komme på engelsk i stedet for dansk. Påmind Kiro om at bruge dansk.

### Øvelse 3: Kode-generering
- Kiro kan generere kode der ikke matcher import-stier korrekt. Hvis `ModuleNotFoundError` opstår, tjek at uvicorn køres fra `app/`-mappen.
- Valideringslogik (FR-06, FR-07) kan mangle i første forsøg. Bed deltagerne eksplicit nævne kravnumrene.
- Tests kan fejle pga. manglende `autouse`-fixture til at rydde in-memory storage mellem tests.

### Øvelse 4: Node.js migrering
- TypeScript-konfiguration kan mangle `strict: true`. Bed deltagerne tjekke `tsconfig.json`.
- Jest-konfiguration med `ts-jest` kræver en `jest.config.ts` — Kiro glemmer den nogle gange.

### Generelt
- Hvis Kiro forklarer i stedet for at handle, bed deltagerne omformulere med "Implementér nu" eller "Skriv koden".
- Kiro kan miste kontekst i lange samtaler. Start en ny chat hvis svarene bliver upræcise.

---

## Tilpasning af sværhedsgrad

### Lettere (for ikke-tekniske deltagere som Kim)
- Spring øvelse 4 over helt
- I øvelse 3: giv deltagerne den færdige spec-ændring (FR-08) i stedet for at lade dem skrive den selv
- Fokusér på øvelse 1 og 2 — her er den største læringsværdi for ikke-tekniske profiler
- Lad deltagerne arbejde i par med en teknisk person

### Sværere (for erfarne udviklere)
- I øvelse 2: bed dem skrive specen selv først, og derefter sammenligne med Kiros version
- I øvelse 3: tilføj ekstra krav (fx FR-09: maks 5000 kg pr. registrering)
- I øvelse 4: bed dem også migrere autentificeringsspecen til Node.js
- Tilføj en ekstra opgave: skriv en CI/CD pipeline-spec

---

## Fokusområder efter deltagertype

### Kim (ikke-teknisk projektleder)
- Fokus: Øvelse 1 og 2
- Læringsmål: Forstå hvad en spec er, hvordan den bruges som kommunikationsværktøj, og hvordan AI kan hjælpe med at formulere krav
- Undgå: Tekniske detaljer om API-design og kodestruktur
- Nøglepointe: Specs er et fælles sprog mellem forretning og teknik

### Ny udvikler
- Fokus: Øvelse 1, 2 og 3
- Læringsmål: Forstå spec-drevet workflow, se hvordan AI genererer kode fra specs, lære at validere AI-output
- Nøglepointe: AI er et værktøj, ikke en erstatning — altid review koden

### Erfaren udvikler
- Fokus: Alle øvelser, med ekstra tid på øvelse 4
- Læringsmål: Vurdere AI's evne til sprogmigrering, forstå begrænsninger, se specs som dokumentation
- Nøglepointe: Specs giver sporbarhed og konsistens i AI-assisteret udvikling

---

## Anbefalinger til facilitering

### Gruppestørrelse
- Ideel: 4–8 deltagere
- Maks: 12 (med 2 facilitatorer)
- Blandede grupper (teknisk + ikke-teknisk) fungerer godt i øvelse 1–2

### Praktisk opsætning
- Sørg for at alle har Kiro installeret og testet FØR workshoppen
- Hav en backup-plan hvis AWS Bedrock er langsom (det sker)
- Print øvelsernes README-filer som reference, så deltagerne ikke skal skifte mellem filer konstant

### Facilitering under øvelserne
- Gå rundt og hjælp individuelt — Kiro giver forskellige svar til forskellige deltagere
- Saml op efter hver øvelse med en kort fælles diskussion (5 min)
- Bed deltagerne dele interessante eller overraskende Kiro-svar med gruppen

### Tidstyring
- Sæt en timer for hver øvelse og giv besked 5 min før tid
- Det er OK ikke at nå øvelse 4 — kvalitet over kvantitet
- Brug pausen mellem øvelse 2 og 3 til at hjælpe dem der er bagud

---

*Denne fil er til intern brug og bør ikke deles med deltagerne.*
