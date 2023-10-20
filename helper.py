def fetch_stats(selected_user, df):
    if selected_user == 'Overall':
        # 1. fetching number of messages
        num_messages = df.shape[0]
        # 2. number of words
        words = []
        for message in df['user_message']:
            words.extend(message.split())
        medias = df[df['user_message'] == '<Media omitted>'].shape[0]
        return num_messages, len(words), medias

    else:
        new_df = df[df['sender'] == selected_user]
        num_messages = new_df.shape[0]
        words = []
        for message in new_df['user_message']:
            words.extend(message.split())
        medias = new_df[new_df['user_message'] == '<Media omitted>'].shape[0]
        return num_messages, len(words), medias
