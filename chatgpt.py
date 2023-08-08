from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import TextLoader
import streamlit as st
import sys
import os
__import__('pysqlite3')


sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# Load OpenAI API key from environment variable
openai_api_key = os.environ.get("OPENAI_API_KEY")

if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_api_key


def query_index(query):
    # Read the data from 'data.txt' every time a query is performed.
    loader = TextLoader('data.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])

    # Use st.write() to display all properties of 'loader' in the Streamlit app
    # Print the value of 'data.txt' to the console
    with open('data.txt', 'r') as file:
        data_content = file.read()
        print("Value of 'data.txt':", data_content)

    return index.query(query)


def main():
    st.title("MCP Helpdesk AI")

    # User input for the query
    query = st.text_input("Enter your question:")

    if query:
        # Perform the query and get the results
        result = query_index(query)

        # Display the query results
        if result:
            st.subheader("Possible solution:")
            st.write(result)
        else:
            st.warning("No results found for the query.")


if __name__ == "__main__":
    main()
