import csv

predictions = {}

with open('data_files/train.csv', 'r') as fr:
    fr__dict_reader = csv.DictReader(fr)

    parch_surv_dict = {}
    sibsp_surv_dict = {}

    count = 0

    for passenger in fr__dict_reader:
        surv_val = int(passenger.get('Survived'))
        parch_val = passenger['Parch']
        sibsp_val = passenger['SibSp']
        # print(surv_val)
        if surv_val == 1:
            count += 1
            # print('Survived: ', passenger['Survived'], 'Parch: ', passenger['Parch'])
            if parch_val in parch_surv_dict:
                parch_surv_dict[parch_val] += 1
            else:
                parch_surv_dict[parch_val] = surv_val


            if sibsp_val in sibsp_surv_dict:
                sibsp_surv_dict[sibsp_val] += 1
            else:
                sibsp_surv_dict[sibsp_val] = surv_val


        # passenger_id = passenger['PassengerId']
        # if passenger['Sex'] == 'female':
        #     predictions[passenger_id] = 1
        # else:
        #     predictions[passenger_id] = 0

print('parch_surv_dict: ', parch_surv_dict)
print("")
print('sibsp_surv_dict: ', sibsp_surv_dict)
