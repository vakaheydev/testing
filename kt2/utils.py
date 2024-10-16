import csv
import json


def calculate_grades_averages():
    averages_list = []
    with open("grades.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            try:
                average = sum(float(grade) for grade in row[3:7]) / 4
            except ValueError:
                continue

            averages_list.append(average)

    return averages_list


def get_json_from_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data

def add_json_to_file():
    hero = {
      "name": "Ant Man",
      "age": 36,
      "secretIdentity": "Cool Guy",
      "powers": ["Size mutation", "Super strength"]
    }
    hero2 = {
        "name": "Spider Man",
        "age": 16,
        "secretIdentity": "Peter Parker",
        "powers": ["Web Shooting", "Walking on walls"]
    }

    json_data = get_json_from_file("SuperHero.json")
    json_data['members'].append(hero)
    json_data['members'].append(hero2)

    with open("../superhero_new.json", "w") as file:
        file.writelines(json.dumps(json_data))


def sort_json():
    json_data = get_json_from_file("../superhero_new.json")
    members = json_data['members']
    members.sort(key = lambda x: x['age'])
    json_data['members'] = members
    with open("../superhero_new.json", "w") as file:
        file.writelines(json.dumps(json_data))
