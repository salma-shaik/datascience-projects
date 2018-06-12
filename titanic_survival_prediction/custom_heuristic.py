'''
For this exercise, you need to write a custom heuristic that will take
    in some combination of the passenger's attributes and predict if the passenger
    survived the Titanic diaster.

    Can your custom heuristic beat 80% accuracy?

    The available attributes are:
    Pclass          Passenger Class
                    (1 = 1st; 2 = 2nd; 3 = 3rd)
    Name            Name
    Sex             Sex
    Age             Age
    SibSp           Number of Siblings/Spouses Aboard
    Parch           Number of Parents/Children Aboard
    Ticket          Ticket Number
    Fare            Passenger Fare
    Cabin           Cabin
    Embarked        Port of Embarkation
                    (C = Cherbourg; Q = Queenstown; S = Southampton)


    Sibsp - if a person has siblings and is less than 18, then more likely to survive, coz young
            children would be escorted to safety first
    Parch  - if a parent has > 3 parch, then less likely to survive coz he/she is middle aged and
            older women, children would be escorted to safety first. If 3, then definitely mom and
            a kid or 1 parent and 2 kids. Either way the person in question is low priority.
'''


import csv

predictions = {}

with open('data_files/train.csv', 'r') as fr:
    fr__dict_reader = csv.DictReader(fr)

    for passenger in fr__dict_reader:
        # print(passenger)
        passenger_id = passenger['PassengerId']

        # some groups of people were more likely to survive than others, such as women, children, and the upper-class.
        '''
            # female
            # upper class and child
            # upper class and no parents/children
            # child with one or both parents irrespective of class
            # 1st class with no sibling or spouse
            # anyone with neither Parch nor SibSp
            
            
              \
            or passenger['Parch'] > 5 or passenger['SibSp'] > 3:
            or passenger['Pclass'] == 3 and passenger['Age'] < 13 \
            
        '''
        # 80.02
        if passenger['Sex'] == 'female' or passenger['Age'] < 4 \
                or passenger['Pclass'] == 1 and passenger['Age'] < 18 \
                or passenger['Pclass'] == 2 and passenger['Age'] < 16:
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0

print(predictions)