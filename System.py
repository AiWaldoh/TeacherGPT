from Student import Student
from Topic import Topic
class System:
    def __init__(self):
        self.students = {}  # Use a dictionary to store students by ID for efficient lookups
        self.topics = []

    def add_student(self, student):
        """Add a student to the system."""
        if student.id not in self.students:
            self.students[student.id] = student
        else:
            print(f"Student with ID {student.id} already exists!")

    def add_topic(self, topic):
        """Add a topic to the system."""
        if topic not in self.topics:
            self.topics.append(topic)
        else:
            print(f"Topic {topic.name} already added!")

    def find_topic_by_name(self, topic_name):
        """Return the topic object with the specified name."""
        for topic in self.topics:
            if topic.name == topic_name:
                return topic
        return None

    def find_student_by_id(self, student_id):
        """Return the student object with the specified ID."""
        return self.students.get(student_id, None)

    def start_lesson(self, student_id, topic_name):
        """Start a lesson for a student on a particular topic."""
        student = self.find_student_by_id(student_id)
        topic = self.find_topic_by_name(topic_name)

        if student and topic:
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
