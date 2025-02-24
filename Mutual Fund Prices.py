import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

sb.set()
plt.style.use("bmh")
numberOfFunds = [0, 6, 11, 9, 7, 5, 2]
mutualFundPrice = np.linspace(0, 40, 7)
plt.rcParams.update({"font.size": 15})
plt.plot(mutualFundPrice, numberOfFunds, color = "cyan", label = "No. of Funds")
plt.title("Mutual Fund Price")
x = plt.axes()
x.set(xlabel = "Mutual Fund Price", ylabel = "No. of Funds")
plt.legend(loc = "best")
#sb.distplot(mutualFundPrice, kde = True)

numberOfFundsBarChart = [0, 6, 11, 9, 7, 5, 2]
plt.bar(mutualFundPrice, numberOfFundsBarChart, color = "black", label = "No. of Funds", width = 6.0, data = numberOfFundsBarChart)
plt.legend(loc = "best")
sb.distplot(numberOfFundsBarChart, kde = True)
#plt.axis([0, 45, 0, 12])
#print(help(plt.rcParams.update()))
plt.show()


sb.set()
x = np.linspace(0, 10, 500)
y = np.random.randn(500)
plt.plot(x,y)
plt.show()

#Visualizing the relationship between variables using .pairplot function
iris = sb.load_dataset("iris")
iris.head()
sb.pairplot(iris, hue='species', height=2.5)
plt.show()

#Joining Distribution of 2 characteristics
with sb.axes_style('white'):
    sb.jointplot("petal_length", "petal_width", data=iris, kind='reg')
    #plt.show()
