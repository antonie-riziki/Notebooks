import csv

##with open("D:\Open Classroom\StackOverflow Dev Survey\developer_survey_2019\survey_results_public.csv") as file:
##    reader = csv.DictReader(file)
####    for line in reader:
####        print(line)
####        break
##    yesCount = 0
##    noCount = 0
##
##    for i in reader:
##        if i["Hobbyist"] == "Yes":
##            yesCount += 1
##        elif i["Hobbyist"] == "No":
##            noCount += 1
##
##print("Yes: ", yesCount)
##print("No: ", noCount)


with open ("D:\Open Classroom\StackOverflow Dev Survey\developer_survey_2019\survey_results_public.csv", encoding = "utf-8") as f:
    reader = csv.reader(f)
    for i in reader:
        print(i[2])
        break
