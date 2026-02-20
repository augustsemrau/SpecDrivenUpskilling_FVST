# Datamodeller for FangstLog
# Baseret på .kiro/specs/fangst-registrering.md

from datetime import date, datetime
from enum import Enum
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


class FiskearterEnum(str, Enum):
    torsk = "torsk"
    sild = "sild"
    makrel = "makrel"
    roedspaette = "rødspætte"
    kuller = "kuller"
    andet = "andet"


class FangstInput(BaseModel):
    """Request body til oprettelse af en fangst."""
    dato: date
    fartoej_navn: str = Field(..., max_length=100)
    fisker_id: str = Field(..., pattern=r"^FIS-\d{4}$")
    fiskeart: FiskearterEnum
    maengde_kg: float


class FangstRegistrering(BaseModel):
    """Fuld fangstregistrering inkl. auto-genererede felter."""
    id: str = Field(default_factory=lambda: str(uuid4()))
    dato: date
    fartoej_navn: str
    fisker_id: str
    fiskeart: FiskearterEnum
    maengde_kg: float
    registreret_tidspunkt: datetime = Field(default_factory=datetime.now)
