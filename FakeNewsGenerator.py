import random

subjects=[
    "Shahrukh khan",
    "Virat Kohli",
    "Nirmala Sitharamn",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions=[
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "celebrates"       
]

places_or_things =[
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "at India Gate"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing=random.choice(places_or_things)

    headline=f"BREAKINGNEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\n Do you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

print("\n Thanks for using the Fake News Headline Generator.Have a fun day")
        
