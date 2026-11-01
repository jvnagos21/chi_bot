from dotenv import load_dotenv
from google import genai

load_dotenv()

llm = genai.Client()

interaction = llm.interactions.create(
    model="gemini-3.5-flash",
    input="hello chi, how are you?"
)

print(interaction.output_text)
