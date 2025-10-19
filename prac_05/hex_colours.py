"""
CP1404/CP5632 Practical
Colour names in a dictionary
"""

COLOUR_TO_NAME = {"bananayellow": "#ffe135",
                "babyblue": "#89cff0",
                "apricot": "#fbceb1",
                "boysenberry": "#873260",
                "brightgreen": "#66ff00",
                "brilliantrose": "	#ff55a3",
                "bronze": "#cd7f32",
                "bubblegum": "#ffc1cc",
                "orange": "#ed872d"}

for colour in COLOUR_TO_NAME:
    print(f"{colour:15} is {COLOUR_TO_NAME[colour]}")

colour_code = input("Enter colour: ").lower()
while colour_code != "":
    try:
        print(f"{colour_code} is {COLOUR_TO_NAME[colour_code]}")
    except KeyError:
        print("Invalid colour code")

    colour_code = input("Enter colour: ").lower()