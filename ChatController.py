from Chatbot import Chatbot
import streamlit as st
from System import System
from Topic import Topic
from Content import Content
from Test import Test
from Question import Question
from TheoryManager import TheoryManager
import random
from GPTQuery import GPTQuery
from learning_styles_fr import learning_styles_json_french

# Initializing session state variables
if "state" not in st.session_state:
    st.session_state.state = "small_talk"
if "current_paragraph_index" not in st.session_state:
    st.session_state.current_paragraph_index = 0
if "teachings" not in st.session_state:
    st.session_state.teachings = []


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


@st.cache_resource(show_spinner=True)
def get_chatbot(prompt):
    return Chatbot(prompt)


@st.cache_resource(show_spinner=True)
def get_system(student_name, student_id):
    filename = "introduction.txt"
    TOPIC_SUBJECT = "Introduction au Génie Logiciel"
    system = System()
    system.register_student(student_name, student_id)
    agile_topics = create_agile_topics(TOPIC_SUBJECT, filename)
    for agile in agile_topics:
        system.add_topic(agile)
    return system


def create_agile_questions(content) -> Test:
    """Generate a set of questions for the given agile content."""
    q1 = Question(
        "What is Agile?",
        {
            "a": "A car model",
            "b": "A bird species",
            "c": "A software development methodology",
            "d": "A type of rock",
        },
        "c",
    )
    q2 = Question(
        "Which is NOT a principle of Agile?",
        {
            "a": "Regular customer feedback",
            "b": "Following a strict plan",
            "c": "Working software is the primary measure of progress",
            "d": "Welcome changing requirements",
        },
        "b",
    )

    agile_test = Test(content)
    agile_test.add_question(q1)
    agile_test.add_question(q2)

    return agile_test


def create_agile_topics(TOPIC_SUBJECT, filename="introduction.txt"):
    manager = TheoryManager()
    theory = manager.get_theory(filename)

    theory = manager.gpt.summarize_theory(theory)
    print(theory)
    theory_split = manager.split_theory(theory)
    print("creating 3 pargraphs for each important point...")
    enhanced_theory = manager.enhance_theory(theory_split, TOPIC_SUBJECT)

    agile_topics = []
    for chunk in chunks(list(enhanced_theory.items()), 3):
        agile_topic = Topic(
            name=TOPIC_SUBJECT,
            description="An iterative approach to software development.",
        )

        for original_theory, enhanced_content in chunk:
            agile_content = Content(
                content_type="article", content_data=enhanced_content
            )
            agile_topic.add_content(agile_content)

        agile_test = create_agile_questions(agile_content)

        agile_topic.set_test(agile_test)
        agile_topics.append(agile_topic)
    return agile_topics


class ChatController:
    def __init__(self):
        self.system_prompt = (
            "This is the chatbot for course SYST1046. The goal is to provide information "
            "and support to students. Let's engage in some small talk first!"
        )
        st.session_state.state = "small_talk"

        self.student_id = "12345"  # À adapter en fonction de votre implémentation
        self.topic_name = "Introduction au Génie Logiciel"  # À adapter
        self.chatbot = get_chatbot(self.system_prompt)
        self.system = get_system("John Doe", self.student_id)

    def start_lesson(self, student_id, topic_name):
        """Start a lesson for a student on a particular topic."""
        interactions = []
        student = self.system.find_student_by_id(student_id)
        topic = self.system.find_topic_by_name(topic_name)
        if student and topic:
            enhanced_theory_list = []
            for content in topic.contents:
                enhanced_theory_list.extend(content.content_data.split("\n\n"))
            filtered_paragraphs = [p for p in enhanced_theory_list if p.strip()]
            interactions.extend(self.interactive_session(topic, filtered_paragraphs))
            interactions.append(topic.display_content())
        else:
            interactions.append("Student or Topic not found!")
        return interactions

    def interactive_session(self, topic, paragraphs):
        interactions = []
        JOKE_INTERVAL = 5
        MAX_HISTORY = 2
        history = []
        for index, paragraph in enumerate(paragraphs):
            interactions.append(paragraph)
            history.append(paragraph)
            if len(history) > MAX_HISTORY:
                history.pop(0)
            if (index + 1) % JOKE_INTERVAL == 0:
                joke_query = GPTQuery()
                joke_content = " ".join(history)
                joke_types = ["knock knock", "dad joke", "walks into a bar"]
                selected_joke_type = random.choice(joke_types)
                joke = joke_query.get_joke(joke_content, joke_type=selected_joke_type)
                interactions.append(f"\nEn passant... {joke}\n")
        return interactions

    def process_message(self, message):
        print("Processing message...")
        if st.session_state.state == "small_talk":
            response = self.chatbot.small_talk(message)
            # Transition logic based on user's intent to start the lesson
            if "Commençons le cours" in response:
                print("setting state to apprentissage")
                st.session_state.state = "apprentissage"
                response = self.start_new_lesson(self.student_id, self.topic_name)
            return response

        elif st.session_state.state == "apprentissage":
            response = self.handle_apprentissage(message)
            if "Fin de l'apprentissage." in response:
                st.session_state.state = "test"
                return "Entering test phase. incomplete"
            else:
                return (
                    response
                    + "\n\nAvez vous des questions ou voulez vous des clarifications? (Typer 'non' pour continuer): "
                )

        elif st.session_state.state == "test":
            return self.chatbot.test(message)

    def start_new_lesson(self, student_id, topic_name):
        st.session_state.teachings = self.start_lesson(student_id, topic_name)
        st.session_state.current_paragraph_index = 0
        return (
            st.session_state.teachings[0]
            + "\n\nAvez vous des questions ou voulez vous des clarifications? (Typer 'non' pour continuer): "
            if st.session_state.teachings
            else "No teachings available."
        )

    def handle_apprentissage(self, message):
        # If the student's response is 'non', move to the next paragraph or end if all are covered
        if message.lower() == "non":
            st.session_state.current_paragraph_index += 1
            if (
                st.session_state.current_paragraph_index
                >= len(st.session_state.teachings)
                or st.session_state.teachings[st.session_state.current_paragraph_index]
                is None
            ):
                return "Fin de l'apprentissage."
            else:
                return st.session_state.teachings[
                    st.session_state.current_paragraph_index
                ]
        # If the student has a question, use GPT to get a response
        else:
            paragraph = st.session_state.teachings[
                st.session_state.current_paragraph_index
            ]  # Current paragraph
            random_style = random.choice(learning_styles_json_french["styles"])
            gpt = GPTQuery()
            response = gpt.ask_question(message, paragraph, random_style)
            return response

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
