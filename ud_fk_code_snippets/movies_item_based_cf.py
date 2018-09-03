# import MovieLens 100k data set into a pandas DataFrame
import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('data_files/u.data', sep='\t', names=r_cols, usecols=range(3))

m_cols = ['movie_id', 'title']
movies = pd.read_csv('data_files/u.item', encoding='latin1', sep='|', names=m_cols, usecols=range(2))

ratings = pd.merge(movies, ratings)

# print(ratings.head())

# Pivot ratings table to construct a matrix of users and movies they rated.
user_ratings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')
# print(user_ratings.head(2))

# Compute a correlation score for every column pair in the user_ratings sparse matrix
corr_matrix = user_ratings.corr()
# print(corr_matrix.head())

# Remove results where fewer than 100 people rated a pair of movies
corr_matrix = user_ratings.corr(method='pearson', min_periods=100)
# print(corr_matrix.head())


# Movie ratings of test user_id 0
test_ratings = user_ratings.loc[0].dropna()
# print(test_ratings)

test_record = pd.DataFrame([[000, 5]],columns=['user_id', '12 Angry Men (1957)'])
user_ratings = pd.concat([user_ratings,test_record])

# Go through each movie that a test user rated and build up a list of possible recommendations
# based on the movies similar to the ones that the user rated.

# For each movie that the user rated, retrieve the list of similar movies from correlation matrix
sim_candidates = pd.Series()
for i in range(0, len(test_ratings)):
    # print('Adding similarities for ' +test_ratings.index[i] + "...")
    # Retrieve similar movies to this one that the user rated
    sims = corr_matrix[test_ratings.index[i]].dropna()
    # print(sims[:3])
    # Scale its similarity by how well the user rated this movie
    sims = sims.map(lambda x:x * test_ratings[i])
    # Add the score to the list of similarity candidates
    sim_candidates = sim_candidates.append(sims)

print("Sorting...")
sim_candidates.sort_values(inplace = True, ascending=False)
# print(sim_candidates.head(5))

# some movies can be similar to more than one movie that the user rated. groupby to increase its worth
sim_candidates = sim_candidates.groupby(sim_candidates.index).sum()
sim_candidates.sort_values(inplace=True, ascending=False)
print(sim_candidates.head(10))

filtered_sims = sim_candidates.drop(test_ratings.index)
# print(filtered_sims.head(10))
