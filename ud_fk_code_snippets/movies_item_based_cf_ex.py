# try a method other than pearson's
# try with a different min_periods value

# Movies similar to the ones that the user has rated poorly should be penalized rather than just scaling down
# Identify and remove outliers i.e users who have rated huge amount of movies causing disproportionate effect on the results

# train test
# How well the recommender system is able to predict the movies that the suer has rated
#

# import MovieLens 100k data set into a pandas DataFrame

import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('data_files/u.data', sep='\t', names=r_cols, usecols=range(3))

m_cols = ['movie_id', 'title']
movies = pd.read_csv('data_files/u.item', encoding='latin1', sep='|', names=m_cols, usecols=range(2))

ratings = pd.merge(movies, ratings)

# print(ratings.head())

# Pivot ratings table to construct a matrix of users and movies they rated
user_ratings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')
# print(user_ratings.head())

# Compute correlation score of every column with every other column in the user_ratings sparse matrix
# corr_matrix = user_ratings.corr(method='pearson', min_periods=100)
# corr_matrix = user_ratings.corr(method='kendall', min_periods=100)
# corr_matrix = user_ratings.corr(method='spearman', min_periods=100)
# corr_matrix = user_ratings.corr(method='pearson', min_periods=75)
corr_matrix = user_ratings.corr(method='pearson', min_periods=150)
# print(corr_matrix.head())

user_ratings.drop(user_ratings.index[943])

test_record = pd.DataFrame([[5, 3, 1]],columns=['12 Angry Men (1957)', '101 Dalmatians (1996)', 'Terminator 2: Judgment Day (1991)'])
user_ratings = pd.concat([user_ratings,test_record], ignore_index=True)

# print(user_ratings.tail())

test_ratings = user_ratings.loc[944].dropna()
# print(test_ratings)


# For each movie that the user has rated, retrieve a list of similar movies from correlation matrix
sim_candidates = pd.Series()
for i in range(0, len(test_ratings)):
    # Retrieve similar movies to this one that the user rated
    sims = corr_matrix[test_ratings.index[i]].dropna()
    # print(sims[:5])
    # Scale its similarity by how well the user rated this movie
    sims = sims.map(lambda x: x * test_ratings[i])
    # Add the score to the list of similarity candidates
    sim_candidates = sim_candidates.append(sims)

print("Sorting....")
sim_candidates.sort_values(inplace=True, ascending=False)
# print(sim_candidates.head(10))

# some movies can be similar to more than one movie that the user rated. grouypby to increase its worth
sim_candidates = sim_candidates.groupby(sim_candidates.index).sum()
sim_candidates.sort_values(inplace=True, ascending=False)
print(sim_candidates)

# filtered_sims = sim_candidates.drop(test_ratings.index)
# print(filtered_sims)
