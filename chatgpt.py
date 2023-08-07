import os
import streamlit as st
import api
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = api.APIKEY


def create_index():
    # This function is not needed anymore since we will read the data each time we perform a query.
    pass


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
    st.title("Language Index Query App")

    # User input for the query
    query = st.text_input("Enter your query:")

    if query:
        # Perform the query and get the results
        result = query_index(query)

        # Display the query results
        if result:
            st.subheader("Query Results:")
            st.write(result)
        else:
            st.warning("No results found for the query.")


if __name__ == "__main__":
    main()
