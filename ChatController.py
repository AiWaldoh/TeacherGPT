from Chatbot import Chatbot
import streamlit as st
from System import System


@st.cache_resource(show_spinner=False)
def get_chatbot(prompt):
    return Chatbot(prompt)


class ChatController:
    def __init__(self):
        self.system_prompt = (
            "This is the chatbot for course SYST1046. The goal is to provide information "
            "and support to students. Let's engage in some small talk first!"
        )
        self.state = "small_talk"
        self.system = System()
        self.student_id = "12345"  # À adapter en fonction de votre implémentation
        self.topic_name = "Agile Méthodologie"  # À adapter
        self.chatbot = get_chatbot(self.system_prompt)
        self.register_student("John Doe", self.student_id)

    def register_student(self, student_name, student_id):
        # this is plural. figure out student registration later
        # also figure out testing and progress saving and note keeping, and ... so... much ... more
        students = [("John Doe", 12345), ("Jane Smith", 67890)]
        for student_name, student_id in students:
            self.system.register_student(student_name, student_id)

    def process_message(self, message):
        if self.state == "small_talk":
            response = self.chatbot.small_talk(message)

            if "Commençons le cours" in response:
                print("Switching phase")
                self.state = "apprentissage"
                # Ici, nous initialisons la leçon et récupérons la réponse pour démarrer le cours
                response = self.start_new_lesson(self.student_id, self.topic_name)

            return response

        elif self.state == "apprentissage":
            print("Apprentissage")
            response = self.handle_apprentissage(message)

            if "Fin de l'apprentissage." in response:
                self.state = "test"

            return response

        elif self.state == "test":
            return self.chatbot.test(message)

    def start_new_lesson(self, student_id, topic_name):
        # Nous commençons la leçon et récupérons les paragraphes/interactions pour les afficher.
        interactions = self.system.start_lesson(student_id, topic_name)
        return "\n\n".join(interactions)

    def handle_apprentissage(self, message):
        # Ici, vous pouvez adapter la manière dont le message est traité pendant l'état d'apprentissage.
        # Pour l'instant, cela renvoie simplement le message, mais cela peut être modifié selon votre besoin.
        return message

    def check_password(self):
        """Returns `True` if the user had the correct password."""

        def password_entered():
            """Checks whether a password entered by the user is correct."""
            if st.session_state["password"] == st.secrets["password"]:
                st.session_state["password_correct"] = True
                del st.session_state[
                    "password"
                ]  # Don't store password in session_state
            else:
                st.session_state["password_correct"] = False

        # Check if "password_correct" is in the session state
        if "password_correct" not in st.session_state:
            # If not present, it's the first run. Show the input field for the password.
            st.text_input(
                "Mot de passe",
                type="password",
                on_change=password_entered,
                key="password",
            )
            return False
        elif not st.session_state["password_correct"]:
            # If password is incorrect, show the input field again + error message.
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            st.error("😕 Mot de passe incorrect")
            return False
        else:
            # Password is correct. Do not display the password input field.
            return True
