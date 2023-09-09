class Question:
    def __init__(self, question_text, choices, correct_answer):
        """
        Initialize a multiple-choice question.
        
        Args:
        - question_text (str): The text of the question.
        - choices (dict): A dictionary with keys ('a', 'b', 'c', 'd') and corresponding choice texts.
        - correct_answer (str): The correct choice key.
        """
        self.text = question_text
        self.choices = choices
        self.correct_answer = correct_answer

    def display(self):
        """Display the question and choices."""
        print(self.text)
        for choice, choice_text in self.choices.items():
            print(f"{choice}. {choice_text}")

    def check_answer(self, student_answer):
        """Check if the provided answer is correct."""
        return student_answer == self.correct_answer
    
    def administer(self):
        """ Pose the question and return True if the user's answer is correct, otherwise return False. """
        print(self.text)
        for choice_key, choice_text in self.choices.items():
            print(f"{choice_key}. {choice_text}")
        answer = input("Your answer (a/b/c/d): ")
        return answer == self.correct_answer
    
    def __str__(self):
        """Return a string representation of the question."""
        return f"Question: {self.text}\nChoices: {self.choices}\nCorrect Answer: {self.correct_answer}"



