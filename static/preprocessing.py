import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

df  =pd.read_csv("/content/movie_metadata.csv")
df

df.columns

df.shape

df.isna().sum()

df.info()

df  =df.drop(['color', 'num_critic_for_reviews', 'duration',
       'director_facebook_likes', 'actor_3_facebook_likes',
       'actor_1_facebook_likes', 'gross','num_voted_users', 'cast_total_facebook_likes',
       'facenumber_in_poster', 'plot_keywords',
       'movie_imdb_link', 'num_user_for_reviews', 'language', 'country',
       'content_rating', 'budget', 'title_year', 'actor_2_facebook_likes',
       'imdb_score', 'aspect_ratio', 'movie_facebook_likes'],axis = 1)

df.dropna(inplace = True)

df['genres'] = df['genres'].apply(lambda x: str(x).replace('|',' '))

df['movie_title'] = df['movie_title'].apply(lambda x: x[:-1])

df['combined'] = df['director_name'] + ' ' + df['actor_2_name'] + ' ' + df['genres'] + ' ' + df['actor_1_name'] + ' ' + df['actor_3_name']

df.to_csv('movie_finalized_data.csv')
