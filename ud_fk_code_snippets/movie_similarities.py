import pandas as pd

ratings_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('data_files/u.data', sep='\t', names=ratings_cols, usecols=range(3))

movie_cols = ['movie_id', 'title']
movies = pd.read_csv('data_files/u.item', encoding='latin1', sep='|', names=movie_cols, usecols=range(2))

ratings = pd.merge(movies, ratings)

# print(ratings.head())


# Create a user/movie rating matrix

movie_ratings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')
# print(movie_ratings.head())


# Extract a series of users who rated Star Wars
star_wars_ratings = movie_ratings['Star Wars (1977)']
# print(star_wars_ratings.head())


# Compute the pairwise correlation of Star Wars' vector of user rating with every other movie!
similar_movies = movie_ratings.corrwith(star_wars_ratings)
similar_movies = similar_movies.dropna()
similar_movies_df = pd.DataFrame(similar_movies)
# print(similar_movies_df.head(10))

similar_movies.sort_values(ascending=False)
# print(similar_movies)

# Create a dataframe with number of ratings, ave rating for each movie
import numpy as np
movie_stats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
# print(movie_stats.head())

# Remove any movies which are rated by fewer than 100 people
popular_movies = movie_stats['rating']['size'] >= 100
top_15_movies = movie_stats[popular_movies].sort_values([('rating', 'mean')], ascending=False)[:15]
# print(top_15_movies)

# Join this data with original set of similar movies to Star Wars
sw_corr_popmovies = movie_stats[popular_movies].join(pd.DataFrame(similar_movies, columns=['similarity']))
# print(sw_corr_popmovies.head())


# sort the above by similarity score
sw_corr_popmovies_top15 = sw_corr_popmovies.sort_values(['similarity'], ascending=False)[:15]
print(sw_corr_popmovies_top15)

