import json

def extraire_et_sauvegarder_tutoriel(fichier_json_entree: str, fichier_md_sortie: str):
    """
    Extrait la dernière question de l'utilisateur et la réponse finale du modèle
    à partir d'un fichier JSON de conversation et les sauvegarde en Markdown.

    Args:
        fichier_json_entree (str): Le chemin vers le fichier JSON d'entrée.
        fichier_md_sortie (str): Le chemin vers le fichier Markdown de sortie.
    """
    print(f"Lecture du fichier d'entrée : {fichier_json_entree}")

    try:
        with open(fichier_json_entree, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier_json_entree}' n'a pas été trouvé.")
        print("Veuillez vous assurer que le script est dans le même dossier que le fichier de données.")
        return
    except json.JSONDecodeError:
        print(f"Erreur : Le fichier '{fichier_json_entree}' n'est pas un fichier JSON valide.")
        return

    # Initialisation des variables pour stocker le contenu
    question_utilisateur = ""
    reponse_modele = ""

    # Accéder aux "chunks" de la conversation
    chunks = data.get("chunkedPrompt", {}).get("chunks", [])

    if not chunks:
        print("Erreur : Le format du JSON est inattendu. Impossible de trouver 'chunks'.")
        return

    # 1. Trouver la dernière question textuelle de l'utilisateur
    for chunk in reversed(chunks):
        if chunk.get("role") == "user" and "text" in chunk:
            question_utilisateur = chunk["text"]
            break # On a trouvé la dernière question, on arrête la boucle

    # 2. Reconstituer la réponse finale du modèle
    # La réponse finale est généralement le dernier "chunk" avec le role "model"
    dernier_chunk_modele = None
    if chunks and chunks[-1].get("role") == "model":
        dernier_chunk_modele = chunks[-1]

    if dernier_chunk_modele and "parts" in dernier_chunk_modele:
        # Concaténer toutes les parties textuelles de la réponse
        texte_complet_reponse = [part.get("text", "") for part in dernier_chunk_modele["parts"]]
        reponse_modele = "".join(texte_complet_reponse)

    # 3. Créer le contenu Markdown final
    contenu_markdown = f"""{reponse_modele}"""

#     contenu_markdown = f"""
# # Tutoriel : Exploration d'un Notebook d'Analyse de Données

# ## Question de l'utilisateur

# > {question_utilisateur}

# ---

# ## Réponse du Modèle

# {reponse_modele}
#     """

    # 4. Sauvegarder le contenu dans un fichier .md
    try:
        with open(fichier_md_sortie, 'w', encoding='utf-8') as f:
            f.write(contenu_markdown)
        print(f"Succès ! Le tutoriel a été sauvegardé dans : {fichier_md_sortie}")
    except IOError as e:
        print(f"Erreur lors de l'écriture du fichier de sortie : {e}")


if __name__ == "__main__":
    # Nom du fichier JSON exporté depuis Google Drive
    fichier_entree = "Tutoriel Notebook Exploration Data.txt"
    # Nom du fichier de sortie que nous allons créer
    fichier_sortie = "tutoriel.md"

    extraire_et_sauvegarder_tutoriel(fichier_entree, fichier_sortie)
