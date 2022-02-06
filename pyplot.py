import matplotlib.pyplot as plt

# x - axis values
x = [1, 2, 3]

# y- axis values
y = [20, 10, 14]

# plotting the point
plt.plot(x, y)
plt.plot(x, "or")
plt.plot(y, "or")

# the X axis lable
plt.xlabel('x - axis')

# the Y axis lable
plt.ylabel('y - axis')

# tital the graph
plt.title('Matplotlib Demo! ')

plt.plot(list(range(10, 87, 4)))
plt.plot(list(range(30, 57, 4)))

# the x-axis should start from 0 and go up to 90 with a difference of 5 value
plt.xticks(list(range(1, 150, 5)))
plt.yticks(list(range(1, 120, 15)))

axes = plt.gca()
axes.legend(['Series 1', 'Series 2'])
plt.figure(figsize=(10, 10))
# show the graph
plt.show()

# display the 2 line in same graph
# each line must be diff color

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.xticks(list(range(1, 100, 5)))
plt.yticks(list(range(1, 5, 9)))

x1 = [10, 9, 29, 79, 92]
y1 = [1, 30, 20, 15, 40]

plt.plot(x1, y1, label="Line-1", color="blue", linewidth=3, linestyle="dashed", markerfacecolor="black",
         markersize="10")

x1 = [29, 39, 79, 20, 82]
y1 = [40, 20, 30, 15, 10]

plt.plot(x1, y1, label="Line-2", color="black")

plt.legend()
plt.show()

# display the avg temp of the months

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
avg_temp = [19, 18, 17, 16, 15, 14, 13, 12, 11, 20, 21, 22]
months_name = ["jan", "feb", "mar", "apr", "may", "june", "july", "aug", "sep", "oct", "nov", "dec"]
plt.xlabel("Months")
plt.ylabel("Avg_temp")
plt.title("Temperature Recordings [2021] ")
plt.plot(months, avg_temp, label=months_name)
plt.bar(months, avg_temp, tick_label=months_name)
plt.scatter(months, avg_temp, label=months_name, marker="s", s=30, color="green")
plt.show()
