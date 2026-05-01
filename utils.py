import pdfplumber

def extract_text(file):
    if file.name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"
        return text
    else:
        return file.read().decode("utf-8")

from models import classifier

ACTION_LABELS = ["task", "decision", "blocker", "info"]

def analyze_transcript(text):
    sentences = [s.strip() for s in text.split(".") if s.strip()]

    results = {
        "actions": [],
        "blockers": [],
        "decisions": []
    }

    for i, sent in enumerate(sentences):

        prediction = classifier(sent, candidate_labels=ACTION_LABELS)

        label = prediction["labels"][0]
        score = prediction["scores"][0]

        item = {
            "text": sent,
            "confidence": round(score, 2),
            "source": f"sentence_{i+1}"
        }

        if label == "task":
            results["actions"].append(item)
        elif label == "blocker":
            results["blockers"].append(item)
        elif label == "decision":
            results["decisions"].append(item)

    return results