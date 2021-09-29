import praw
import pandas as pd
import datetime as dt
from IPython.display import display

reddit = praw.Reddit(client_id = 'Zd6pKgiPqtwE6gx7iMlaEw', 
client_secret = 'KhJY-ievwIFm6TWnoAoqrAr_kX06sA', 
user_agent = 'valorantinfobot',
username = '<username>',
password = '<password>')

subreddit = reddit.subreddit('ValorantCompetitive')
top_subreddit = subreddit.top(limit = 500)

topics = {"title" : [], "score" : [], "id" : [], "url" : [], "num_comm" : [], "created" : [], "body" : []}

for submission in subreddit.hot(limit = 7):
    topics["title"].append(submission.title)
    topics["score"].append(submission.score)
    topics["id"].append(submission.id)
    topics["url"].append(submission.url)
    topics["num_comm"].append(submission.num_comments)
    topics["created"].append(submission.created)
    topics["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics)

def get_date(created):
    return dt.datetime.fromtimestamp(created)
_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)

topics_data.to_csv(r'C:\Users\KevinG\OneDrive\Desktop\Reddit Scraper\test.csv', index=False)
display(topics_data)

