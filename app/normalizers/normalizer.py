import re
import phonenumbers


class Normalizer:
    """
    Handles normalization of candidate fields.
    """

    @staticmethod
    def normalize_email(email):
        if not email:
            return None

        return email.strip().lower()

    @staticmethod
    def normalize_phone(phone):
        if not phone:
            return None

        try:
            number = phonenumbers.parse(phone, "IN")
            return phonenumbers.format_number(
                number,
                phonenumbers.PhoneNumberFormat.E164
            )
        except:
            return phone

    @staticmethod
    def normalize_name(name):
        if not name:
            return None

        name = name.strip()

        name = re.sub(r"\s+", " ", name)

        return name.title()

    @staticmethod
    def normalize_company(company):
        if not company:
            return None

        company = company.strip()

        replacements = {
            "Google Inc.": "Google",
            "Google LLC": "Google",
            "Amazon.com": "Amazon"
        }

        return replacements.get(company, company)

    @staticmethod
    def normalize_skills(skills):

        if not skills:
            return []

        skill_map = {
            "python3": "Python",
            "python": "Python",
            "sql": "SQL",
            "fastapi": "FastAPI",
            "machine learning": "Machine Learning",
            "ml": "Machine Learning",
            "mongodb": "MongoDB",
            "reactjs": "React",
            "react": "React"
        }

        normalized = []

        for skill in skills:

            key = skill.lower().strip()

            normalized.append(
                skill_map.get(key, skill)
            )

        return list(set(normalized))