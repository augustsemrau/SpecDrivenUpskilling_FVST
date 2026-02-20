# FangstLog API
# Komplet FastAPI applikation baseret på .kiro/specs/fangst-registrering.md

from datetime import date

from fastapi import FastAPI, HTTPException, Query, Response, status

from .models import FangstInput, FangstRegistrering

app = FastAPI(
    title="FangstLog API",
    description="Fiktivt fangstregistreringssystem til læringsformål",
    version="0.1.0",
)

# In-memory storage
fangster: dict[str, FangstRegistrering] = {}


@app.get("/")
def rod():
    return {"besked": "Velkommen til FangstLog API. Se /docs for dokumentation."}


@app.post("/fangster", status_code=status.HTTP_201_CREATED)
def opret_fangst(fangst_input: FangstInput) -> FangstRegistrering:
    """Opretter en ny fangstregistrering (FR-01, FR-02)."""
    # FR-06: Afvis negativ mængde
    if fangst_input.maengde_kg <= 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"fejl": "Mængde skal være større end 0"},
        )

    # FR-07: Afvis fremtidig dato
    if fangst_input.dato > date.today():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"fejl": "Dato må ikke være i fremtiden"},
        )

    registrering = FangstRegistrering(**fangst_input.model_dump())
    fangster[registrering.id] = registrering
    return registrering


@app.get("/fangster")
def hent_fangster(
    fra_dato: date | None = Query(None, description="Filtrer fra denne dato (inklusiv)"),
    til_dato: date | None = Query(None, description="Filtrer til denne dato (inklusiv)"),
) -> list[FangstRegistrering]:
    """Henter alle fangstregistreringer med valgfri dato-filtrering (FR-03)."""
    resultat = list(fangster.values())

    if fra_dato:
        resultat = [f for f in resultat if f.dato >= fra_dato]
    if til_dato:
        resultat = [f for f in resultat if f.dato <= til_dato]

    return resultat


@app.get("/fangster/{fangst_id}")
def hent_fangst(fangst_id: str) -> FangstRegistrering:
    """Henter én specifik fangstregistrering (FR-04)."""
    if fangst_id not in fangster:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"fejl": "Fangst ikke fundet"},
        )
    return fangster[fangst_id]


@app.delete("/fangster/{fangst_id}", status_code=status.HTTP_204_NO_CONTENT)
def slet_fangst(fangst_id: str):
    """Sletter en fangstregistrering (FR-05)."""
    if fangst_id not in fangster:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"fejl": "Fangst ikke fundet"},
        )
    del fangster[fangst_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
