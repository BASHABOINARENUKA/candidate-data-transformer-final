from rapidfuzz import fuzz


class EntityResolver:

    @staticmethod
    def is_same_candidate(candidate1, candidate2):

        # Exact email match
        if (
            candidate1.email
            and candidate2.email
            and candidate1.email == candidate2.email
        ):
            return True

        # Exact phone match
        if (
            candidate1.phone
            and candidate2.phone
            and candidate1.phone == candidate2.phone
        ):
            return True

        # Fuzzy name matching
        if (
            candidate1.full_name
            and candidate2.full_name
        ):

            score = fuzz.ratio(
                candidate1.full_name,
                candidate2.full_name
            )

            if score >= 85:
                return True

        return False