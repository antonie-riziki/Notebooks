import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb

hostelWorkersList = [[500, "Patrick", "Red", 44, 22000, 7],
                     [510, "Dolly", "Blue", 30, 45000, 15],
                     [520, "Sindy", "Orange", 35, 26000, 10],
                     [530, "Lucy", "Green", 20, 44000, 12]]

hostelWorkersNumpy = np.array(hostelWorkersList)
print(hostelWorkersNumpy)
print("")

hostelWorkersPandas = pd.DataFrame(hostelWorkersNumpy, index = [1, 2, 3, 4], columns = ["ID", "NAME", "HOSTEL", "AGE", "SALARY", "SERVICE YEARS'"])
print(hostelWorkersPandas)
print("")

mask = hostelWorkersPandas["AGE"] == 0 
print(hostelWorkersPandas[mask])

hostelWorkersPandasSorted = np.sort(hostelWorkersPandas.SALARY)

newHostelDatabaseUpdate = pd.DataFrame([[540, "Shirlyne", "Yellow", 29, 38000, 9]],
                                       index = [5],
                                       columns = hostelWorkersPandas.columns)

newHostelDatabaseUpdate = hostelWorkersPandas.append(newHostelDatabaseUpdate)
print(newHostelDatabaseUpdate)

patrick = newHostelDatabaseUpdate.iloc[2]
print(patrick)

sb.set()
plt.style.use("bmh")
x = np.arange(0, 70000)
plt.bar(hostelWorkersPandas.NAME, hostelWorkersPandasSorted, color = "black", label = "Salary")
plt.title("HOSTEL WORKERS SALARY")
y = plt.axes()
y.set(xlabel = "WORKERS NAME", ylabel = "SALARY")
plt.legend(loc = "best")
plt.show()

plt.plot(hostelWorkersPandas.NAME, hostelWorkersPandas.SALARY)
plt.show()
