from transformers import pipeline

# Load model from HuggingFace:
pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=128,
    repetition_penalty=1.2,
    do_sample=False
)

def clean_output(text: str) -> str:
    sentences = list(dict.fromkeys(text.split(". ")))
    return ". ".join(sentences).strip()


def call_llm(prompt: str) -> str:
    output = pipe(prompt)[0]["generated_text"]
    return clean_output(output)