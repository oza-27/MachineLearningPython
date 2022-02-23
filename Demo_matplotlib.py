import matplotlib.pyplot as plt
# import numpy as np

# x = [1, 2, 3, 4]
# colors = plt.get_cmap("Blues")(np.linspace(0.2, 0.7, len(x)))
#
# fig, ax = plt.subplots()
#
# ax.pie(x, colors=colors, radius=4, center=(4, 4), wedgeprops={"linewidth": 3, "edgecolor": "white"}, frame=True)
# ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
#
# plt.show()

# Display the average temp of each month
import numpy as np

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
average_temp = [19, 18, 25, 29, 31, 38, 39, 30, 28, 20, 19]

month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
               "October", "November", "December"]

plt.xlabel("Months")
plt.ylabel("Average Temperature")

plt.title("Temperature Recordings [2021]")

# plt.plot(months, average_temp)
# plt.bar(months, average_temp, tick_label=month_names)
# plt.scatter(months, average_temp, label=month_names, marker="s", s=30, color="Blue")
#
# plt.show()

fig, ax = plt.subplots()

ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 100), yticks=np.linspace(0, 100, 9))

plt.show()
