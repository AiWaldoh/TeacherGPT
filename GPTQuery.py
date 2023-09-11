from GPTBase import GPTBase


class GPTQuery(GPTBase):
    def __init__(
        self,
        # prompt="Vous êtes un enseignant de l'école Mathieu Martin a Dieppe. Vous parlez shiac. Vos réponses sont élaborées et détaillé",
        prompt="Vous êtes un enseignant du college communautaire du Nouveau-Brunswick. Vos réponses sont élaborées et détaillées.",
    ):
        super().__init__(system_prompt=prompt)
        self.prompt = prompt

    def query_gpt(self, topic, subject):
        prompt = f"""
            Préparer 3 paragraphes basé sur {topic} pour élaborer plus en détails sur ce sujet: {subject} 
            Pour chaque paragraphe, donnez un exemple concret et une explication détaillée.
            Répondez avec le style suivant: Enseignant au secondaire.
        """
        return self.generate_message(prompt, temperature=0)

    def small_talk(self, message):
        # Pre-defined static context about the interaction's goal
        static_context = (
            "You're engaging in small talk with a student who's showing "
            "interest in the course SYST1046. The conversation is designed "
            "to make the student feel comfortable and welcomed before diving "
            "into course-specific discussions."
        )

        # Last few lines of the conversation for dynamic context
        dynamic_context = "\n".join(self.history[-4:])

        # Combine the static and dynamic context
        full_context = f"{static_context}\nRecent conversation:\n{dynamic_context}"

        style = (
            "Maintain a cheerful and friendly tone, ensure the student feels "
            "valued and at ease. Respond to their message, and if possible, "
            "direct the conversation subtly towards the course."
        )

        prompt = f"""
            Respond based on the following context: 
            {full_context}
            
            The student's message is: 
            {message}
            
            The style of your response should be: 
            {style}
        """

        response = self.generate_message(prompt, temperature=0.5)
        self.history.append(f"Teacher: {response}")

        return response

    def ask_question(self, contexte, question, style):
        prompt = f"""
            Répondez à un etudiant du secondaire à la question suivante: {question}
            La question est posée concernant ce texte: {contexte}
            
            Le style de votre réponse doit être: 
            {style}
        """
        return self.generate_message(prompt, temperature=0.5)

    def summarize_theory(self, theory):
        prompt = f"""
            Transformez cet article en éléments pédagogiques pertinents, en utilisant une numérotation continue, et assurez-vous que les chiffres ne se répètent pas: {theory}

            Exemple:
            1. Expliquer ce qu'est ...
            2. Définir les termes ...
            3. ...
        """
        return self.generate_message(prompt)
