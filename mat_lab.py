# Mad Libs with Conditional Logic

weather = input("What's the weather like today (e.g., sunny, rainy, foggy)? ")
funny_moment = input("Enter a funny moment: ")
day_description = input("How was the day : ")

# Optional conditional message based on weather
if weather == "sunny":
    intro = "The sun was shining bright and it felt like a perfect day for an adventure!"
elif weather == "rainy":
    intro = "Despite the rain, I grabbed my umbrella and decided not to miss the fun!"
else:
    intro = f"The {weather} weather gave the day a mysterious twist."

# Story building
story = f""" {intro}
On a beautiful {weather} day, I went to the zoo.
the fun moment was {funny_moment} and the full experience was {day_description}. """

# Display the story
print(story)
