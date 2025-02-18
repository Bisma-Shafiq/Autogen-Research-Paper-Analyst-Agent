import os
import streamlit as st
from dotenv import load_dotenv
from agents import ResearchAgent
from dataloader import DataLoader

load_dotenv()

st.title('Research Assistant')


groq_api_key = os.getenv('GROQ_API_KEY')

agents = ResearchAgent(groq_api_key)

data_loader = DataLoader()

query = st.text_input("Enter a research topic.")