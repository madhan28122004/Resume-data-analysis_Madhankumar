import re

roles = {
    "Full Stack Developer": {"html","css","javascript","react","nodejs","mongodb","sql"},
    
    "Front End Developer": {
        "html","css","javascript",
        "react","responsive","flexbox",
        "grid","dom","api","git"
    },
    
    "Data Scientist": {"python","pandas","numpy","machine_learning","statistics","data_visualization"},
    
    "Cloud Engineer": {"aws","azure","docker","kubernetes","linux","networking"},
    
    "UI/UX Designer": {"figma","adobe xd","wireframing","prototyping","user research"},
    
    "AI Engineer": {"python","deep learning","tensorflow","pytorch","nlp","computer vision"},
    
    "Java Developer": {"java","spring","hibernate","jdbc","sql"},
    
    "Backend Developer": {"java","python","nodejs","api","database","sql"}
}

# ==========================================
# ANALYZE SKILLS
# ==========================================

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

# ==========================================
# SHOW RESULTS
# ==========================================

def show_results(results):
    if not results:
        print("\n❌ No matching roles found.")
        return

    print("\n=== MATCHING ROLES ===")

    for role, percent, matched, missing in results:
        print(f"\nRole: {role}")
        print(f"Match: {percent:.2f}%")
        print("Matched Skills:", ", ".join(matched))

        # 🔻 BELOW 50%
        if percent < 50:
            print("👉 You need to learn some or more skills.")
            print("Missing Skills:", ", ".join(missing))

        # 🔸 50% to 89%
        elif percent < 90:
            print("👍 Good for applying jobs.")
            print("Missing Skills:", ", ".join(missing))
            search_query = role.replace(" ", "+")
            print(f"Find Jobs: https://www.linkedin.com/jobs/search/?keywords={search_query}")

        # 🔥 90% and above
        else:
            print("🔥 Excellent for applying jobs!")
            print("Missing Skills:", "None" if not missing else ", ".join(missing))
            search_query = role.replace(" ", "+")
            print(f"Find Jobs: https://www.linkedin.com/jobs/search/?keywords={search_query}")

# ==========================================
# MAIN PROGRAM
# ==========================================

print("=== SMART CAREER ANALYZER ===")

while True:
    user_input = input("\nEnter your skills (comma or space-separated) or 'exit': ")

    if user_input.lower() == "exit":
        print("Exiting...")
        break

    results = analyze_skills(user_input)
    show_results(results)
