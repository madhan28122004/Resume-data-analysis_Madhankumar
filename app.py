import streamlit as st
import re

st.set_page_config(page_title="Resume Data Analyzer", page_icon="📄")

st.title("📄 Resume Data Analyzer")
st.write("Enter your skills and discover suitable job roles.")

roles = {
    "Full Stack Developer": {"html", "css", "javascript", "react", "nodejs", "mongodb", "sql"},

    "Front End Developer": {
        "html", "css", "javascript",
        "react", "responsive", "flexbox",
        "grid", "dom", "api", "git"
    },

    "Data Scientist": {
        "python", "pandas", "numpy",
        "machine_learning", "statistics",
        "data_visualization"
    },

    "Cloud Engineer": {
        "aws", "azure", "docker",
        "kubernetes", "linux", "networking"
    },

    "UI/UX Designer": {
        "figma", "adobe_xd",
        "wireframing", "prototyping",
        "user_research"
    },

    "AI Engineer": {
        "python", "deep_learning",
        "tensorflow", "pytorch",
        "nlp", "computer_vision"
    },

    "Java Developer": {
        "java", "spring",
        "hibernate", "jdbc", "sql"
    },

    "Backend Developer": {
        "java", "python",
        "nodejs", "api",
        "database", "sql"
    }
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
    "Enter your skills",
    placeholder="python pandas numpy machine_learning statistics"
)

if st.button("Analyze Resume"):

    if not skills.strip():
        st.warning("Please enter your skills.")
    else:
        results = analyze_skills(skills)

        if not results:
            st.error("❌ No matching roles found.")
        else:
            st.success("✅ Matching Roles Found")

            for role, percent, matched, missing in results:

                st.subheader(role)

                st.progress(int(percent))

                st.write(f"**Match Percentage:** {percent:.2f}%")
                st.write("**Matched Skills:**", ", ".join(sorted(matched)))

                if percent < 50:
                    st.warning("You need to learn more skills.")
                    st.write("**Missing Skills:**", ", ".join(sorted(missing)))

                elif percent < 90:
                    st.info("Good for applying jobs.")
                    st.write("**Missing Skills:**", ", ".join(sorted(missing)))

                    search_query = role.replace(" ", "+")
                    st.markdown(
                        f"🔗 [Find Jobs on LinkedIn](https://www.linkedin.com/jobs/search/?keywords={search_query})"
                    )

                else:
                    st.success("🔥 Excellent for applying jobs!")

                    if missing:
                        st.write("**Missing Skills:**", ", ".join(sorted(missing)))
                    else:
                        st.write("**Missing Skills:** None")

                    search_query = role.replace(" ", "+")
                    st.markdown(
                        f"🔗 [Find Jobs on LinkedIn](https://www.linkedin.com/jobs/search/?keywords={search_query})"
                    )

st.markdown("---")
st.caption("Developed by Madhankumar M")
