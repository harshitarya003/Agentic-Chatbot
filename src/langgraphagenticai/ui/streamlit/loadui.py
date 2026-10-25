import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config  

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title())
        st.header(self.config.get_page_title())

        with st.sidebar:
            #get options from config file
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            #LLM Selection
            self.user_controls["llm_selection"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["llm_selection"] == "Groq":
                #model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")

                #Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your GROQ API Key to proceed.")
                    # st.stop()  # Stop execution until the API key is provided

                #Usecase selection
                print("Usecase Options:", usecase_options)  # Debugging line
                self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)
        return self.user_controls