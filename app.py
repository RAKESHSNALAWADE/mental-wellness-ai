import streamlit as st
import openai
from textblob import TextBlob

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"

# App title
st.set_page_config(page_title="Mental Wellness AI", layout="centered")
st.title("🧠 Mental Wellness AI Chatbot")
st.markdown("Hi there! I'm here to support your emotional wellbeing. Let's talk.")

# Mood check-in
mood = st.selectbox("How are you feeling today?", ["😊 Happy", "😐 Okay", "😔 Sad", "😠 Angry", "😰 Anxious", "😴 Tired"])

# User input
user_input = st.text_area("What's on your mind?", height=150)

# Analyze sentiment
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Generate AI response
def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are a kind, supportive mental wellness assistant for students."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=200
    )
    return response.choices[0].message.content.strip()

# Submit button
if st.button("Send"):
    if user_input:
        sentiment = get_sentiment(user_input)
        ai_response = get_ai_response(user_input)

        st.markdown("### 🤖 AI Response:")
        st.write(ai_response)

        # Optional: Crisis alert
        if sentiment < -0.5:
            st.warning("⚠️ It seems you're feeling really low. Consider talking to a trusted adult or counselor.")
    else:
        st.error("Please share something so I can help.")

# Footer
st.markdown("---")
st.caption("This is a supportive tool, not a substitute for professional help.")
