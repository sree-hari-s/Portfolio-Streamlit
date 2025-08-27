from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "SREEHARI_S.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sreehari S"
PAGE_ICON = ":wave:"
NAME = "Sreehari S"
DESCRIPTION = """
Data Science enthusiast
"""
EMAIL = "sreeharis1999@gmail.com"
PHONE_NUMBER = "+91 8089776183"
LOCATION = "Trivandrum,Kerala,India"
SOCIAL_MEDIA = {
    # "Instagram": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com/sree-hari-s",
    #"Twitter": "https://twitter.com/sreehari",
}
PROJECTS = {
    "🏆 Product Recommendation System for E-commerce": "https://www.linkedin.com/feed/update/urn:li:activity:7121068898635968512/",
    "🏆 MasteringPyTrail  - Python learning resource,to guide beginners to advanced levels": "https://github.com/sree-hari-s/MasteringPyTrail",
    "🏆 Expense Tracker - Web app using Streamlit": "https://github.com/sree-hari-s/Expense-Tracker",
    "🏆 E-commerce Website - Fully Functional E-commerce website using Python Django": "https://www.linkedin.com/feed/update/urn:li:activity:7034419399939817472/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📱", PHONE_NUMBER)
    st.write("🏠", LOCATION)


# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
# st.write('\n')
# st.subheader("Experience & Qualifications")
# st.write(
#     """
# - ✔️ 7 Years experience extracting actionable insights from data
# - ✔️ Strong hands on experience and knowledge in Python and Excel
# - ✔️ Good understanding of statistical principles and their respective applications
# - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
# """
# )


# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 **Programming:** Python (Django,Pandas,Scikit-learn), SQL
- ⚙️ **Automation:** Automation Anywhere,BluePrism,Power Automate
- 📊 **Data Visualization:** Matplotlib,Seaborn,Plotly,PowerBi
- 📚 **Modeling:** Logistic regression, Linear regression, Decision trees
- 🗄️ **Databases:** MySQL,MSSQL
"""
)


# --- WORK HISTORY ---
st.write("\n")
st.subheader("Work History")
st.write("---")

# --- JOB 
st.write("🚧", "**Associate Automation Engineer | Fournxt**")
st.write("02/2024 - Present")
st.write(
    """
- ► Designing and providing Automation solutions for clients in their business processes using RPA tools like Automation Anywhere and Blueprism.
"""
)
st.write(" ")

# # --- JOB 
# st.write("🚧", "**Machine Learning Intern | Feynn Labs**")
# st.write("09/2023 - 12/2023")
# st.write(
#     """
# - ► As a SQL Developer, I designed ER diagrams, streamlined table schemas, and optimized stored procedures. I also proficiently hosted Node.js, .NET, and React applications using IIS, ensuring seamless integration between front-end and back-end systems.
# """
# )
# st.write(" ")

# --- JOB 
st.write("🚧", "**SQL DEVELOPER | TL Technologies Pvt Ltd**")
st.write("04/2023 - 06/2023")
st.write(
    """
- ► As a SQL Developer, I designed ER diagrams, streamlined table schemas, and optimized stored procedures. I also proficiently hosted Node.js, .NET, and React applications using IIS, ensuring seamless integration between front-end and back-end systems.
"""
)
st.write(" ")

# --- JOB 
st.write('\n')
st.write("🚧", "**Data Science Intern | Brototype**")
st.write("10/2022 - 03/2023")
st.write(
    """
- ► I honed my skills in this field while working on various projects that deepened my understanding 
- ► Projects underwent regular review by industrial experts providing valuable feedback for continual improvement.
"""
)

# --- Education ---
st.write("\n")
st.subheader("Education")
st.write("---")

# --- Education 1
st.write("📖", "**Electrical and Electronics Engineering | College of Engineering Trivandrum (CET)**")
st.write("08/2017 - 12/2021")
st.write(" ")

# --- Education 2
st.write("📖", "**Advanced Certification In DataScience and AI | Intellipaat**")
st.write("10/2021 - 09/2022")

