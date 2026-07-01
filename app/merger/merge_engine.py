from app.models.candidate import Candidate


class MergeEngine:

    @staticmethod
    def merge(csv_candidate, ats_candidate, resume_candidate):

        candidate = Candidate()

        # Candidate ID
        candidate.candidate_id = (
            ats_candidate.candidate_id
            or csv_candidate.candidate_id
        )

        # Name
        candidate.full_name = (
            ats_candidate.full_name
            or csv_candidate.full_name
            or resume_candidate.full_name
        )

        # Email
        candidate.email = (
            ats_candidate.email
            or csv_candidate.email
            or resume_candidate.email
        )

        # Phone
        candidate.phone = (
            csv_candidate.phone
            or ats_candidate.phone
            or resume_candidate.phone
        )

        # Company
        candidate.company = (
            ats_candidate.company
            or csv_candidate.company
        )

        # Experience
        candidate.experience = (
            ats_candidate.experience
            or csv_candidate.experience
        )

        # Location
        candidate.location = (
            ats_candidate.location
            or csv_candidate.location
        )

        # Skills (Union)
        candidate.skills = list(
            set(
                csv_candidate.skills
                + ats_candidate.skills
                + resume_candidate.skills
            )
        )

        # Education
        candidate.education = list(
            set(
                csv_candidate.education
                + ats_candidate.education
                + resume_candidate.education
            )
        )

        return candidate