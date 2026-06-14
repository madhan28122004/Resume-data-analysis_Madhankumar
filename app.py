import streamlit as st
import re

st.title("📄 Resume Data Analyzer")

roles = {
    "Full Stack Developer": {"html", "css", "javascript", "react", "nodejs", "mongodb", "sql"},
    "Front End Developer": {"html", "css", "javascript", "react", "responsive", "flexbox", "grid", "dom", "api", "git"},
    "Data Scientist": {"python", "pandas", "numpy", "machine_learning", "statistics", "data_visualization"},
    "Cloud Engineer": {"aws", "azure", "docker", "kubernetes", "linux", "networking"},
    "UI/UX Designer": {"figma", "adobe_xd", "wireframing", "prototyping", "user_research"},
    "AI Engineer": {"python", "deep_learning", "tensorflow", "pytorch", "nlp", "computer_vision"},
    "Java Developer": {"java", "spring", "hibernate", "jdbc", "sql"},
    "Backend Developer": {"java", "python", "nodejs", "api", "database", "sql"}
}

def analyze_skills(user_input):
    user_skills = set(re.split(r"[,\s]+", user_input.lower().strip()))
    results = []

    for role, required in roles.items():
        matched = user_skills.intersection(required)

        if matched:
            missing = required - user_skills
            percent = (len(matched) / len(required)) * 100
            results.append((role, percent, matched, missing))

    return sorted(results, key=lambda x: x[1], reverse=True)

skills = st.text_input(
    "Enter Skills",
    placeholder="python pandas numpy statistics"
)

if st.button("Analyze Resume"):

    results = analyze_skills(skills)

    if not results:
        st.error("No matching roles found.")
    else:
        for role, percent, matched, missing in results:

            st.subheader(role)
            st.write(f"Match: {percent:.2f}%")
            st.write("Matched Skills:", ", ".join(matched))

            if percent < 50:
                st.warning("Need more skills.")
                st.write("Missing Skills:", ", ".join(missing))

            elif percent < 90:
                st.info("Good for applying jobs.")
                st.write("Missing Skills:", ", ".join(missing))

            else:
                st.success("Excellent for applying jobs!")
                st.write("Missing Skills:", "None" if not missing else ", ".join(missing))
