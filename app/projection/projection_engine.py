import json


class ProjectionEngine:

    @staticmethod
    def project(candidate, config_path):

        # Read config.json
        with open(config_path, "r") as f:
            config = json.load(f)

        fields = config.get("fields", [])

        # Convert Candidate object to dictionary
        candidate_dict = candidate.model_dump()

        projected = {}

        # Keep only requested fields
        for field in fields:
            if field in candidate_dict:
                projected[field] = candidate_dict[field]

        return projected