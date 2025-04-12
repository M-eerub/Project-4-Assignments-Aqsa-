# Dictionary containing the percentage gravity for each planet
planet_gravity = {
    "Mercury": 37.6,
    "Venus": 88.9,
    "Mars": 37.8,
    "Jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 81.5,
    "Neptune": 114.0
}

def main():
    # Ask the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Ask the user for the planet name
    planet = input("Enter a planet: ")

    # Check if the entered planet is in the dictionary
    if planet in planet_gravity:
        # Calculate the weight on the selected planet
        planet_weight = earth_weight * (planet_gravity[planet] / 100)
        
        # Print the result rounded to 2 decimal places
        print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")
    else:
        # If the planet is not in the dictionary, print a message
        print("Sorry, the planet you entered is not recognized.")

if __name__ == "__main__":
    main()
