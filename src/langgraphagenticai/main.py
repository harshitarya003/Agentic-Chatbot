import streamlit as st
from src.langgraphagenticai.ui.streamlit.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI Streamlit application.
    This function initializes the Streamlit UI, retrieves user selections, and displays the selected options.
    """

    #load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.warning("Please make selections in the sidebar to proceed.")
        return

    user_message = st.chat_input("Enter you message here...")

    if user_message:
        try:
            #configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Failed to configure the LLM model. Please check your selections and try again.")
                return

            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("No use case selected. Please select a use case to proceed.")
                return
        except Exception as e:
            st.error(f"An error occurred while configuring the LLM: {e}")
            return