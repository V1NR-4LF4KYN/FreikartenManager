import json
def addJson():
  anna = {
    "name": "Anna",
    "folge": 0,
    "freikarten": 0,
    "youtube": 0,
    "einmal_aufstehen": 0,
    "massage": 0,
    "sklave": 0,
    "striptease": 0,
    "hasssache": 0, 
  }
  james = {
    "name": "James",
    "folge": 0,
    "freikarten": 0,
    "youtube": 0,
    "einmal_aufstehen": 0,
    "massage": 0,
    "sklave": 0,
    "striptease": 0,
    "hasssache": 0, 
  }

  # turning python into readable json
  data_anna = json.dumps(anna, indent=2)
  data_james = json.dumps(james, indent=2)

  # adding json for james data
  with open("data_james.json", "a") as file:
    file.write(data_james)

  # adding json for annas data
  with open("data_anna.json", "a") as file:
    file.write(data_anna)