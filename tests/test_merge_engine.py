from app.parsers.csv_parser import CSVParser
from app.parsers.json_parser import JSONParser
from app.parsers.resume_parser import ResumeParser
from app.merger.merge_engine import MergeEngine


def test_merge():

    csv = CSVParser("data/recruiter.csv").parse()[0]

    ats = JSONParser("data/ats.json").parse()

    resume = ResumeParser("data/resume.pdf").parse()

    merged = MergeEngine.merge(csv, ats, resume)

    assert merged.company == "Google"

    assert merged.email == "john.smith@gmail.com"

    assert "Python" in merged.skills