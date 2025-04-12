# Countdown program for spaceship launch

def countdown():
    # 10 se 1 tak reverse order me numbers print karne ke liye range ka use
    for i in range(10, 0, -1):  # 10 se shuru, 0 tak jao, -1 ka step
        print(i, end=" ")       # Saath me space ke saath same line me print

    # Countdown ke baad Liftoff! print karein
    print("Liftoff!")

# Function call
countdown()
