# EnseignantGPT : Application d'enseignement basée sur l'IA

EnseignantGPT est une plateforme d'enseignement innovante qui exploite la puissance de l'IA pour guider les étudiants à travers les sujets, garantissant la compréhension avant de progresser. Le système présente les sujets un par un, administre des tests pour évaluer la compréhension, et poursuit le cycle d'enseignement.

## Fonctionnalités :

- **Livraison de contenu dynamique** : Livre du contenu basé sur les sujets. Si un étudiant a des difficultés, le contenu peut être répété.
- **Test automatisé** : Après avoir complété un sujet, les étudiants sont testés sur leur compréhension. Ils doivent réussir le test pour passer au sujet suivant.
- **Suivi des progrès** : Visualisez les progrès des étudiants, y compris les sujets abordés et leurs scores aux tests associés.

## Configuration et installation :

1. Clonez le dépôt :
<pre>
git clone https://github.com/AiWaldoh/TeacherGPT.git
</pre>

2. Naviguez vers le répertoire du projet :
<pre>
cd EnseignantGPT
</pre>

3. Installez les dépendances nécessaires (le cas échéant) :
<pre>
pip install -r requirements.txt
</pre>

4. Installez `venv` (si ce n'est pas déjà fait) et créez un nouvel environnement virtuel :

```bash
python -m venv monenv
```

**Note :** Vous pouvez remplacer `monenv` par le nom que vous souhaitez donner à votre environnement virtuel.

5. Activez l'environnement virtuel :

- **Windows :**

```bash
.\monenv\Scripts\activate
```

- **macOS et Linux :**

```bash
source monenv/bin/activate
```
6. Exécutez l'application :
<pre>
python main.py
</pre>

## Utilisation :

Après avoir configuré l'application, les utilisateurs peuvent :

1. Enregistrer un étudiant.
2. Commencer une leçon pour l'étudiant sur un sujet spécifique.
3. Administrer un test pour le sujet.
4. Voir les progrès de l'étudiant.

## Contribuer :

Nous accueillons les contributions ! Veuillez forker le dépôt et apporter les modifications que vous souhaitez. Les pull requests sont les bienvenues.

## Améliorations futures :

- Ajouter plus de sujets pour élargir le programme.
- Mettre en œuvre des stratégies de test adaptatives.
- Intégrer du contenu multimédia pour des expériences d'apprentissage riches.

## Licence :

Ce projet est sous licence MIT.
