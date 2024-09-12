import getpass
import os

from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM Artist LIMIT 10;")

# os.environ["MISTRAL_API_KEY"] = getpass.getpass()
# we use get pass to get the API key from the user, and then set it as an environment variable, but the apikey will not be shown on the screen

os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")
print(os.getenv("MISTRAL_API_KEY"))


from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(model="mistral-large-latest")

from langchain.chains import create_sql_query_chain

chain = create_sql_query_chain(llm, db)
response = chain.invoke({"question": "How many employees are there"})
print(response)
db.run(response)

chain.get_prompts()[0].pretty_print()