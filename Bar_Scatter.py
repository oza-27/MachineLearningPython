import matplotlib.pyplot as plt
#display average temperature of each month
months=[1,2,3,4,5,6,7,8,9,10,11,12]
avg_temp=[15,20,34,40,56,35,32,39,32,30,29,20]
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.title("Temperature Recordings 2021")
labels=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
#plt.plot(months,avg_temp,label=labels)
#plt.bar(months,avg_temp,tick_label=labels,color="red",width=0.7)
plt.scatter(months,avg_temp,marker="s",color="green",s=20)
plt.show()