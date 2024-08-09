!pip install -qqq openai
!pip install -qqq groq

import os
from google.colab import userdata
os.environ["GROQ_API_KEY"] = userdata.get('groqai-key')
os.environ["OPEN_API_KEY"] = userdata.get('openai-key')

from groq import Groq
from openai import OpenAI

client2 = Groq()
client1 = OpenAI()

def profile_user(tweets):
    prompt = (
        "Based on the following tweets, identify the user's personal traits, hobbies, likes, and dislikes:\n\n"
        "Tweets:\n"
        + '\n'.join(tweets)
        + "\n\nPersonal Traits:\n"
        "Hobbies:\n"
        "Likes:\n"
        "Dislikes:\n"
    )
    return get_completion(prompt)

def load_and_process_csv(file_path):
    df = pd.read_csv(file_path)
    print("Available columns:", df.columns)
    
    if 'tweets' not in df.columns:
        raise KeyError("The 'tweet' column is not found in the CSV file.")
    
    tweets = df['tweets'].tolist()
    return tweets


csv_file_path = '/content/JeffBezos.csv'
# Replace 'path_to_your_csv_file.csv' with the actual path to your CSV file.



user_profile = profile_user(user_tweets)

# Print the user's profile
print(user_profile)

