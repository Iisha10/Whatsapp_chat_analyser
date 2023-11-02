from urlextract import URLExtract
extract=URLExtract()
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
def fetch_stats(selected_user, df):
    if selected_user == 'Overall':
        # 1. fetching number of messages
        num_messages = df.shape[0]
        # 2. number of words
        words = []
        for message in df['user_message']:
            words.extend(message.split())
        medias = df[df['user_message'] == '<Media omitted>'].shape[0]
    # fetch number of links
        links=[]
        for message in df['user_message']:
            links.extend(extract.find_urls(message))
        return num_messages, len(words), medias, len(links)
    #


    else:
        new_df = df[df['sender'] == selected_user]
        num_messages = new_df.shape[0]
        links = []
        for message in new_df['user_message']:
            links.extend(extract.find_urls(message))
        words = []
        for message in new_df['user_message']:
            words.extend(message.split())
        medias = new_df[new_df['user_message'] == '<Media omitted>'].shape[0]
        return num_messages, len(words), medias, len(links)


def most_busy(df):
    x=df['sender'].value_counts().head()
    df=round((df['sender'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'sender': 'name', 'count': 'percent'})
    return x, df

def create_worldcloud(selected_user, df):
    if selected_user!='Overall':
        df=df[df['sender'] == selected_user]

    wc=WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc=wc.generate(df['user_message'].str.cat(sep= " "))
    return df_wc

def most_common_used_words(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()
    if selected_user!='Overall':
        df=df[df['sender'] == selected_user]
    temp = df[df['sender'] != 'group_notification']
    temp=temp[temp['user_message'] != '<Media omitted>']
    words = []

    for message in temp['user_message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    most_common_df=pd.DataFrame(Counter(words).most_common(20))
    return most_common_df