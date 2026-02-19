import json
from datetime import datetime
from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

SYSTEM_PROMPT = """
Ты дружелюбный Telegram-бот.
Отвечай кратко и понятно.
Отвечай кратко (до 5 абзацев).
Правила:
- Не используй LaTeX.
- Не используй математическую разметку (\[ \] \( \)).
- Не используй формулы в TeX-стиле.
- Пиши формулы обычным текстом.
- Без Markdown.
- Без оформления.
"""

def ask_ai(user_text: str):
    # print("USER:", user_text)
    response = client.chat.completions.create(
        model="openrouter/aurora-alpha",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ],
        temperature=0.5,
        max_tokens=1500
    )

    return response.choices[0].message.content

def log_to_json(user_id, username, user_text, reply):
    log_entry = {
        "user_id": user_id,
        "message": user_text,
        "response": reply,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        with open("ai_logs.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(log_entry)
    with open("ai_logs.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
