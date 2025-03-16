import streamlit as st
import os

def create_sidebar():
  """Render the sidebar with options and information"""
  with st.sidebar:
    st.image("static/images/logo.png", width=300)
    st.header("Data Science Tutor Settings (Development)")
    st.markdown("Customize your data science learning experience. Settings are currently under development.")
    st.markdown("---")
    st.markdown("Powered by Gemini 1.5 Pro")
    st.markdown("Created by Pandey Abhishek")
    st.markdown("This application is in its early stages. Expect changes and improvements.")
    st.markdown("---")
    # Add GitHub and LinkedIn links
    st.markdown("[GitHub](https://github.com/vjabhi000985/) | [LinkedIn](https://www.linkedin.com/in/pandey-abhishek-nath-roy/)")
