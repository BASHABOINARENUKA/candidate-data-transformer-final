from app.parsers.csv_parser import CSVParser
from app.parsers.json_parser import JSONParser
from app.parsers.resume_parser import ResumeParser

from app.merger.merge_engine import MergeEngine
from app.projection.projection_engine import ProjectionEngine


def test_projection():

    csv = CSVParser("data/recruiter.csv").parse()[0]

    ats = JSONParser("data/ats.json").parse()

    resume = ResumeParser("data/resume.pdf").parse()

    merged = MergeEngine.merge(csv, ats, resume)

    result = ProjectionEngine.project(
        merged,
        "data/config.json"
    )

    assert isinstance(result, dict)