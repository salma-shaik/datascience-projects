'''

 Here's the algorithm, predict the passenger survived if:
    1) If the passenger is female or
    2) if his/her socioeconomic status is high AND if the passenger is under 18

    Otherwise, your algorithm should predict that the passenger perished in the disaster.

    You can access the socioeconomic status of a passenger via passenger['Pclass']:
    High socioeconomic status -- passenger['Pclass'] is 1
    Medium socioeconomic status -- passenger['Pclass'] is 2
    Low socioeconomic status -- passenger['Pclass'] is 3

    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the Passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associated value should be 1 if the
    passenger survived or 0 otherwise.

'''

import csv

predictions = {}

with open('data_files/train.csv', 'r') as fr:
    fr__dict_reader = csv.DictReader(fr)

    for passenger in fr__dict_reader:
        # print(passenger)
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'female' or passenger['Pclass'] == 1 and passenger['Age'] < 18:
            predictions[passenger_id] = 1
        else :
            predictions[passenger_id] = 0

print(predictions)

