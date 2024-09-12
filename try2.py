import getpass
import os
from langchain_community.utilities import SQLDatabase

# Connect to the SQLite database
db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM Artist LIMIT 10;")

# Set Mistral API key from environment variables (or get from user)
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")
print(os.getenv("MISTRAL_API_KEY"))

from langchain_mistralai import ChatMistralAI
from langchain.chains import create_sql_query_chain

# Initialize the language model
llm = ChatMistralAI(model="mistral-large-latest")
chain = create_sql_query_chain(llm, db)

# Ask a question using the language model
response = chain.invoke({"question": "How many employees are there"})
print(response)

# Extract the SQL query from the response (assuming response follows a structured format)
query = response.get('query') or response.split("\n")[0].replace("SQLQuery: ", "")
print(f"Extracted Query: {query}")

# Run the query on the database
db_result = db.run(query)
print(db_result)

# Print the prompt used by the chain
chain.get_prompts()[0].pretty_print()
