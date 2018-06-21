import pandas
import numpy

def add_full_name(path_to_csv, path_to_new_csv):

    # There are columns called 'nameFirst' and 'nameLast'.
    # 1) Write a function that reads a csv located at "path_to_csv" into a pandas dataframe
    # and adds a new column called 'nameFull' with a player's full name.
    #
    # For example: for Hank Aaron, nameFull would be 'Hank Aaron',
	#
    # 2) Write the data in the pandas dataFrame to a new csv file located at path_to_new_csv

    master_csv = pandas.read_csv(path_to_csv)

    master_csv['nameFull'] = master_csv['nameFirst'] + ' ' + master_csv['nameLast']

    ave_weight = numpy.mean(master_csv['weight'])

    master_csv['weight'] = master_csv['weight'].fillna(ave_weight)

    master_csv.to_csv(path_to_new_csv)


if __name__ == "__main__":
    path_to_csv = "data_files/baseball_people_lahman.csv"
    path_to_new_csv = "data_files/baseball_people_lahman_fullnames.csv"
    add_full_name(path_to_csv, path_to_new_csv)
