import streamlit as st
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with Multiple PDFs",
                       page_icon=":books:")

    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.button("Processing"):


if __name__ == '__main__':
    main()

# Note
# run the following streamlite command with: python3 -m streamlit run app.py
