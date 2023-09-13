import random
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import messagebox

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def random_uniform(min_val, max_val):
    return random.uniform(min_val, max_val)

def draw_shape(draw, x, y, size, color):
    sides = random.randint(3, 6)  # Random number of sides (3 to 6)
    angle = 360 / sides

    points = []
    for _ in range(sides):
        points.extend((x, y))
        x += size * 2 * random_uniform(0.7, 1.3)  # Randomize x
        y += size * 2 * random_uniform(0.7, 1.3)  # Randomize y
        points.extend((x, y))
        draw.polygon(points, fill=color, outline=color)

def draw_graffiti(draw, x, y, size, color):
    for _ in range(size):
        angle = random_uniform(0, 360)  # Randomize angle
        distance = random_uniform(1, 20)  # Randomize distance
        x2 = x + distance * random_uniform(0.7, 1.3) * angle  # Randomize x
        y2 = y + distance * random_uniform(0.7, 1.3) * angle  # Randomize y
        draw.line((x, y, x2, y2), fill=color, width=2)
        x, y = x2, y2

def generate_painted_canvas():
    canvas_size = 600  # Set the size of the canvas

    def generate():
        # Create a blank canvas
        canvas = Image.new("RGB", (canvas_size, canvas_size), "white")
        draw = ImageDraw.Draw(canvas)

        max_shapes = 1000  # Maximum number of shapes to generate
        shape_size = 30  # Size of the shapes
        grid_spacing = shape_size  # Spacing between shapes

        for x in range(0, canvas_size, grid_spacing):
            for y in range(0, canvas_size, grid_spacing):
                if max_shapes <= 0:
                    break

                size = random.randint(10, shape_size)  # Adjust the size range as desired
                color = random_color()

                draw_shape(draw, x, y, size, color)
                max_shapes -= 1

        print("The canvas is filled.")

        # Display the canvas in a popup window
        canvas.show()

        # Ask the user whether they want to save the file
        user_response = messagebox.askyesno("Save Art", "Do you want to save the art?")
        if user_response:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                canvas.save(file_path)
                print(f"Art exported as {file_path}")

    root = tk.Tk()
    root.title("Canvas Generation")

    generate_button = tk.Button(root, text="Generate", command=generate)
    generate_button.pack()

    root.mainloop()  # Start the tkinter main loop

if __name__ == "__main__":
    generate_painted_canvas()
