import requests

response = requests.get("http://checklight.pythonanywhere.com/streets")


data = response.json()
streets_list = data["streets"]

# for streets in streets_list:
#     print(streets["name"].ljust(25),"|",streets["state"].ljust(6), "|", streets["status"], "|",streets["avg_power"])


adenuga = streets_list[13]["history"]
adenuga_timeline = adenuga['time_line']

for timeline in adenuga_timeline:

    if timeline["status"] == 1:
        print(timeline["time"], "|", "ON")

    elif timeline["status"] == 0:
        print(timeline["time"], "|", "OFF")
