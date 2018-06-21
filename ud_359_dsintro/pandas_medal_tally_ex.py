import numpy as np
from pandas import DataFrame, Series


#################
# Syntax Reminder:
#
# The following code would create a two-column pandas DataFrame
# named df with columns labeled 'name' and 'age':
#
# people = ['Sarah', 'Mike', 'Chrisna']
# ages  =  [28, 32, 25]
# df = DataFrame({'name' : Series(people),
#                 'age'  : Series(ages)})

def create_dataframe():
    '''
    Create a pandas dataframe called 'olympic_medal_counts_df' containing
    the data from the table of 2014 Sochi winter olympics medal counts.

    The columns for this dataframe should be called
    'country_name', 'gold', 'silver', and 'bronze'.

    There is no need to  specify row indexes for this dataframe
    (in this case, the rows will automatically be assigned numbered indexes).

    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    # olympic_medal_counts_df = DataFrame({'country_name': Series(countries), 'gold': Series(gold),
    #                                      'silver': Series(silver), 'bronze': Series(bronze)
    #                                      })

    # # We do not need to use pandas.Series, can pass in python lists as the values in this case:
    olympic_medal_counts_df = DataFrame({'country_name': countries, 'gold': gold,
                                         'silver': silver, 'bronze': bronze
                                         })

    avg_medal_count = olympic_medal_counts_df[['gold', 'silver', 'bronze']].apply(np.mean)

    # print(avg_medal_count)

   # print(olympic_medal_counts_df.loc[0])

    points_arr = np.array([4, 2, 1])

    olympic_points_df = DataFrame({'country_name': countries, 'points': np.dot(DataFrame(olympic_medal_counts_df[['gold', 'silver', 'bronze']]), points_arr)})

    print(olympic_points_df)

    # return olympic_medal_counts_df


create_dataframe()
