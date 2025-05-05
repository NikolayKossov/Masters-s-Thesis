import os
from dotenv import load_dotenv
from groq import AsyncGroq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

async def analyze_event(text):
    client = AsyncGroq(
        api_key=groq_api_key
    )

    prompt = (
        f"Given the following text about a historical event, identify and list its causes, "
        f"classified into economic, social, political, military, and other causes if applicable:\n\n"
        f"Text:\n{text}\n\n"
        f"Format the output clearly under each category."
    )

    response = await client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=500,
    )

    return response.choices[0].message.content
