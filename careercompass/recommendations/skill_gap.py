def analyze_skill_gap(user_skills, career_tools):

    user_skills = user_skills.lower().split(",")

    required_skills = career_tools.lower().replace("/", ",").split(",")

    user_set = set(s.strip() for s in user_skills)
    required_set = set(s.strip() for s in required_skills)

    missing_skills = required_set - user_set

    return {
        "known": list(user_set),
        "missing": list(missing_skills)
    }