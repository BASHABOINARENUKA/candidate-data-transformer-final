# Candidate Data Transformer

## Overview

Candidate Data Transformer is a backend data processing pipeline that consolidates candidate information from multiple heterogeneous sources into a single canonical candidate profile.

The system ingests structured and unstructured data, normalizes it, detects duplicate candidates, merges records, tracks data provenance, assigns confidence scores, validates the final profile, and generates configurable output using a runtime configuration file.

---

# Features

- Parse Recruiter CSV
- Parse ATS JSON
- Parse Resume PDF
- Normalize emails, phone numbers, company names, and skills
- Detect duplicate candidates using entity resolution
- Merge candidate information from multiple sources
- Generate provenance for every field
- Generate confidence scores
- Runtime configurable output using `config.json`
- Validate final output

---

# Architecture

```
Recruiter CSV
        │
ATS JSON
        │
Resume PDF
        │
        ▼
     Parsers
        ▼
 Candidate Model
        ▼
 Normalization
        ▼
 Entity Resolution
        ▼
 Merge Engine
        ▼
 Provenance
        ▼
 Confidence
        ▼
 Projection Engine
        ▼
 Validator
        ▼
 Final JSON Output
```

---

# Folder Structure

```
candidate-transformer/

app/
│
├── confidence/
├── matcher/
├── merger/
├── models/
├── normalizers/
├── parsers/
├── projection/
├── provenance/
└── validator/

data/

tests/

main.py

requirements.txt

README.md
```

---

# Tech Stack

- Python 3
- Pandas
- pdfplumber
- Pydantic
- RapidFuzz
- phonenumbers

---

# Input Sources

### Structured Sources

- recruiter.csv
- ats.json

### Unstructured Source

- resume.pdf

---

# Merge Strategy

The merge engine combines candidate records using source priority.

Priority:

```
ATS JSON
↓

Recruiter CSV
↓

Resume PDF
```

Rules:

- Email → ATS > CSV > Resume
- Phone → CSV > ATS > Resume
- Company → ATS > CSV
- Skills → Union of all sources
- Education → Resume
- Experience → ATS

---

# Normalization

The system normalizes:

- Email
- Phone Number
- Company Name
- Candidate Name
- Skills

Example:

```
JOHN@GMAIL.COM

↓

john@gmail.com
```

```
9876543210

↓

+919876543210
```

---

# Edge Cases Handled

- Missing phone number
- Missing company
- Duplicate skills
- Different phone formats
- Different email casing
- Similar candidate names
- Duplicate candidate records
- Invalid email
- Invalid phone number
- Missing required fields
- Invalid JSON
- Missing PDF

---

# Assumptions

- ATS data has the highest priority.
- Resume contains the most complete education and skills information.
- Email is the strongest identifier for duplicate detection.
- Phone number is used as a secondary identifier.
- Confidence and provenance are currently rule-based.

---

# Future Improvements

- Dynamic confidence calculation
- Dynamic provenance generation
- LinkedIn integration
- GitHub integration
- OCR support for scanned resumes
- Database support
- REST API deployment

---

# How to Run

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

# Sample Output

```json
{
    "full_name":"John A. Smith",
    "email":"john.smith@gmail.com",
    "company":"Google",
    "skills":[
        "Python",
        "SQL",
        "FastAPI",
        "Machine Learning"
    ]
}
```

---

# Author

Renuka Bashaboina

B.Tech Artificial Intelligence and Machine Learning