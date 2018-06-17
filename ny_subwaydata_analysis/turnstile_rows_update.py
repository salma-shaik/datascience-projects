import csv


def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt

    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file.

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775

    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the
    Instructor Notes below for more details on the task.

    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy

    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:

    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    # for name in filenames:

# your code here


with open('data_files/subway_turnstile_data.csv', 'r') as fr:
    subway_data_reader = csv.reader(fr)
    new_row_list = []

    with open('data_files/updated_subway_turnstile_data.csv', 'w') as fw:
        subway_data_writer = csv.writer(fw)
        for dataline in subway_data_reader:
            row_prefix = dataline[:3]
            del dataline[:3]
            while len(dataline):
                row = list(row_prefix)
                row.extend(dataline[:5])
                subway_data_writer.writerow(row)
                del dataline[:5]

# A002,R051,02-00-00,05-21-11,00:00:00,REGULAR,003169391,001097585,
#                    05-21-11,04:00:00,REGULAR,003169415,001097588,
#                    05-21-11,08:00:00,REGULAR,003169431,001097607,
#                    05-21-11,12:00:00,REGULAR,003169506,001097686,
#                    05-21-11,16:00:00,REGULAR,003169693,001097734,
#                    05-21-11,20:00:00,REGULAR,003169998,001097769,
#                    05-22-11,00:00:00,REGULAR,003170119,001097792,
#                    05-22-11,04:00:00,REGULAR,003170146,001097801
