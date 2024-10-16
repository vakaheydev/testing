from utils import *


# 1
def test_average_grades():
    actual = calculate_grades_averages()
    expected = [78.25, 48.0, 44.0, 47.0, 45.0, 46.0, 43.0, 50.0, 83.0, 97.0, 40.0, 45.0, 77.0, 90.0, 4.0, 40.0]

    for i in range(len(actual)):
        if actual[i] != expected[i]:
            print(f'Wrong value: actual {actual[i]} | expected {expected[i]}')
        else:
            print(f'Correct: {actual[i]}')

    assert actual == expected


# 2
def test_get_json():
    actual = get_json_from_file("SuperHero.json")
    expected = {'squadName': 'Super hero squad', 'homeTown': 'Metro City', 'formed': 2016, 'secretBase': 'Super tower', 'active': True, 'members': [{'name': 'Molecule Man', 'age': 29, 'secretIdentity': 'Dan Jukes', 'powers': ['Radiation resistance', 'Turning tiny', 'Radiation blast']}, {'name': 'Madame Uppercut', 'age': 39, 'secretIdentity': 'Jane Wilson', 'powers': ['Million tonne punch', 'Damage resistance', 'Superhuman reflexes']}, {'name': 'Eternal Flame', 'age': 1000000, 'secretIdentity': 'Unknown', 'powers': ['Immortality', 'Heat Immunity', 'Inferno', 'Teleportation', 'Interdimensional travel']}]}

    assert actual == expected


def test_add_json():
    add_json_to_file()
    actual = get_json_from_file("../superhero_new.json")
    expected = {"squadName": "Super hero squad", "homeTown": "Metro City", "formed": 2016, "secretBase": "Super tower", "active": True, "members": [{"name": "Molecule Man", "age": 29, "secretIdentity": "Dan Jukes", "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]}, {"name": "Madame Uppercut", "age": 39, "secretIdentity": "Jane Wilson", "powers": ["Million tonne punch", "Damage resistance", "Superhuman reflexes"]}, {"name": "Eternal Flame", "age": 1000000, "secretIdentity": "Unknown", "powers": ["Immortality", "Heat Immunity", "Inferno", "Teleportation", "Interdimensional travel"]}, {"name": "Ant Man", "age": 36, "secretIdentity": "Cool Guy", "powers": ["Size mutation", "Super strength"]}, {"name": "Spider Man", "age": 16, "secretIdentity": "Peter Parker", "powers": ["Web Shooting", "Walking on walls"]}]}

    assert actual == expected


def test_sort_json():
    sort_json()
    actual = get_json_from_file("../superhero_new.json")
    expected = {"squadName": "Super hero squad", "homeTown": "Metro City", "formed": 2016, "secretBase": "Super tower", "active": True, "members": [{"name": "Spider Man", "age": 16, "secretIdentity": "Peter Parker", "powers": ["Web Shooting", "Walking on walls"]}, {"name": "Molecule Man", "age": 29, "secretIdentity": "Dan Jukes", "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]}, {"name": "Ant Man", "age": 36, "secretIdentity": "Cool Guy", "powers": ["Size mutation", "Super strength"]}, {"name": "Madame Uppercut", "age": 39, "secretIdentity": "Jane Wilson", "powers": ["Million tonne punch", "Damage resistance", "Superhuman reflexes"]}, {"name": "Eternal Flame", "age": 1000000, "secretIdentity": "Unknown", "powers": ["Immortality", "Heat Immunity", "Inferno", "Teleportation", "Interdimensional travel"]}]}

    assert actual == expected
