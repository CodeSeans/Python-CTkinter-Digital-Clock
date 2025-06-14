import customtkinter as ctk
import tkinter as tk
from time import strftime
from PIL import Image, ImageTk
from customtkinter import CTkImage

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class DigitalClockApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CustomTkinter Dijital Saat")
        self.geometry("480x270")
        self.resizable(False,False)
        
        
       # Tkinter Canvas arka plan için (image gösteriyor)
        self.canvas = tk.Canvas(self, width=500, height=200, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Pillow ile resmi aç ve Tkinter uyumlu yap
        self.bg_image_pil = Image.open("world.webp")
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image_pil)

        # Canvas'a arka plan resmi olarak ekle
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor="nw")

        self.normal_color = "lime"
        self.flash_color = "white"
        
        self.clock_label = ctk.CTkLabel(
            self,
            text="",
            font=ctk.CTkFont(family="Courier", size=48, weight="bold"),
            text_color=self.normal_color,
        )

        # canvas'ı pack ettik onun üzerine place ile label yerleştir
        self.clock_label.place(relx=0.5, rely=0.5, anchor="center")

        self.update_time() # şu anki zamanı alıyor
        
    def update_time(self):
        current_time = strftime("%H:%M:%S")
        self.clock_label.configure(text=current_time, text_color=self.flash_color)
        self.after(200, lambda: self.clock_label.configure(text_color=self.normal_color))
        self.after(1000, self.update_time)

if __name__ == "__main__":
    app = DigitalClockApp()
    app.mainloop()
