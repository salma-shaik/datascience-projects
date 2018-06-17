import datetime


def reformat_subway_dates(date):
    '''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-day.

    In order to join these two data sets together, we'll want the dates formatted
    the same way.  Write a function that takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.

    Hint:
    There are a couple of useful functions in the datetime library that will
    help on this assignment, called strptime and strftime.
    More info can be seen here and further in the documentation section:
    http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
    '''

    print(date)
    print(type(date))

    # subway_date = datetime.datetime.strptime(date, '%m-%d-%y')
    subway_date = datetime.datetime.strptime(date, '%m-%d-%y')
   # subway_date = datetime.datetime.strptime(date, '%y-%m-%d')
    print('Subway date format: ', subway_date)

    # subway_date_to_weather_date = subway_date.strftime('%Y-%m-%d')
    # print('subway_date_to_weather_date: ', subway_date_to_weather_date)

    # oldformat = '20140716'
    # datetimeobject = datetime.datetime.strptime(oldformat, '%Y%m%d')
    # print(datetimeobject)

# reformat_subway_dates('16-11-16') # '%y-%m-%d'
reformat_subway_dates('11-16-16') #'%m-%d-%y'
