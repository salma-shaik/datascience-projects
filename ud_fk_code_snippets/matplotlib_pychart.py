import matplotlib.pyplot as plt

values = [11, 40, 25, 4, 20]
colors = ['b', 'g', 'purple', 'r', 'pink']
labels = ['Russia', 'USA', 'India', 'Canada', 'China']
explode = [0, 0, .2, 0, 0]
plt.pie(values, colors=colors, labels=labels, explode=explode)
plt.title('Applicants Locations')
plt.show()

