from System import System
from Topic import Topic
from Test import Test
from Question import Question
from Content import Content

def main():
    sys = System()

    # Register students
    sys.register_student("John Doe", 12345)
    sys.register_student("Jane Smith", 67890)

    # Create a topic
    agile = Topic(name="Agile Methodology", description="An iterative approach to software development.")
    
    # Add content to topic
    agile_content = Content(content_type="article", content_data="Waterfall methodology is a linear approach...")
    agile.add_content(agile_content)

    # Add test to topic
    q1 = Question("What is Agile?", 
                  {"a": "A car model", "b": "A bird species", "c": "A software development methodology", "d": "A type of rock"},
                  "c")
    q2 = Question("Which is NOT a principle of Agile?", 
                  {"a": "Regular customer feedback", "b": "Following a strict plan", "c": "Working software is the primary measure of progress", "d": "Welcome changing requirements"},
                  "b")
    
    agile_test = Test(agile)
    agile_test.add_question(q1)
    agile_test.add_question(q2)
    agile.set_test(agile_test)

    # Add topic to system
    sys.add_topic(agile)

    # Emulate a student learning session
    sys.start_lesson(12345, "Agile Methodology")

    sys.conduct_test(12345, "Agile Methodology")
    sys.display_student_progress(12345)

if __name__ == "__main__":
    main()
