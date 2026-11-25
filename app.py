import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from resume_parser import extract_resume_text, extract_skills
from recommender import recommend_jobs

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.title("AURI.x")
st.subheader("AI Utility for Recruitment Insights")
st.caption("AI-powered resume analysis and job recommendations.")

st.sidebar.markdown("**Built by Shreyas**")

DATA_PATH = Path(__file__).parent / "data" / "jobs.csv"

@st.cache_data
def load_jobs():
    return pd.read_csv(DATA_PATH).fillna("")

jobs = load_jobs()

with st.sidebar:
    st.header("About this project")
    st.write("A student project demonstrating resume text extraction, keyword-based skill identification, NLP similarity and job recommendations.")
    st.write("**Matching method:** TF-IDF cosine similarity + skill coverage.")
    st.divider()
    st.write("Supported files: PDF, DOCX, TXT")

uploaded = st.file_uploader("Upload your resume", type=["pdf", "docx", "txt"])

if uploaded:
    try:
        resume_text = extract_resume_text(uploaded, uploaded.name)
        if not resume_text.strip():
            st.error("No readable text was found. Try a text-based PDF or DOCX file.")
            st.stop()

        skills = extract_skills(resume_text)
        recommendations = recommend_jobs(resume_text, skills, jobs)

        st.success("Resume uploaded and analyzed successfully.")
        c1, c2, c3 = st.columns(3)
        c1.metric("Words extracted", f"{len(resume_text.split()):,}")
        c2.metric("Skills identified", len(skills))
        c3.metric("Jobs compared", len(jobs))

        tab1, tab2, tab3 = st.tabs(["📊 Analysis", "💼 Job recommendations", "📝 Extracted resume text"])

        with tab1:
            st.subheader("Skills identified in your resume")
            if skills:
                st.write("  •  ".join(skills))
                skill_df = pd.DataFrame({"Skill": skills, "Detected": [1] * len(skills)})
                fig = px.bar(skill_df, x="Skill", y="Detected", title="Detected technical skills")
                fig.update_layout(showlegend=False, yaxis_title="", xaxis_title="")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No skills from the project's skill dictionary were detected. Add relevant skills or check the resume text.")

            st.info("The system identifies skills by matching terms from a predefined technical-skill dictionary. It may miss synonyms or skills not included in that dictionary.")

        with tab2:
            st.subheader("Best matching jobs")
            if recommendations.empty:
                st.warning("No job records are available.")
            else:
                for _, row in recommendations.iterrows():
                    with st.container(border=True):
                        left, right = st.columns([4, 1])
                        with left:
                            st.markdown(f"### {row['job_title']}")
                            st.write(f"**Company:** {row['company']}  |  **Location:** {row['location']}")
                            st.write(f"**Required skills:** {row['required_skills']}")
                            st.write(f"**Matching skills:** {row['matched_skills'] or 'No direct skill matches'}")
                        with right:
                            st.metric("Match score", f"{row['match_score']}%")
                            st.progress(min(int(row["match_score"]), 100))
                st.caption("Scores are algorithmic relevance estimates, not hiring probabilities or guarantees.")
        with tab3:
            st.text_area("Extracted text", resume_text, height=350)
    except Exception as e:
        st.error(f"Could not analyze this file: {e}")
        st.caption("Check the file type and try another text-based resume.")
else:
    st.info("Start by uploading a resume above. You can test the application with sample_resumes/sample_resume.txt.")
    st.subheader("How it works")
    steps = st.columns(4)
    for col, number, label in zip(steps, ["1", "2", "3", "4"], ["Upload resume", "Extract text", "Identify skills", "Recommend jobs"]):
        col.markdown(f"### {number}")
        col.write(label)

st.divider()
st.caption("Academic demonstration project • Python • Streamlit • Scikit-learn")
