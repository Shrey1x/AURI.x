AI RESUME ANALYZER & JOB RECOMMENDATION SYSTEM
================================================

READ THIS FIRST. You do not need to know coding to run the project.

WHAT IS INCLUDED
- app.py: the application screen
- resume_parser.py: reads resume text and identifies skills
- recommender.py: ranks jobs using NLP similarity and skill coverage
- data/jobs.csv: sample job dataset
- sample_resumes/sample_resume.txt: sample resume for testing
- requirements.txt: software packages needed
- Project_Report.docx: editable project report
- Project_Presentation.pptx: editable viva presentation

RUN ON WINDOWS (VS CODE)

STEP 1 — Install Python
1. Open https://www.python.org/downloads/
2. Download Python 3.11 or newer.
3. During installation, tick "Add Python to PATH".
4. Finish installation.

STEP 2 — Open the project folder
1. Extract this ZIP file.
2. Open VS Code.
3. Click File > Open Folder.
4. Select the extracted AI_Resume_Analyzer_Job_Recommender folder.

STEP 3 — Open the terminal
In VS Code, click Terminal > New Terminal.

STEP 4 — Create a private Python environment
Copy and run this command:
    py -m venv .venv

STEP 5 — Activate it
Copy and run:
    .venv\Scripts\activate

If Windows blocks activation, run this once in the same terminal:
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Then run the activate command again.

STEP 6 — Install the required packages
Copy and run:
    python -m pip install --upgrade pip
Then:
    pip install -r requirements.txt

STEP 7 — Start the application
Copy and run:
    streamlit run app.py

A browser tab should open automatically. If not, copy the Local URL shown in the terminal (usually http://localhost:8501) into Chrome.

HOW TO TEST
1. In the app, upload sample_resumes/sample_resume.txt.
2. Check the skills identified.
3. Open Job recommendations.
4. Confirm that ranked jobs and match scores appear.
5. Try your own PDF resume. Text-based PDFs work best.

IF SOMETHING GOES WRONG
- "py is not recognized": reinstall Python and tick Add Python to PATH; restart VS Code.
- "streamlit is not recognized": activate .venv and run pip install -r requirements.txt again; then use python -m streamlit run app.py.
- PDF gives no text: it may be a scanned image. Use a text-based PDF or DOCX.
- Browser does not open: use the localhost URL printed in the terminal.
- Port is busy: run python -m streamlit run app.py --server.port 8502

IMPORTANT FOR SUBMISSION
- Replace sample data with your own test data where appropriate.
- Run the application and take screenshots of actual outputs.
- Edit the report cover page with your name, roll number, department, college, guide and academic year.
- Follow your department's required report format if one was provided.
- Understand the algorithm and limitations before viva.
- Do not claim that this system uses a trained deep-learning model. It uses TF-IDF and cosine similarity, which are NLP / information-retrieval techniques.
- Match score is a relevance score, not a probability of getting hired.
