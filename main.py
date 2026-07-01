import argparse

from app.parsers.csv_parser import CSVParser
from app.parsers.json_parser import JSONParser
from app.parsers.resume_parser import ResumeParser

from app.normalizers.normalizer import Normalizer
from app.matcher.entity_resolution import EntityResolver
from app.merger.merge_engine import MergeEngine
from app.provenance.provenance_engine import ProvenanceEngine
from app.confidence.confidence_engine import ConfidenceEngine
from app.projection.projection_engine import ProjectionEngine
from app.validator.validator import Validator


def get_args():
    parser = argparse.ArgumentParser(
        description="Candidate Data Transformer"
    )

    parser.add_argument(
        "--csv",
        required=True,
        help="Path to Recruiter CSV"
    )

    parser.add_argument(
        "--ats",
        required=True,
        help="Path to ATS JSON"
    )

    parser.add_argument(
        "--resume",
        required=True,
        help="Path to Resume PDF"
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to Config JSON"
    )

    return parser.parse_args()


def normalize_candidate(candidate):

    candidate.full_name = Normalizer.normalize_name(candidate.full_name)
    candidate.email = Normalizer.normalize_email(candidate.email)
    candidate.phone = Normalizer.normalize_phone(candidate.phone)
    candidate.company = Normalizer.normalize_company(candidate.company)
    candidate.skills = Normalizer.normalize_skills(candidate.skills)

    return candidate


def main():

    args = get_args()

    # ------------------------------------
    # Parse all sources
    # ------------------------------------

    csv_candidates = CSVParser(
        args.csv
    ).parse()

    ats_candidate = JSONParser(
        args.ats
    ).parse()

    resume_candidate = ResumeParser(
        args.resume
    ).parse()

    # ------------------------------------
    # Normalize
    # ------------------------------------

    csv_candidates = [
        normalize_candidate(c)
        for c in csv_candidates
    ]

    ats_candidate = normalize_candidate(
        ats_candidate
    )

    resume_candidate = normalize_candidate(
        resume_candidate
    )

    # ------------------------------------
    # Entity Resolution
    # ------------------------------------

    if not EntityResolver.is_same_candidate(
        csv_candidates[0],
        ats_candidate
    ):
        print("CSV and ATS candidate do not match.")
        return

    if not EntityResolver.is_same_candidate(
        csv_candidates[0],
        resume_candidate
    ):
        print("CSV and Resume candidate do not match.")
        return

    # ------------------------------------
    # Merge
    # ------------------------------------

    merged = MergeEngine.merge(
        csv_candidates[0],
        ats_candidate,
        resume_candidate
    )

    # ------------------------------------
    # Provenance
    # ------------------------------------

    merged.provenance = ProvenanceEngine.generate()

    # ------------------------------------
    # Confidence
    # ------------------------------------

    merged.confidence = ConfidenceEngine.generate()

    # ------------------------------------
    # Validate
    # ------------------------------------

    Validator.validate(merged)

    # ------------------------------------
    # Projection
    # ------------------------------------

    projected = ProjectionEngine.project(
        merged,
        args.config
    )

    # ------------------------------------
    # Final Output
    # ------------------------------------

    print("\n========== FINAL OUTPUT ==========\n")

    print(projected)


if __name__ == "__main__":
    main()