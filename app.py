import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


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
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)


if __name__ == '__main__':
    main()

# Note
# run the following streamlite command with: python3 -m streamlit run app.py # import streamlit as st
# from dotenv import load_dotenv
# from PyPDF2 import PdfReader


# def get_pdf_text(pdf_documents):
#     text = ""
#     for pdf in pdf_documents:
#         pdf_reader = PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#     return text


# def main():
#     load_dotenv()
#     st.set_page_config(page_title='Chat Multiple PDFs', page_icon=':books:')

#     if 'text' not in st.session_state:
#         st.session_state.text = ""

#     with st.sidebar:
#         pdf_documents = st.file_uploader('Upload your PDF file', type=[
#                                          'pdf'], accept_multiple_files=True)

#         if st.button('Process'):
#             with st.spinner('Processing...'):
#                 pdf_text = get_pdf_text(pdf_documents)

#                 st.session_state.text = pdf_text

#                 # text_chunks = get_chunks(pdf_text)

#                 st.success('Done!')

#     st.title('Chat with Multiple PDFs :books:')
#     st.text_input('Ask a question about the PDFs')

#     st.write(st.session_state.text)


# if __name__ == '__main__':
#     main()
# Note
# run the following streamlite command with: python3 -m streamlit run app.py
