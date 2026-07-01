import pandas as pd
from typing import List

from app.models.candidate import Candidate


class CSVParser:
    """
    Reads recruiter CSV and converts each row
    into a Candidate object.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self) -> List[Candidate]:
        df = pd.read_csv(self.file_path)

        candidates = []

        for _, row in df.iterrows():

            candidate = Candidate(
                candidate_id=row.get("candidate_id"),
                full_name=row.get("name"),
                email=row.get("email"),
                phone=row.get("phone"),
                company=row.get("company"),
                experience=row.get("experience"),
                location=row.get("location"),
            )

            candidates.append(candidate)

        return candidates