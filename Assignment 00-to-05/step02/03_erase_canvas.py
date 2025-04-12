import tkinter as tk

# Canvas size
canvas_width = 500
canvas_height = 500

# Cell size
cell_size = 20

# Create the root window
root = tk.Tk()
root.title("Canvas Eraser")

# Create the canvas widget
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="blue")
canvas.pack()

# Create a 2D list to store the cell status (True = blue, False = white)
cells = [[True for _ in range(canvas_width // cell_size)] for _ in range(canvas_height // cell_size)]

# Function to draw the grid on the canvas
def draw_grid():
    for row in range(len(cells)):
        for col in range(len(cells[row])):
            color = "blue" if cells[row][col] else "white"
            canvas.create_rectangle(
                col * cell_size, row * cell_size,
                (col + 1) * cell_size, (row + 1) * cell_size,
                fill=color, outline="black"
            )

# Function to update cells based on the eraser's position
def erase(event):
    col = event.x // cell_size
    row = event.y // cell_size
    if 0 <= row < len(cells) and 0 <= col < len(cells[row]):
        cells[row][col] = False  # Set the cell to white
    draw_grid()

# Create an eraser rectangle that will track mouse drag
eraser = canvas.create_rectangle(0, 0, cell_size, cell_size, fill="white", outline="black")

# Update the position of the eraser on mouse drag
def move_eraser(event):
    canvas.coords(eraser, event.x - cell_size / 2, event.y - cell_size / 2,
                  event.x + cell_size / 2, event.y + cell_size / 2)
    erase(event)

# Bind mouse movement and dragging to the canvas
canvas.bind("<B1-Motion>", move_eraser)

# Initially draw the grid
draw_grid()

# Start the Tkinter main loop
root.mainloop()
