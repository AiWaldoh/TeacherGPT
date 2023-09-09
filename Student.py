class Student:
    def __init__(self, name, student_id):
        """
        Initialize a student with a name and student ID.
        """
        self.name = name
        self.student_id = student_id
        self.completed_topics = {}  
        self.progress = {} 
        self.scores = {}  
    
    def record_test_score(self, topic_name, score):
        """Record a test score for a given topic."""
        self.completed_topics[topic_name] = score

    def has_passed(self, topic_name, passing_score=3):
        """Check if the student has passed a given topic based on a specified passing score."""
        return self.completed_topics.get(topic_name, 0) >= passing_score

    def get_test_score(self, topic_name):
        """Retrieve the test score for a given topic. Returns None if no score is recorded."""
        return self.completed_topics.get(topic_name)
    
    def add_score(self, topic, score):
        """
        Add a test score for a specific topic.
        """
        self.scores[topic] = score

    def display_progress(self):
        """
        Display the progress of the student.
        """
        print(f"\nProgress for {self.name} (ID: {self.student_id}):")
        for topic, score in self.scores.items():
            print(f"{topic}: Scored {score}")


    def __str__(self):
        """Return a string representation of the student and their test scores."""
        return f"Student: {self.name}\nID: {self.student_id}\nCompleted Topics: {self.completed_topics}"

