class Content:
    def __init__(self, content_type, content_data):
        """
        Initialize content with its type and actual data.
        """
        self.content_type = content_type
        self.content_data = content_data

    def display(self):
        """
        Display the content to the student.
        """
        if self.content_type == 'video':
            print(f"Watch this video: {self.content_data}")
        elif self.content_type == 'article':
            print(f"Read this article: {self.content_data}")
        else:
            print("Unsupported content type.")

    def __str__(self):
        """
        Return a string representation of the content for easy viewing.
        """
        return f"Type: {self.content_type}\nData: {self.content_data}"

