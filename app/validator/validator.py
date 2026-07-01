class Validator:

    @staticmethod
    def validate(candidate):

        if not candidate.full_name:
            raise ValueError("Name is required.")

        if not candidate.email:
            raise ValueError("Email is required.")

        if "@" not in candidate.email:
            raise ValueError("Invalid email.")

        if candidate.phone and not candidate.phone.startswith("+"):
            raise ValueError("Invalid phone number.")

        return True