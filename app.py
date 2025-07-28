import streamlit as st
from graph import graph
from state import GraphState
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit app configuration
st.set_page_config(page_title="Song Mood Playlist Generator", layout="centered")

# Title and input
st.title("Song Mood Playlist Generator")
song_input = st.text_input("Enter a song title:", placeholder="e.g., Happier Than Ever")

if st.button("Generate Playlist"):
    if song_input:
        with st.spinner("Processing..."):
            input_state = {"song": song_input}
            final_state = graph.invoke(input_state)

            if "error" in final_state:
                st.error(final_state["error"])
            else:
                st.success("Playlist generated successfully!")
                st.write(f"**Mood:** {final_state.get('mood')} (Confidence: {final_state.get('mood_confidence'):.2f})")
                st.write("**Playlist:**")
                playlist = final_state.get("playlist", [])
                if playlist:
                    for title, url in playlist:
                        st.write(f"- [{title}]({url})")
                else:
                    st.warning("No songs found for this playlist.")
    else:
        st.warning("Please enter a song title.")

# Optional: Add a footer or instructions
st.markdown("---")
st.markdown("Enter a song title and click 'Generate Playlist' to get a mood-based playlist from YouTube.")