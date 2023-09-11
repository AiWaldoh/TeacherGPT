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
