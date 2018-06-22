import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

x = np.arange(-3, 3, 0.01)

# # multiple plots, saving to a file
# plt.plot(x, norm.pdf(x))
# plt.plot(x, norm.pdf(x, 1, 0.5))
# plt.plot(x, norm.pdf(x, 2, 0.1))
# # supported formats: eps, pdf, pgf, png, ps, raw, rgba, svg, svgz
# plt.savefig('C:\\Users\\sshaik2\\Downloads\\DataScience\\Plots\\MultiplePlots.png', format='png')
# plt.show()

# Adjust the axes and grid; Change line types and colors; Labeling axes
axes = plt.axes()
axes.set_xlim([-5, 5])
axes.set_ylim([0, 1])
axes.set_xticks(np.arange(-5, 5, 1))
axes.set_yticks(np.arange(0, 1, 0.1))
axes.grid()
plt.xlabel('Random Variable')
plt.ylabel('Probability')
plt.plot(x, norm.pdf(x), 'g-')
plt.plot(x, norm.pdf(x, 1, 0.5),  'r-.')
plt.legend(['Sample 1', 'Sample 2'], loc=1)
plt.show()