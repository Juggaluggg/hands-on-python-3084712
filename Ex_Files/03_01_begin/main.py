import csv
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

with open("laureates.csv", "r") as f: #Opens the file in read mode 
    reader = csv.DictReader(f) #Reads file 
    laureates = list(reader) #Creates a list of from file 

for laureate in laureates: #Looks for in field of the filename  
    if laureate["surname"] == "Einstein": # surname field for Einstein
        pprint(laureate) #pretty prints the data in JSON format
        break
