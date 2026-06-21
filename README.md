# AI-Powered Resume Screener

An intelligent resume screening system that automates the process of ranking candidates based on job descriptions. This application uses machine learning to calculate ATS (Applicant Tracking System) scores and extract relevant skills from resumes.

## Features

- **Resume Parsing**: Automatically extract text from PDF resumes
- **Skill Extraction**: Identify and extract key skills from candidate resumes
- **ATS Scoring**: Calculate similarity scores between job descriptions and resumes using TF-IDF and cosine similarity
- **Candidate Ranking**: Rank candidates based on their ATS scores using heap-based ranking algorithm
- **Database Management**: Store candidate information and skills in MySQL database
- **Web Interface**: User-friendly Streamlit interface for easy interaction

## Technologies Used

- **Python 3.x**
- **Streamlit** - Web UI framework
- **PyPDF2** - PDF text extraction
- **scikit-learn** - Machine learning for ATS scoring
- **MySQL** - Database for candidate storage
- **Pandas** - Data manipulation
- **Heap Ranking** - Algorithm for efficient top-k candidate selection

## Installation

### Prerequisites
- Python 3.7 or higher
- MySQL Server

### Setup

1. Clone the repository:
```bash
git clone https://github.com/achalcipher/Automate-AI-Resume-Screener.git
cd Automate-AI-Resume-Screener
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your MySQL database connection in `db.py`

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter the job description in the text area

4. Upload one or multiple PDF resumes

5. Click "Analyze" to process the resumes and get ranked candidates

6. View the top-ranked candidates sorted by ATS score

## Project Structure

```
.
├── app.py                   # Main Streamlit application
├── parser.py               # Resume PDF parser
├── skill_extractor.py      # Skill extraction from resume text
├── ats_score.py            # ATS score calculation using TF-IDF
├── candidate.py            # Candidate data model
├── db.py                   # Database operations
├── heap_ranking.py         # Top-k candidate ranking algorithm
├── binary_search.py        # Binary search utility
├── requirements.txt        # Python dependencies
└── data/
    └── skills.csv          # Predefined skills database
```

## How It Works

1. **Resume Parsing**: PDFs are parsed using PyPDF2 to extract text content
2. **Skill Extraction**: Extracted text is processed to identify relevant skills
3. **ATS Scoring**: TF-IDF vectorization is applied to both job description and resume text, then cosine similarity is calculated to produce a score (0-100)
4. **Ranking**: Candidates are ranked using a heap-based algorithm to efficiently select top candidates
5. **Storage**: Candidate information and skills are persisted in the database

## Dependencies

- streamlit
- pandas
- scikit-learn
- mysql-connector-python
- PyPDF2

## Future Enhancements

- Support for more file formats (DOCX, TXT)
- Advanced NLP-based skill extraction
- Customizable scoring weights
- REST API for integration
- Export results to various formats
- Performance analytics and insights

## Author

Achal Cipher

## License

This project is open source and available under the MIT License.
