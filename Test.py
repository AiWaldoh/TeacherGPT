class Test:
    def __init__(self, topic):
        """
        Initialize a test associated with a topic.
        
        Args:
        - topic (Topic): The topic object this test is associated with.
        """
        self.topic = topic
        self.questions = []

    def add_question(self, question):
        """
        Add a multiple-choice question to the test.
        
        Args:
        - question_text (str): The text of the question.
        - choices (dict): A dictionary with keys ('a', 'b', 'c', 'd') and corresponding choice texts.
        - correct_answer (str): The correct choice key.
        """

        self.questions.append(question)

    def administer(self, student):
        """
        Administer the test to a student. 
        For now, we will display the questions and take user input for answers. 
        We'll return the number of correct answers.
        """
        correct_count = 0

        for question in self.questions:
            print(question.text)  # Changed this line
            for choice_key, choice_text in question.choices.items():
                print(f"{choice_key}. {choice_text}")
            answer = input("Your answer (a/b/c/d): ")
            if answer == question.correct_answer:  # Changed this line
                correct_count += 1

        return correct_count

    def __str__(self):
        """
        Return a string representation of the test.
        """
        return f"Test for Topic: {self.topic.name}\nNumber of Questions: {len(self.questions)}"


