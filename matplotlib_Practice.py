import matplotlib.pyplot as plt

'''
x = [1, 2, 4, 5]
y = [1, 2, 4, 5]

plt.plot(x, y, marker='o')
plt.figure(figsize=(12, 9))

# X-axis values
x = [1, 2, 4, 5]
# Corresponding values for Y-axis
y = [20, 10, 13]

# Plotting the points
plt.plot(x,y)
'''

# Display two lines on same graph. Each line must have different color
plt.xlabel("x-axis")
plt.ylabel("y-axis")
x1 = [19, 2, 15, 40, 23]
y1 = [9, 5, 8, 30, 35]

plt.xticks(list(range(1, 50, 5)))
plt.yticks(list(range(1, 50, 5)))

plt.plot(x1, y1, marker="s", label="Line1", linestyle="dashed", color="green", markerfacecolor="black", markersize=5)

x1 = [29, 39, 45, 20, 33]
y1 = [40, 20, 30, 15, 10]
plt.plot(x1, y1, marker='o', label="Line2", linestyle="dotted", color="blue", markerfacecolor="black", markersize=6)
axes = plt.gca()
axes.legend()
plt.show()
