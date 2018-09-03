import numpy as np
import pandas as pd
from sklearn import tree

input_file = "data_files/PastHires.csv"
df = pd.read_csv(input_file, header=0)

# print(df.head())

# convert non-numeric data to numeric
d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)

# print(df.head())

# Separate the features from the target column that we're trying to build a decision tree for
features = list(df.columns[:6])
# print(features)

# Construct the decision tree
y = df["Hired"]
X = df[features]
dt_classifier = tree.DecisionTreeClassifier()
dt_classifier = dt_classifier.fit(X, y)
print(dt_classifier)

print ('dt_classifier: ', dt_classifier.predict([[10, 1, 4, 0, 0, 0]]))
# with open('data_files/dt_classifier.txt', 'w') as f:
#     f = tree.export_graphviz(dt_classifier, out_file=f)

# display
from IPython.display import Image, display
from sklearn.externals.six import StringIO
import pydotplus

dot_data = StringIO()
tree.export_graphviz(dt_classifier, out_file=dot_data, feature_names=features)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
image = Image(graph.create_png())
display(image)

# Enseble learning - using a random forest to predict employment
from sklearn.ensemble import RandomForestClassifier

rf_classifier = RandomForestClassifier(n_estimators = 10)
rf_classifier = rf_classifier.fit(X, y)

#Predict employment of an employed 10-year veteran
print (rf_classifier.predict([[10, 1, 4, 0, 0, 0]]))
#...and an unemployed 10-year veteran
print (rf_classifier.predict([[10, 0, 4, 0, 0, 0]]))




from sklearn.ensemble import RandomForestClassifier