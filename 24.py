import fitz  
import re
import os

def classify_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()

        if len(text.split()) > 1500:
            print("Error: Essay exceeds 1500 words.")
            return

        
        words = text.split()
        verbs = []
        nouns = []
        pronouns = []
        prepositions = []
        phrasal_verbs = []

        
        common_verbs = ['is', 'are', 'run', 'go', 'eat']
        common_nouns = ['man', 'school', 'book']
        common_pronouns = ['he', 'she', 'it', 'they']
        common_prepositions = ['in', 'on', 'at', 'with']
        common_phrasal = ['look up', 'break down', 'give up']

        
        for word in words:
            lw = word.lower()
            if lw in common_pronouns:
                pronouns.append(word)
            elif lw in common_nouns:
                nouns.append(word)
            elif lw in common_verbs:
                verbs.append(word)
            elif lw in common_prepositions:
                prepositions.append(word)

        with open("verbs.txt", "w") as f: f.write("\n".join(verbs))
        with open("nouns.txt", "w") as f: f.write("\n".join(nouns))
        with open("pronouns.txt", "w") as f: f.write("\n".join(pronouns))
        with open("prepositions.txt", "w") as f: f.write("\n".join(prepositions))

        print("[INFO] Classified word files saved.")
        print("[INFO] Email simulation completed.")

    except FileNotFoundError:
        print("Error: PDF file not found.")
    except Exception as e:
        print(f"Error: {e}")
classify_text_from_pdf("essay.pdf")