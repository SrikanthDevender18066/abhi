from groq import Groq
import streamlit as st

# Initialize Groq API key directly
api_key = "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"

# Define the Groq client
client = Groq(api_key=api_key)

# Streamlit UI
st.title("Celebrity Search")

# User input
celebrity_name = st.text_input("Enter the name of a celebrity you want to search for:")

# When the user submits a search
if st.button("Search"):
    if celebrity_name:
        # Prepare the request payload
        messages = [
            {
                "role": "user",
                "content": f"I am looking for information about the celebrity: {celebrity_name}. Please provide a brief biography, notable works, and any interesting facts."
            }
        ]

        # Send a request to the Groq API
        try:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model="llama3-8b-8192"  # Replace with the desired model
            )

            information = chat_completion.choices[0].message.content
            st.write("### Information about the Celebrity:")
            st.write(information)
        except Exception as e:
            st.write("Error: Could not fetch information.")
            st.write(str(e))
    else:
        st.write("Please enter a celebrity name to search.")
