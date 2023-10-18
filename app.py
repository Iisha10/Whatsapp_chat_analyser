import streamlit as st
import preprocessor


st.sidebar.title("Whatsapp chat Analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue() #this file is currently a stream of byte data so now we will conver that file to string format
    data = bytes_data.decode("utf-8")#decoding and converting the file inti string format
    df = preprocessor.preprocess(data)

    st.dataframe(df)

    #fetching unique users
    user_list = df['sender'].unique().tolist()
    user_list.sort()
    user_list.insert(0, "Overall")
    st.sidebar.selectbox("Show analysis wrt:", user_list)

    if st.sidebar.button("Show Analysis"):
        pass
