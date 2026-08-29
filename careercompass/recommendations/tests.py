from django.test import TestCase
from recommendations.ml_engine import recommend_career
from recommendations.project_engine import recommend_projects
from recommendations.skill_gap import analyze_skill_gap

class RecommendationsTests(TestCase):
    def test_recommend_career(self):
        # Test recommending career based on skills and interests
        results = recommend_career("Python Machine Learning", "AI Research")
        self.assertTrue(len(results) > 0)
        first = results[0]
        self.assertIn("job_opportunity", first)
        self.assertIn("focus_area", first)
        self.assertIn("tools", first)

    def test_recommend_projects(self):
        # Test recommending projects based on keywords
        results = recommend_projects("Python, Machine Learning, Web")
        self.assertTrue(len(results) > 0)
        first = results[0]
        self.assertIn("title", first)
        self.assertIn("owner", first)
        self.assertIn("language", first)

    def test_analyze_skill_gap(self):
        # Test skill gap analysis
        user_skills = "Python, SQL, Django"
        career_tools = "Python, Django, React, Docker"
        gap = analyze_skill_gap(user_skills, career_tools)
        
        self.assertIn("python", gap["known"])
        self.assertIn("django", gap["known"])
        self.assertIn("react", gap["missing"])
        self.assertIn("docker", gap["missing"])
