import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageDraw

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")
        
        self.canvas = Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack()
        
        self.color = "black"  # Default color
        self.create_color_palette()
        
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(fill=tk.X)
        
        self.save_button = tk.Button(root, text="Save", command=self.save_canvas)
        self.save_button.pack(fill=tk.X)
        
        self.canvas.bind("<B1-Motion>", self.paint)
        
        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)
    
    def create_color_palette(self):
        self.palette_frame = tk.Frame(self.root)
        self.palette_frame.pack(fill=tk.X)
        
        colors = ["black", "red", "green", "blue", "yellow", "purple", "orange", "brown"]
        
        for color in colors:
            btn = tk.Button(self.palette_frame, bg=color, width=4, height=2, command=lambda c=color: self.set_color(c))
            btn.pack(side=tk.LEFT, padx=2, pady=2)
    
    def set_color(self, new_color):
        self.color = new_color
    
    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
        self.draw.ellipse([x1, y1, x2, y2], fill=self.color, outline=self.color)
    
    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)
    
    def save_canvas(self):
        self.image.save("drawing.png")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
