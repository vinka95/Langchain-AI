from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI

# Load environment variables
load_dotenv(find_dotenv())
# --------------------------------------------------------------
# LLMs: Get predictions from a language model
# --------------------------------------------------------------

llm = OpenAI(model_name="text-davinci-003")
prompt = "Write a poem about python and ai"
print(llm(prompt))