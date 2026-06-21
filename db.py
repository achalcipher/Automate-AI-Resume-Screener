import mysql.connector
import streamlit as st

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Achal1234",
                database="ats_resume_db",
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            st.error(f"Database connection error: {err}")
            self.connection = None
            self.cursor = None
    
    def save_candidate(self, candidate):
        if not self.connection:
            return None
        query = """
        INSERT INTO candidates (name, email, score)
        VALUES (%s, %s, %s)
        """
        try:
            self.cursor.execute(query, (candidate.name, candidate.email, candidate.score))
            self.connection.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            st.error(f"Error saving candidate: {err}")
            return None
    
    def save_skills(self, candidate_id, skills):
        if not self.connection or not candidate_id:
            return
        try:
            for skill in skills:
                self.cursor.execute(
                    """
                    INSERT INTO candidate_skills (candidate_id, skill_name) VALUES (%s, %s)
                    """,
                    (candidate_id, skill)
                )
            self.connection.commit()
        except mysql.connector.Error as err:
            st.error(f"Error saving skills: {err}")  