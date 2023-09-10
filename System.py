from Student import Student
from GPTQuery import GPTQuery
from Topic import Topic
import random
from learning_styles_fr import learning_styles_json_french


class System:
    def __init__(self):
        self.students = {}
        self.topics = []
        self.gpt_query = GPTQuery()

    def add_student(self, student):
        if student.id not in self.students:
            self.students[student.id] = student
        else:
            print(f"Student with ID {student.id} already exists!")

    def add_topic(self, topic):
        # print(f"Adding topic {topic}...")
        if topic not in self.topics:
            self.topics.append(topic)
        else:
            print(f"Topic {topic.name} already added!")

    def find_topic_by_name(self, topic_name):
        # print(f"Finding topic {topic_name}...")
        for topic in self.topics:
            if topic.name == topic_name:
                return topic
        return None

    def find_student_by_id(self, student_id):
        return self.students.get(student_id, None)

    # def generate_theory(self, topic, name):
    #     # Get 3 paragraphs using GPTQuery.
    #     paragraphs = self.gpt_query.query_gpt(topic, name)
    #     return paragraphs.split("\n")  # Assuming paragraphs are separated by newline.

    def interactive_session(self, topic, paragraphs):
        # For each paragraph, present it and allow for Q&A.
        for index, paragraph in enumerate(paragraphs):
            print(paragraph)
            while True:
                student_input = (
                    input(
                        "\n\nAvez vous des questions ou voulez vous des clarifications? (Typer 'non' pour continuer): "
                    )
                    .strip()
                    .lower()
                )

                if student_input in ["non"]:
                    break
                random_style = random.choice(learning_styles_json_french["styles"])
                response = self.gpt_query.ask_question(
                    student_input, paragraph, random_style
                )
                print(response)
            print("Continuons!\n")

    def start_lesson(self, student_id, topic_name):
        """Start a lesson for a student on a particular topic."""
        student = self.find_student_by_id(student_id)
        topic: Topic = self.find_topic_by_name(topic_name)

        if student and topic:
            enhanced_theory_list = []
            for content in topic.contents:
                enhanced_theory_list.extend(content.content_data.split("\n\n"))
            filtered_paragraphs = [p for p in enhanced_theory_list if p.strip()]

            self.interactive_session(topic, filtered_paragraphs)

            topic.display_content()

        else:
            print("Student or Topic not found!")

    def conduct_test(self, student_id, topic_name):
        """Conduct a test for a specific topic for a student."""
        student = self.find_student_by_id(student_id)
        topic = self.find_topic_by_name(topic_name)

        if student and topic:
            score = topic.administer_test(student)
            student.add_score(topic, score)
            return score
        else:
            print("Student or Topic not found!")
            return None

    def register_student(self, student_name, student_id):
        """Register (or add) a student to the system."""
        if student_id not in self.students:
            new_student = Student(student_name, student_id)
            self.students[student_id] = new_student
        else:
            print(f"Student with ID {student_id} already exists!")

    def display_student_progress(self, student_id):
        """Display the progress of a student."""
        student = self.find_student_by_id(student_id)
        if student:
            student.display_progress()
        else:
            print(f"Student with ID {student_id} not found!")
        return None
