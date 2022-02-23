import matplotlib.pyplot as plt

'''x=[1,2,3]
y=[1,2,3]
plt.plot(x,y,marker='o')
plt.figure(figsize=(12,19))
#x-axis values
x=[1,2,3]
#corresponding values for y-axis
y=[20,10,14]
#plotting the points
#plt.plot(x,y)
#plt.plot(x,"or")#it plots (0-1,1-2,2-3)
#plt.plot(x,marker='o')
#plt.plot(y)#it plots (0-20,1-10,2-14)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Matplotlib-demo")
#x-axis should start from 1 till 150 with a diifference of 5 values
plt.plot(list(range(30,57,4)),marker='o')
plt.xticks(list(range(1,150,5)))
plt.yticks(list(range(1,120,15)))
axes=plt.gca()
axes.legend(['series1'])
#show graph/plot
plt.show()'''

# display two lines on same graph. Each line must be of different color
plt.xlabel("x-axis")
plt.ylabel("y-axis")
x1 = [19, 2, 15, 40, 23]
y1 = [9, 5, 8, 30, 35]
plt.xticks(list(range(1, 50, 5)))
plt.yticks(list(range(1, 50, 5)))
plt.plot(x1, y1, marker="s", label="Line1", linestyle="dashed", color="green", markerfacecolor="black", markersize=5)

x1 = [29, 39, 45, 20, 33]
y1 = [40, 20, 30, 15, 10]
plt.plot(x1, y1, marker="o", label="Line2", linestyle="dotted", linewidth=2, markerfacecolor="black", markersize=5)
axes = plt.gca()
axes.legend()
plt.show()
