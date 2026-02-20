# Tests for FangstLog API
# Komplet testsuite baseret på .kiro/specs/fangst-registrering.md

from datetime import date, timedelta

import pytest
from fastapi.testclient import TestClient

from src.main import app, fangster


@pytest.fixture(autouse=True)
def ryd_fangster():
    """Ryd in-memory storage før hver test."""
    fangster.clear()
    yield
    fangster.clear()


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def gyldig_fangst_data():
    return {
        "dato": str(date.today()),
        "fartoej_navn": "Havørnen",
        "fisker_id": "FIS-0042",
        "fiskeart": "torsk",
        "maengde_kg": 340.5,
    }


# --- POST /fangster ---

def test_opret_fangst_succes(client, gyldig_fangst_data):
    """POST /fangster: succesfuld oprettelse returnerer 201."""
    response = client.post("/fangster", json=gyldig_fangst_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["dato"] == gyldig_fangst_data["dato"]
    assert data["fartoej_navn"] == "Havørnen"
    assert data["fisker_id"] == "FIS-0042"
    assert data["fiskeart"] == "torsk"
    assert data["maengde_kg"] == 340.5
    assert "registreret_tidspunkt" in data


def test_opret_fangst_negativ_maengde(client, gyldig_fangst_data):
    """POST /fangster: afvisning ved negativ mængde (FR-06) returnerer 422."""
    gyldig_fangst_data["maengde_kg"] = -5.0
    response = client.post("/fangster", json=gyldig_fangst_data)
    assert response.status_code == 422
    assert "fejl" in response.json().get("detail", {})


def test_opret_fangst_nul_maengde(client, gyldig_fangst_data):
    """POST /fangster: afvisning ved nul mængde (FR-06) returnerer 422."""
    gyldig_fangst_data["maengde_kg"] = 0
    response = client.post("/fangster", json=gyldig_fangst_data)
    assert response.status_code == 422
    assert "fejl" in response.json().get("detail", {})


def test_opret_fangst_fremtidig_dato(client, gyldig_fangst_data):
    """POST /fangster: afvisning ved fremtidig dato (FR-07) returnerer 422."""
    gyldig_fangst_data["dato"] = str(date.today() + timedelta(days=1))
    response = client.post("/fangster", json=gyldig_fangst_data)
    assert response.status_code == 422
    assert "fejl" in response.json().get("detail", {})


def test_opret_fangst_ugyldig_fiskeart(client, gyldig_fangst_data):
    """POST /fangster: ugyldig fiskeart returnerer fejl."""
    gyldig_fangst_data["fiskeart"] = "haj"
    response = client.post("/fangster", json=gyldig_fangst_data)
    assert response.status_code == 422


# --- GET /fangster ---

def test_hent_fangster_tom_liste(client):
    """GET /fangster: returnerer tom liste når ingen fangster."""
    response = client.get("/fangster")
    assert response.status_code == 200
    assert response.json() == []


def test_hent_fangster_returnerer_alle(client, gyldig_fangst_data):
    """GET /fangster: returnerer alle fangster."""
    client.post("/fangster", json=gyldig_fangst_data)
    client.post("/fangster", json=gyldig_fangst_data)
    response = client.get("/fangster")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_hent_fangster_dato_filtrering(client, gyldig_fangst_data):
    """GET /fangster: dato-filtrering virker korrekt."""
    # Opret fangst med dagens dato
    gyldig_fangst_data["dato"] = str(date.today())
    client.post("/fangster", json=gyldig_fangst_data)

    # Opret fangst med gårsdagens dato
    gyldig_fangst_data["dato"] = str(date.today() - timedelta(days=1))
    client.post("/fangster", json=gyldig_fangst_data)

    # Filtrer kun på dagens dato
    response = client.get(f"/fangster?fra_dato={date.today()}&til_dato={date.today()}")
    assert response.status_code == 200
    assert len(response.json()) == 1


# --- GET /fangster/{id} ---

def test_hent_fangst_succes(client, gyldig_fangst_data):
    """GET /fangster/{id}: returnerer korrekt fangst."""
    opret_response = client.post("/fangster", json=gyldig_fangst_data)
    fangst_id = opret_response.json()["id"]
    response = client.get(f"/fangster/{fangst_id}")
    assert response.status_code == 200
    assert response.json()["id"] == fangst_id


def test_hent_fangst_ikke_fundet(client):
    """GET /fangster/{id}: returnerer 404 for ukendt id."""
    response = client.get("/fangster/ukendt-id")
    assert response.status_code == 404
    assert response.json()["detail"]["fejl"] == "Fangst ikke fundet"


# --- DELETE /fangster/{id} ---

def test_slet_fangst_succes(client, gyldig_fangst_data):
    """DELETE /fangster/{id}: sletter fangst, returnerer 204."""
    opret_response = client.post("/fangster", json=gyldig_fangst_data)
    fangst_id = opret_response.json()["id"]
    response = client.delete(f"/fangster/{fangst_id}")
    assert response.status_code == 204

    # Verificer at fangsten er slettet
    get_response = client.get(f"/fangster/{fangst_id}")
    assert get_response.status_code == 404


def test_slet_fangst_ikke_fundet(client):
    """DELETE /fangster/{id}: returnerer 404 for ukendt id."""
    response = client.delete("/fangster/ukendt-id")
    assert response.status_code == 404
    assert response.json()["detail"]["fejl"] == "Fangst ikke fundet"
