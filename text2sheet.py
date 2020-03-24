import pandas as pd

text_file = open("vocab_schedule_date_view.txt", "r").readlines()

filtered = list(filter(lambda a: a != "\n", text_file))
filtered = [i.replace("\n", "") for i in filtered]
#print(filtered)

days = []
day_count = 0
for i in filtered:
    if "/" in i:
        days.append([])
        days[-1].append(i)
    else:
        days[-1].append(i)

dates = []
days_sorted = []
for i in days:
    dates.append(i[0])
    days_sorted.append(sorted(i[1:], key=lambda x: x[-1]))


days_processed = []
for i in days_sorted:
    if i[0][-1] == "2":
        days_processed.append(["nan"] + i)
    elif i[0][-1] == "3":
        days_processed.append(["nan", "nan"] + i)
    elif i[0][-1] == "4":
        days_processed.append(["nan", "nan", "nan"] + i)
    elif i[0][-1] == "5":
        days_processed.append(["nan", "nan", "nan", "nan"] + i)
    else:
        days_processed.append(i)

days_processed = [[dates[i]] + days_processed[i] for i in range(len(days_processed))]
print(days_processed)

# longest = len(max(days, key=len))

# for i in days:
#     while len(i) < longest:
#         i.append("nan")


sheet = open("sheet_view.csv", "w+")
for i in days_processed:
    for j in range(len(i)):
        if j == len(i) - 1:
            sheet.write(i[j])
        else:
            sheet.write(i[j] + ",")
    sheet.write("\n")

# sheet.close()

# df = pd.read_csv("sheet_view.csv")
# df.to_excel("sheet.xlsx", header=["Date", "Review 1", "Review 2", "Review 3", "Review 4", "Review 5"])