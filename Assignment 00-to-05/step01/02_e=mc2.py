# Speed of light constant
C = 299792458  # meters per second

while True:
    # User se input lena
    mass_input = input("Enter kilos of mass (or type 'exit' to stop): ")

    if mass_input.lower() == 'exit':
        print("Goodbye!")
        break

    try:
        # Mass ko float me convert karna
        m = float(mass_input)

        # Energy calculate karna
        E = m * C**2

        # Output dikhana
        print("\ne = m * C^2...")
        print("m =", m, "kg")
        print("C =", C, "m/s")
        print(f"{E} joules of energy!\n")

    except ValueError:
        print("Please enter a valid number for mass.\n")
