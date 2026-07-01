from app.parsers.csv_parser import CSVParser


def test_csv_parser():

    parser = CSVParser("data/recruiter.csv")

    candidates = parser.parse()

    assert len(candidates) > 0

    assert candidates[0].email == "john.smith@gmail.com"