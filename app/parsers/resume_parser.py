import re
import pdfplumber

from app.models.candidate import Candidate


class ResumeParser:
    """
    Reads a resume PDF and extracts candidate information.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text(self) -> str:
        """
        Extract all text from the PDF.
        """
        text = ""

        try:
            with pdfplumber.open(self.file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

            return text

        except FileNotFoundError:
            raise FileNotFoundError(
                f"Resume not found: {self.file_path}"
            )

        except Exception as e:
            raise Exception(f"Error reading PDF: {e}")

    def parse(self) -> Candidate:
        """
        Extract candidate details from resume text.
        """

        text = self.extract_text()

        # -----------------------------
        # Name (Assume first line)
        # -----------------------------
        lines = text.split("\n")
        name = lines[0].strip() if lines else None

        # -----------------------------
        # Email
        # -----------------------------
        email_match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )

        email = email_match.group(0) if email_match else None

        # -----------------------------
        # Phone
        # -----------------------------
        phone_match = re.search(
            r"(\+?\d[\d\s\-]{9,15})",
            text
        )

        phone = phone_match.group(0).strip() if phone_match else None

        # -----------------------------
        # Skills
        # -----------------------------

        known_skills = [
            "Python",
            "Java",
            "SQL",
            "FastAPI",
            "Machine Learning",
            "Deep Learning",
            "MongoDB",
            "React",
            "Node.js",
            "Docker",
            "Git"
        ]

        skills = []

        lower_text = text.lower()

        for skill in known_skills:
            if skill.lower() in lower_text:
                skills.append(skill)

        # -----------------------------
        # Education
        # -----------------------------

        education = []

        education_keywords = [
            "B.Tech",
            "Bachelor",
            "M.Tech",
            "Master",
            "CBIT",
            "University"
        ]

        for word in education_keywords:
            if word.lower() in lower_text:
                education.append(word)

        # -----------------------------
        # Candidate Object
        # -----------------------------

        candidate = Candidate(
            full_name=name,
            email=email,
            phone=phone,
            skills=skills,
            education=education
        )

        return candidate