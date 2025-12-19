from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from .config import MODEL_PATH

# Load model and tokenizer once
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

# Label mapping (update ONLY if your model uses different labels)
label_map = {
    0: "diabetes",
    1: "cardiovascular",
    2: "respiratory"
}

def predict(text: str):
    inputs = tokenizer(
        text,
        padding=True,
        truncation=True,
        max_length=256,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)

    confidence, predicted_class = torch.max(probs, dim=1)

    label = label_map[int(predicted_class)]
    score = float(confidence)

    return label, score
