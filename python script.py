import pandas as pd
import matplotlib.pyplot as plt
import numpy 
import os
import csv
from collections import defaultdict, Counter

with open("D:\Open Classroom\StackOverflow Dev Survey\developer_survey_2019\survey_results_public.csv", encoding = "utf-8") as file:
	reader = csv.DictReader(file)

	counter = Counter()

	for line in reader:
		counter.update(line["LanguageWorkedWith"].split(";"))
#print(counter.most_common(5))
language = []
popularity = []

for count in counter.most_common(15):
	language.append(count[0])
	popularity.append(count[1])
language.reverse()
popularity.reverse()
plt.barh(language, popularity, label = "Popularity")
plt.title("Language Response by Popularity")
plt.legend(loc = "best")
plt.show()
print(language, popularity)
