import matplotlib.pyplot as plt

# Display average temperature of each month
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
avg_temp = [15, 20, 34, 56, 67, 78, 89, 90, 91, 25, 69, 30]
plt.xlabel("Month")
plt.ylabel("Average Temperature")
plt.title("Temperature recordings 2021")
labels = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
plt.plot(months, avg_temp, label=labels)
plt.bar(months, avg_temp, tick_label=labels, color="red", width=0.7)
plt.show()
