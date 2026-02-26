from openai import OpenAI
from .config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def evaluate_story_structure(text):
    prompt = f"""
Analyze the storytelling structure of the text below.

Classify it into one of these:
Linear
Non-linear
Branching
Meandering
Circular
Episodic

Explain the reasoning briefly.

Text:
{text}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a narrative structure expert."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content


def evaluate_creativity(text):
    prompt = f"""
Rate the creativity of this text from 1 to 10 and explain why.

Text:
{text}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You evaluate writing creativity."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content
