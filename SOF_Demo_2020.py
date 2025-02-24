import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from collections import defaultdict, Counter
import csv
import os
import sys

"""
Most Common Programming, Scripting and
Markup Languages that Devs opt to work
with next year
"""
with open("D:\Open Classroom\StackOverflow Dev Survey\developer_survey_2020\survey_results_public.csv", encoding = "utf-8")as file:
    fileReader = csv.DictReader(file)

    fileCounter = Counter()
    total = 0

    for line in fileReader:
        languages = line["LanguageDesireNextYear"].split(";")
        
        for language in languages:
            fileCounter[language] += 1
            total += 1

for lang, val in fileCounter.most_common(5):
    fileCounter.update(languages)
    
    langPercentage = (val / total) * 100
    langPercentage = round(langPercentage, 2)
    print(f"{lang}: {langPercentage}")

    
print(f"{lang}:{val}")
print(fileCounter.most_common(5))

   
"""
Most Common Programming, Scripting and
Markup Languages that Devs haved worked
with over the previous years
"""
with open("D:\Open Classroom\StackOverflow Dev Survey\developer_survey_2020\survey_results_public.csv", encoding = "utf-8")as file:
    previousFile = csv.DictReader(file)

    langDict = defaultdict(int)

    for line in previousFile:
        language = line["LanguageWorkedWith"].split(";")

        for lang in language:
            langDict[lang] += 1

print(langDict.get("JavaScript", "Python"))

"""
NEWStuck - What do you do when you get stuck on a problem?
"""
with open("D:\Open Classroom\StackOverflow Dev Survey\developer_survey_2020\survey_results_public.csv", encoding = "utf-8")as stuck:
    stuckReader = csv.DictReader(stuck)

    stuckCounter = Counter()

    for line in stuckReader:
        problemStuck = line["NEWStuck"].split(";")

        for prob in problemStuck:
            stuckCounter[prob] += 1

print(stuckCounter)
            
            
