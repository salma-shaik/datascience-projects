import matplotlib as mp
import numpy as np
import pandas as pd

past_hires = pd.read_csv('data_files/PastHires.csv')
#print(past_hires)

prev_emp_hired = past_hires[['Previous employers','Hired']][4:9]

prev_emp_hired_count = prev_emp_hired['Previous employers'].value_counts()

prev_emp_hired_count.plot(kind='bar')

# print(prev_emp_hired_count)
