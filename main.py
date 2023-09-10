from System import System
from Topic import Topic
from Test import Test
from Question import Question
from Content import Content
from TheoryManager import TheoryManager


def main():
    filename = "introduction.txt"
    sys = System()
    students = [("John Doe", 12345), ("Jane Smith", 67890)]
    for student_name, student_id in students:
        sys.register_student(student_name, student_id)
    TOPIC_SUBJECT = "Introduction au Génie Logiciel"
    agile_topics = create_agile_topics(TOPIC_SUBJECT, filename)

    # why not pass agile_topics to student session?
    for agile in agile_topics:
        sys.add_topic(agile)

    # agile topics is stored in sys object, so no need to pass it here, we retrieve it later
    student_session(sys, 12345, TOPIC_SUBJECT)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


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

    print("Extracting important points from theory... ")
    # gpt api call
    theory = manager.gpt.summarize_theory(theory)
    print(theory)
    theory_split = manager.split_theory(theory)
    print("creating 3 pargraphs for each important point...")
    # TODO: replace this static variable for something dynamic
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


def student_session(system: System, student_id, topic_name):
    system.start_lesson(student_id, topic_name)
    system.conduct_test(student_id, topic_name)
    system.display_student_progress(student_id)


if __name__ == "__main__":
    main()
