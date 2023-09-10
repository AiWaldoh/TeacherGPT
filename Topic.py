class Topic:
    def __init__(self, name, description):
        """
        Initialize a new topic.
        """
        self.name = name
        self.description = description
        self.contents = []  # Initialize contents as an empty list
        self.test = None

    def add_content(self, content):
        """Add content to the topic."""
        if content.content_data not in [c.content_data for c in self.contents]:
            self.contents.append(content)
        else:
            print(f"Content already exists in this topic!")

    def get_content(self):
        """
        Retrieve content associated with the topic.
        """
        return self.content_list

    def set_test(self, test):
        """Set the test for this topic."""
        self.test = test

    def display_content(self):
        """Display the content of the topic."""
        print(f"Learning Topic: {self.name}")
        for content in self.contents:
            print(f"\nTitle: {content.content_type}")

            print(f"Data: {content.content_data}")

    def administer_test(self, student):
        """Administer the test associated with this topic."""
        if self.test:
            return self.test.administer(student)
        else:
            print(f"No test defined for the topic: {self.name}")
            return None

    def __str__(self):
        return f"Topic: {self.name}\nDescription: {self.description}\nNumber of Contents: {len(self.contents)}"
