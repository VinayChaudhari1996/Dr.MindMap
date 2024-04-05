import streamlit as st
from streamlit_markmap import markmap
import google.generativeai as genai

def main():
    
    """
    Main function to create a Streamlit app for generating markdown content with markmap visualization.
    """

    # Set page config and sidebar
    st.set_page_config(page_title="GPT-DR", layout="wide")
    st.sidebar.markdown("# Dr.MindMap")
    st.sidebar.markdown("___")



    # Create or get the session state to store API key
    session_state = st.session_state
    if 'google_api_key' not in session_state:
        session_state.google_api_key = ""

    google_api_key = st.sidebar.text_input('Enter your Google API Key', type='password', value=session_state.google_api_key)


    # Configure generative AI with API key
    genai.configure(api_key=google_api_key)



    @st.cache_data
    def create_markdown(input_data):
        """
        Function to generate detailed markdown content based on the input data.

        Parameters:
            input_data (str): The topic provided by the user.

        Returns:
            str: Generated markdown content.
        """
        prompt = """
        You are expert experienced doctor healthcare consultant.
        please use # and ## for title and subtitle , Strictly follow the markdown format , :-
        
        # Disease Name:
        
            ## Defination=
                -- add subpoints here about disease defination
            ## Causes=
                -- add subpoints here
            ## Types=
                -- add subpoints here
            ## Clinical features=
                -- add subpoints here
            ## Symptoms=
                -- add subpoints here
            ## Preventation=
                -- add subpoints here
            ## Dignosis=
                -- add subpoints here
            ## Useful Medicines=
                -- add subpoints here
        
        Add parent node and child nodes names in bold uses nested structue.

        [Topic] => 
        
        """
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt + input_data)
            return response.text

        except:
            return "Invalid"


    # Add input text box for data with smaller size
    data_input = st.sidebar.text_area("Write down topic here", value='', height=100)
    
    # Add a submit button
    if st.sidebar.button("Submit"):
        # Render markmap with the input data
        if create_markdown(data_input) == 'Invalid':
            st.error("Invalid API Key")
        else:
            output = create_markdown(data_input)
            markmap(output)

            
            st.write(output)
    # Save the API key to the session state
    session_state.google_api_key = google_api_key

if __name__ == "__main__":
    main()
