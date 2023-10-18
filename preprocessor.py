import re
import pandas as pd

def preprocess(data):
    pattern = r'(\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2} (?:[ap]m)?) - (\w+): (.+)'

    # Use re.findall to extract date, sender, and message as tuples
    matches = re.findall(pattern, data)
    # Separate matches into dates, senders, and messages
    dates = [match[0] for match in matches]
    senders = [match[1] for match in matches]
    messages = [match[2] for match in matches]
    # Create a DataFrame with the extracted data
    df = pd.DataFrame({'date': dates, 'sender': senders, 'user_message': messages})

    # Convert the 'date' column to datetime and format it as 12-hour
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y, %I:%M %p')
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['date'] = df['date'].dt.strftime('%d/%m/%Y, %I:%M %p')

    return df
