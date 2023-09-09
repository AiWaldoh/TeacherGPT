from GPTBase import GPTBase

class GPTQuery(GPTBase):
    def __init__(self, prompt='You are teacher creating detailed theory for students.'):
        super().__init__(system_prompt=prompt)
        self.prompt = prompt
    
    def query_gpt(self, topic, name):
        prompt = f"""
           Provide 3 paragraphs on this topic: {topic} based on {name}
        """
        return self.generate_message(prompt)

    
   