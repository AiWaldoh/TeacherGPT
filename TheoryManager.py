from GPTQuery import GPTQuery
import os
import re


class TheoryManager:
    def __init__(self, folder_path="theorie"):
        self.folder_path = folder_path
        self.theory_dict = self._load_theories()
        self.gpt = GPTQuery()

    def _load_theories(self):
        theory_dict = {}
        try:
            for file in os.listdir(self.folder_path):
                with open(
                    os.path.join(self.folder_path, file), "r", encoding="utf-8"
                ) as f:
                    theory_dict[file] = f.read()
            return theory_dict
        except Exception as e:
            print(f"An error occurred: {e}")
            return {}

    def get_theory(self, filename):
        return self.theory_dict.get(filename, "Item not found.")

    def split_theory(self, text):
        splits = re.split(r"\n*\d+\.", text)
        return [s.strip() for s in splits if s.strip()]

    def enhance_theory(self, theory_split, name):
        enhanced_dict = {}
        for theory in theory_split:
            print(f"Enhancing point: {theory}")
            enhanced_content = self.gpt.query_gpt(topic=theory, name=name)
            enhanced_dict[theory] = enhanced_content
        return enhanced_dict
