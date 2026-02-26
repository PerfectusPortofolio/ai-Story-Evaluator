from openai import OpenAI
from .config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze_tone(text):
    prompt = f"""
Analyze the tone and humor style of this writing.

Return:
Tone
Humor Type
Short explanation

Text:
{text}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You analyze humor and tone in writing."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content
