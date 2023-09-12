from dotenv import load_dotenv
from GPTBase import GPTBase

load_dotenv()

import random


class Chatbot(GPTBase):
    def __init__(self, system_prompt):
        super().__init__(system_prompt)
        self.history = []
        self.message_count = 0
        self.context_static = (
            "Vous engagez une conversation légère avec un étudiant "
            "qui montre de l'intérêt pour le cours SYST1046. La "
            "conversation est conçue pour mettre l'étudiant à l'aise "
            "et le faire se sentir accueilli avant de plonger dans "
            "des discussions spécifiques au cours."
        )
        # List of topics for small talk
        self.topics = [
            "le weekend à venir",
            "les films récents",
            "la musique populaire",
            "des activités de loisir",
            "des projets personnels en informatique",
        ]

    def small_talk(self, message):
        self.history.append(f"Étudiant: {message}")
        self.message_count += 1

        context_dynamic = "\n".join(self.history[-6:])
        context_full = (
            f"{self.context_static}\nConversation récente:\n{context_dynamic}"
        )
        print(self.message_count)
        if self.message_count == 1:
            print("First message")
            style = (
                f"Répondez de manière chaleureuse à son sentiment, sans le saluer à nouveau. "
                f"Introduisez subtilement une question sur {random.choice(self.topics)}."
            )
        elif 2 <= self.message_count <= 3:
            print("Even message")
            style = (
                f"Répondez de manière chaleureuse à son message et posez une question suivi, sans le saluer à nouveau.  "
                # f"Introduisez ensuite subtilement une question sur {random.choice(self.topics)}."
            )
        elif 4 <= self.message_count <= 8:
            style = (
                "Répondez de manière chaleureuse la conversation précédente, sans le saluer à nouveau.  "
                "Terminez en demandant s'il souhaite commencer l'apprentissage comme suit: 'Est-ce que vous voulez commencer le cours?'"
            )
            if "oui" in message.lower():
                return "Commençons le cours."
        else:
            style = "Demandez seulement s'il souhaite commencer l'apprentissage."
            if "oui" in message.lower():
                return "Commençons le cours."

        prompt = f"""
            Répondez en fonction du contexte suivant: 
            {context_full}

            Le message de l'étudiant est: 
            {message}

            Le style de votre réponse doit être: 
            {style}
        """
        response = self.generate_message(prompt)
        self.history.append(f"Professeur: {response}")

        return response
