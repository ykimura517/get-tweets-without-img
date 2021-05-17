import csv
import pandas as pd

col_names=["id","conversation_id","created_at","date","time","timezone","user_id","username","name","place","tweet","language","mentions","urls","photos","replies_count","retweets_count",
"likes_count","hashtags","cashtags","link","retweet","quote_url","video","thumbnail","near","geo","source","user_rt_id","user_rt","retweet_id","reply_to","retweet_date",
"translate","trans_src","trans_dest"
]

all_tweets_df = pd.read_csv("all-tweet.csv", names = col_names)
tweets_with_images_df=pd.read_csv("tweet-image-only.csv",names = col_names)

df_concat = pd.concat([tweets_with_images_df, all_tweets_df])

df_concat = df_concat[df_concat.duplicated(keep=False,subset='id')==False]

df_concat.to_csv("result.csv")

