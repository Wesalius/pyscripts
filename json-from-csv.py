import csv
import json

mydict = dict()
with open("example.csv", "r") as csvfile:
    fieldnames = ("fide id", "rating")
    reader = csv.DictReader(csvfile, fieldnames, delimiter=",")
    for row in reader:
        mydict[row["fide id"]] = row["rating"]

with open("output.json", "w") as jsonfile:
    json.dump(mydict, jsonfile, indent=4)

# Example.csv with first column of fide ids and second column of ratings
#    1503014,2857
#    623539,2819
#    4100018,2812
#    4101588,2808
#    2020009,2807
#    13300474,2792
#    2016192,2791
#    5202213,2771
#    5000017,2770
#    24116068,2769
#    14109603,2769
#    13401319,2764
#    2900084,2761
#    8603677,2755
#    4126025,2754
#    8604436,2753
#    5007003,2752
#    738590,2752
#    4102142,2751
