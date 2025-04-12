# Constants for each planet's gravity relative to Earth's gravity
MARS_GRAVITY = 0.378
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Get the user's weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Ask the user to enter a planet
    planet = input("Enter a planet (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ")

    # Check which planet the user entered and calculate weight
    if planet == "Mercury":
        gravity = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity = VENUS_GRAVITY
    elif planet == "Mars":
        gravity = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity = NEPTUNE_GRAVITY
    else:
        # If the planet name is not valid
        print("Sorry, that's not a valid planet.")
        return

    # Calculate the weight on the chosen planet
    planet_weight = earth_weight * gravity

    # Round the result to two decimal places
    rounded_weight = round(planet_weight, 2)

    # Print the result
    print(f"The equivalent weight on {planet}: {rounded_weight}")

if __name__ == "__main__":
    main()
