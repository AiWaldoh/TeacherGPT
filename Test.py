class Test:
    def __init__(self, topic):
        """
        Initialize a test associated with a topic.
        """
        self.topic = topic
        self.questions = []

    def add_question(self, question):
        """
        Add a multiple-choice question to the test.
        """

        self.questions.append(question)

    def administer(self, student):
        """
        Administer the test to a student. 
        """
        correct_count = 0

        for question in self.questions:
            print(question.text) 
            for choice_key, choice_text in question.choices.items():
                print(f"{choice_key}. {choice_text}")
            answer = input("Your answer (a/b/c/d): ")
            if answer == question.correct_answer:
                correct_count += 1

        return correct_count

    def __str__(self):
        """
        Return a string representation of the test.
        """
        return f"Test for Topic: {self.topic.name}\nNumber of Questions: {len(self.questions)}"


