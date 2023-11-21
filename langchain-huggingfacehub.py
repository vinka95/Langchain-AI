from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate

import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

load_dotenv()

repo_id = "gpt2"
hub_llm = HuggingFaceHub(repo_id=repo_id,
                         model_kwargs={'temperature': 0.5, 'max_length': 100})

prompt = PromptTemplate(
    input_variables=["joke"],
    template="You the best comedian, someone who has got the verbose style of George Carlin and as satirical as Louis CK could get! Now tell me a joke on {joke}"    
)

hub_chain = LLMChain(prompt=prompt, llm=hub_llm, verbose=True)
print(hub_chain.run("dogs"))
print(hub_chain.run("dead babies"))
print(hub_chain.run("airplanes"))