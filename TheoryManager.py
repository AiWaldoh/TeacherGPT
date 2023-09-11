from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from GPTQuery import GPTQuery
import os
import re

MAX_WORKERS = 5


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
        lines_with_numbers = re.findall(r"^\d+\..*$", text, re.M)
        return lines_with_numbers

    # def enhance_theory(self, theory_split, subject):
    #     enhanced_dict = {}
    #     for theory in theory_split:
    #         print(f"Enhancing point: {theory}")
    #         # gpt api call
    #         enhanced_content = self.gpt.query_gpt(topic=theory, subject=subject)
    #         enhanced_dict[theory] = enhanced_content
    #     return enhanced_dict

    def _enhance_single_theory(self, theory, subject):
        print(f"Enhancing point: {theory}")
        # gpt api call
        return theory, self.gpt.query_gpt(topic=theory, subject=subject)

    def enhance_theory(self, theory_split, subject):
        enhanced_dict = {}

        with ThreadPoolExecutor(
            max_workers=min(len(theory_split), MAX_WORKERS)
        ) as executor:
            future_results = {
                executor.submit(self._enhance_single_theory, theory, subject): theory
                for theory in theory_split
            }

            for future in concurrent.futures.as_completed(future_results):
                theory, enhanced_content = future.result()
                enhanced_dict[theory] = enhanced_content

        return enhanced_dict
