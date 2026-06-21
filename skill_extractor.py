import pandas as pd
import os

class SkillExtractor:
    def __init__(self):
        csv_path = os.path.join(os.path.dirname(__file__), "skills.csv")
        if os.path.exists(csv_path):
            self.skills = pd.read_csv(csv_path)["Skills"].tolist()
        else:
            self.skills = ["Python", "Java", "SQL", "JavaScript", "C++", "Data Science", "Machine Learning"]
    
    def extract_skills(self, text):
        found = []
        for skill in self.skills:
            if skill.lower() in text.lower():
                found.append(skill)
        return found