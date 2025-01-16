# import streamlit as st

# # Title and Header
# st.title("Chat with Me! 🤖")
# st.markdown("""
# <div style="background-color: #f4f4f4; padding: 10px; border-radius: 10px;">
#     <h2 style="text-align: center; color: #4CAF50;">Welcome to the Chatbot</h2>
#     <p style="text-align: center;">Ask me anything, and I'll try to respond! 😊</p>
# </div>
# """, unsafe_allow_html=True)

# # Chat history
# if "chat_history" not in st.session_state:
#     st.session_state["chat_history"] = []

# # User input
# user_input = st.text_input("You:", key="input", placeholder="Type your message here...", label_visibility="collapsed")

# # Generate a simple response
# def generate_response(user_message):
#     responses = {
#         "hello": "Hi there! How can I assist you today? 😊",
#         "how are you": "I'm just a bunch of code, but I'm doing great! How about you? 🤖",
#         "what's your name": "I'm your friendly chatbot! You can call me ChatBuddy. 🌟",
#         "bye": "Goodbye! Have a great day! 👋",
#     }
#     return responses.get(user_message.lower(), "I'm not sure how to respond to that. Could you ask something else? 🤔")

# # Handle user input
# if user_input:
#     st.session_state["chat_history"].append({"user": user_input, "bot": generate_response(user_input)})

# # Display chat history
# for chat in st.session_state["chat_history"]:
#     st.markdown(f"**You:** {chat['user']}")
#     st.markdown(f"**ChatBuddy:** {chat['bot']}")

# # Footer
# st.markdown("""
# <div style="text-align: center; margin-top: 20px; font-size: 14px;">
#     <p>Made with ❤️ using <a href="https://streamlit.io" target="_blank">Streamlit</a></p>
# </div>
# """, unsafe_allow_html=True)
import streamlit as st
import pandas as pd

def load_data(file_path):
    # Read the dataset, assuming it's a tab-separated file
    data = pd.read_csv(file_path, sep="\t", header=None, names=["input", "response"])
    print(data.head())  # Debugging: Print the first few rows of the dataset
    return data

# Call the function
data = load_data("dialogs.txt")


# Chatbot UI
st.title("Streamlit Chatbot 🤖")
st.markdown("### Ask me something and I'll respond based on the dataset!")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Function to find the best response from the dataset
def get_response(user_input, dataset):
    # Case-insensitive match
    response = dataset.loc[dataset["input"].str.lower() == user_input.lower(), "response"]
    return response.values[0] if not response.empty else "I'm not sure how to respond to that."

# User input
user_input = st.text_input("You:", key="input", placeholder="Type your message here...", label_visibility="collapsed")

if user_input:
    bot_response = get_response(user_input, data)
    st.session_state["chat_history"].append({"user": user_input, "bot": bot_response})

# Display the conversation
for chat in st.session_state["chat_history"]:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")

st.markdown("### Powered by your dataset! 🚀")
