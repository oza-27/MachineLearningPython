import matplotlib.pyplot as plt
import numpy as np

# x = 4 + np.random.normal(0, 1.5, 200)
# fig, ax = plt.subplots()
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Histogram Graph")
# ax.hist(x, bins=10, linewidth=3.0, edgecolor="CYAN")
# ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 100), yticks=np.linspace(0, 100, 9))
# plt.show()

# Pie Chart
x = [1, 2, 3, 4]
colors = plt.get_cmap('Blues')(
    np.linspace(0.2, 0.7, len(x)))  # here 0.2 and 0.7 is used for the color shade of the pie chart
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=4, center=(4, 4), wedgeprops={"linewidth": 3, "edgecolor": "white "}, frame=True)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
plt.show()
