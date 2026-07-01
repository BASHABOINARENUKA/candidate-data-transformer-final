from pydantic import BaseModel
from typing import List, Optional, Dict

class Candidate(BaseModel):
    candidate_id: Optional[int] = None

    full_name: Optional[str] = None

    email: Optional[str] = None

    phone: Optional[str] = None

    company: Optional[str] = None

    experience: Optional[int] = None

    location: Optional[str] = None

    skills: List[str] = []

    education: List[str] = []

    confidence: Dict[str, float] = {}

    provenance: Dict[str, str] = {}