# --- Projects & Accomplishments ---
st.write("\n")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
# keep alive at 2025-08-08 16:34 UTC
# keep alive at 2025-08-08 20:30 UTC
# keep alive at 2025-08-08 22:26 UTC
# keep alive at 2025-08-08 23:26 UTC
# keep alive at 2025-08-09 05:26 UTC
# keep alive at 2025-08-09 06:38 UTC
# keep alive at 2025-08-09 09:27 UTC
# keep alive at 2025-08-09 10:27 UTC
# keep alive at 2025-08-09 11:21 UTC
# keep alive at 2025-08-09 12:53 UTC
# keep alive at 2025-08-09 14:24 UTC
# keep alive at 2025-08-09 16:32 UTC
# keep alive at 2025-08-09 17:23 UTC
# keep alive at 2025-08-09 20:28 UTC
# keep alive at 2025-08-10 04:07 UTC
# keep alive at 2025-08-10 06:38 UTC
# keep alive at 2025-08-10 08:33 UTC
# keep alive at 2025-08-10 09:27 UTC
# keep alive at 2025-08-10 10:28 UTC
# keep alive at 2025-08-10 11:21 UTC
# keep alive at 2025-08-10 12:54 UTC
# keep alive at 2025-08-10 13:35 UTC
# keep alive at 2025-08-10 14:24 UTC
# keep alive at 2025-08-10 17:22 UTC
# keep alive at 2025-08-10 18:36 UTC
# keep alive at 2025-08-10 21:24 UTC
# keep alive at 2025-08-11 02:27 UTC
# keep alive at 2025-08-11 07:31 UTC
# keep alive at 2025-08-11 08:39 UTC
# keep alive at 2025-08-11 11:25 UTC
# keep alive at 2025-08-11 12:59 UTC
# keep alive at 2025-08-11 13:47 UTC
# keep alive at 2025-08-11 14:29 UTC
# keep alive at 2025-08-11 16:36 UTC
# keep alive at 2025-08-11 18:41 UTC
# keep alive at 2025-08-11 22:26 UTC
# keep alive at 2025-08-11 23:25 UTC
# keep alive at 2025-08-12 02:09 UTC
# keep alive at 2025-08-12 05:27 UTC
# keep alive at 2025-08-12 06:40 UTC
# keep alive at 2025-08-12 07:27 UTC
# keep alive at 2025-08-12 08:35 UTC
# keep alive at 2025-08-12 09:30 UTC
# keep alive at 2025-08-12 10:30 UTC
# keep alive at 2025-08-12 14:27 UTC
# keep alive at 2025-08-12 15:29 UTC
# keep alive at 2025-08-12 16:35 UTC
# keep alive at 2025-08-12 17:25 UTC
# keep alive at 2025-08-12 18:40 UTC
# keep alive at 2025-08-12 20:30 UTC
# keep alive at 2025-08-12 23:25 UTC
# keep alive at 2025-08-13 05:28 UTC
# keep alive at 2025-08-13 06:40 UTC
# keep alive at 2025-08-13 07:27 UTC
# keep alive at 2025-08-13 08:36 UTC
# keep alive at 2025-08-13 12:57 UTC
# keep alive at 2025-08-13 14:28 UTC
# keep alive at 2025-08-13 15:26 UTC
# keep alive at 2025-08-13 16:29 UTC
# keep alive at 2025-08-13 17:21 UTC
# keep alive at 2025-08-13 18:38 UTC
# keep alive at 2025-08-13 20:29 UTC
# keep alive at 2025-08-13 23:25 UTC
# keep alive at 2025-08-14 02:12 UTC
# keep alive at 2025-08-14 03:54 UTC
# keep alive at 2025-08-14 06:41 UTC
# keep alive at 2025-08-14 07:27 UTC
# keep alive at 2025-08-14 09:31 UTC
# keep alive at 2025-08-14 11:24 UTC
# keep alive at 2025-08-14 12:58 UTC
# keep alive at 2025-08-14 14:27 UTC
# keep alive at 2025-08-14 16:35 UTC
# keep alive at 2025-08-14 19:21 UTC
# keep alive at 2025-08-14 20:30 UTC
# keep alive at 2025-08-14 23:25 UTC
# keep alive at 2025-08-15 05:28 UTC
# keep alive at 2025-08-15 13:35 UTC
# keep alive at 2025-08-15 22:26 UTC
# keep alive at 2025-08-16 02:06 UTC
# keep alive at 2025-08-16 05:26 UTC
# keep alive at 2025-08-16 07:23 UTC
# keep alive at 2025-08-16 08:32 UTC
# keep alive at 2025-08-16 12:52 UTC
# keep alive at 2025-08-16 15:25 UTC
# keep alive at 2025-08-16 16:30 UTC
# keep alive at 2025-08-16 19:20 UTC
# keep alive at 2025-08-17 02:24 UTC
# keep alive at 2025-08-17 03:57 UTC
# keep alive at 2025-08-17 05:26 UTC
# keep alive at 2025-08-17 06:37 UTC
# keep alive at 2025-08-17 11:20 UTC
# keep alive at 2025-08-17 13:33 UTC
# keep alive at 2025-08-17 17:22 UTC
# keep alive at 2025-08-17 22:25 UTC
# keep alive at 2025-08-17 23:25 UTC
# keep alive at 2025-08-18 02:24 UTC
# keep alive at 2025-08-18 07:28 UTC
# keep alive at 2025-08-18 08:38 UTC
# keep alive at 2025-08-18 09:33 UTC
# keep alive at 2025-08-18 11:24 UTC
# keep alive at 2025-08-18 14:28 UTC
# keep alive at 2025-08-18 16:35 UTC
# keep alive at 2025-08-18 17:26 UTC
# keep alive at 2025-08-18 23:24 UTC
# keep alive at 2025-08-19 05:26 UTC
# keep alive at 2025-08-19 06:38 UTC
# keep alive at 2025-08-19 07:25 UTC
# keep alive at 2025-08-19 10:28 UTC
# keep alive at 2025-08-19 11:21 UTC
# keep alive at 2025-08-19 13:35 UTC
# keep alive at 2025-08-19 14:26 UTC
# keep alive at 2025-08-19 18:35 UTC
# keep alive at 2025-08-19 22:24 UTC
# keep alive at 2025-08-20 02:02 UTC
# keep alive at 2025-08-20 03:43 UTC
# keep alive at 2025-08-20 04:31 UTC
# keep alive at 2025-08-20 05:26 UTC
# keep alive at 2025-08-20 09:28 UTC
# keep alive at 2025-08-20 16:31 UTC
# keep alive at 2025-08-20 17:22 UTC
# keep alive at 2025-08-20 19:20 UTC
# keep alive at 2025-08-20 22:24 UTC
# keep alive at 2025-08-20 23:23 UTC
# keep alive at 2025-08-21 02:01 UTC
# keep alive at 2025-08-21 03:42 UTC
# keep alive at 2025-08-21 04:31 UTC
# keep alive at 2025-08-21 05:26 UTC
# keep alive at 2025-08-21 06:48 UTC
# keep alive at 2025-08-21 09:28 UTC
# keep alive at 2025-08-21 12:53 UTC
# keep alive at 2025-08-21 13:35 UTC
# keep alive at 2025-08-21 15:27 UTC
# keep alive at 2025-08-21 16:36 UTC
# keep alive at 2025-08-21 18:34 UTC
# keep alive at 2025-08-21 21:23 UTC
# keep alive at 2025-08-21 22:25 UTC
# keep alive at 2025-08-21 23:23 UTC
# keep alive at 2025-08-22 03:42 UTC
# keep alive at 2025-08-22 07:24 UTC
# keep alive at 2025-08-22 08:33 UTC
# keep alive at 2025-08-22 09:27 UTC
# keep alive at 2025-08-22 10:27 UTC
# keep alive at 2025-08-22 11:20 UTC
# keep alive at 2025-08-22 12:52 UTC
# keep alive at 2025-08-22 15:26 UTC
# keep alive at 2025-08-22 16:31 UTC
# keep alive at 2025-08-22 18:35 UTC
# keep alive at 2025-08-22 19:20 UTC
# keep alive at 2025-08-22 23:23 UTC
# keep alive at 2025-08-23 01:58 UTC
# keep alive at 2025-08-23 04:29 UTC
# keep alive at 2025-08-23 06:34 UTC
# keep alive at 2025-08-23 07:22 UTC
# keep alive at 2025-08-23 08:30 UTC
# keep alive at 2025-08-23 10:25 UTC
# keep alive at 2025-08-23 12:49 UTC
# keep alive at 2025-08-23 16:28 UTC
# keep alive at 2025-08-23 18:32 UTC
# keep alive at 2025-08-23 19:18 UTC
# keep alive at 2025-08-23 21:21 UTC
# keep alive at 2025-08-23 22:23 UTC
# keep alive at 2025-08-23 23:23 UTC
# keep alive at 2025-08-24 02:19 UTC
# keep alive at 2025-08-24 03:51 UTC
# keep alive at 2025-08-24 04:32 UTC
# keep alive at 2025-08-24 07:23 UTC
# keep alive at 2025-08-24 08:30 UTC
# keep alive at 2025-08-24 10:25 UTC
# keep alive at 2025-08-24 12:49 UTC
# keep alive at 2025-08-24 14:22 UTC
# keep alive at 2025-08-24 15:23 UTC
# keep alive at 2025-08-24 17:21 UTC
# keep alive at 2025-08-24 19:19 UTC
# keep alive at 2025-08-24 22:24 UTC
# keep alive at 2025-08-24 23:23 UTC
# keep alive at 2025-08-25 02:07 UTC
# keep alive at 2025-08-25 03:50 UTC
# keep alive at 2025-08-25 04:33 UTC
# keep alive at 2025-08-25 06:40 UTC
# keep alive at 2025-08-25 07:25 UTC
# keep alive at 2025-08-25 08:36 UTC
# keep alive at 2025-08-25 09:29 UTC
# keep alive at 2025-08-25 11:22 UTC
# keep alive at 2025-08-25 12:55 UTC
# keep alive at 2025-08-25 13:36 UTC
# keep alive at 2025-08-25 14:27 UTC
# keep alive at 2025-08-25 16:32 UTC
# keep alive at 2025-08-25 17:21 UTC
# keep alive at 2025-08-25 21:23 UTC
# keep alive at 2025-08-26 02:03 UTC
# keep alive at 2025-08-26 03:43 UTC
# keep alive at 2025-08-26 05:26 UTC
# keep alive at 2025-08-26 09:28 UTC
# keep alive at 2025-08-26 10:28 UTC
# keep alive at 2025-08-26 12:56 UTC
# keep alive at 2025-08-26 13:38 UTC
# keep alive at 2025-08-26 14:25 UTC
# keep alive at 2025-08-26 16:31 UTC
# keep alive at 2025-08-26 18:35 UTC
# keep alive at 2025-08-26 19:19 UTC
# keep alive at 2025-08-26 20:27 UTC
# keep alive at 2025-08-27 01:59 UTC
