import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp chat Analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()  #this file is currently a stream of byte data so now we will conver that file to string format
    data = bytes_data.decode("utf-8") #decoding and converting the file inti string format
    df = preprocessor.preprocess(data)

    st.dataframe(df)

    #fetching unique users
    user_list = df['sender'].unique().tolist()
    user_list.sort()
    user_list.insert(0, "Overall")
    selected_user = st.sidebar.selectbox("Show analysis wrt:", user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages, words, medias, links = helper.fetch_stats(selected_user, df)
        col1, col2, col3, col4 = st.columns(4)  # Get a list of 4 columns

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Total media shared")
            st.title(medias)
        with col4:
            st.header("Total Links shared")
            st.title(links)
        #finding the most active users in the group
        if selected_user=='Overall':
            st.title('Most active user')
            x, new_df=helper.most_busy(df)
            fig, ax = plt.subplots()
            col1, col2= st.columns(2)
            with col1:

                ax.bar(x.index, x.values, color='orange')

                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
        #wordcloud
        st.title("WorldCloud")
        df_wc=helper.create_worldcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        #most common words
        most_common_df=helper.most_common_used_words(selected_user, df)
        st.dataframe(most_common_df)