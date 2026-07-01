import json

from app.models.candidate import Candidate


class JSONParser:
    """
    Reads ATS JSON file and converts it
    into a Candidate object.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self) -> Candidate:

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            candidate = Candidate(
                candidate_id=data.get("candidate_id"),
                full_name=data.get("name"),
                email=data.get("email"),
                phone=data.get("phone"),
                company=data.get("company"),
                experience=data.get("experience"),
                location=data.get("location"),
            )

            return candidate

        except FileNotFoundError:
            raise FileNotFoundError(
                f"ATS JSON file not found: {self.file_path}"
            )

        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format.")

        except Exception as e:
            raise Exception(f"Unexpected error: {e}")