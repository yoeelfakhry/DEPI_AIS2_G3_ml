import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Attempt to import prediction function
try:
    from predictor import predict_price
except ImportError:
    def predict_price(rm, lstat, ptratio):
        # Dummy logic for standalone testing
        return (rm * 50) - (lstat * 2) - (ptratio * 5)

# --- MODERN COLOR PALETTE ---
BG_MAIN = "#121826"        # Dark Slate
BG_SECONDARY = "#1f2937"   # Lighter Slate for inputs
ACCENT = "#00dfc8"         # Vibrant Cyan
ACCENT_HOVER = "#00f0d8"   # Brighter Cyan for hover
TEXT_PRIMARY = "#f9fafb"   # White
TEXT_SECONDARY = "#9ca3af" # Muted Gray

class HousingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Housing Intelligence System")
        self.geometry("900x600")
        self.configure(bg=BG_MAIN)
        self.resizable(False, False)

        container = tk.Frame(self, bg=BG_MAIN)
        container.pack(fill="both", expand=True)
        
        self.frames = {}
        for Page in (HomePage, PriceEstimatorPage):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page):
        self.frames[page].tkraise()

# --- HELPER FOR HOVER EFFECTS ---
def on_enter(e, color):
    e.widget['background'] = color

def on_leave(e, color):
    e.widget['background'] = color

# ---------------- HOME PAGE ---------------- #
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_MAIN)

        # Main horizontal container
        content = tk.Frame(self, bg=BG_MAIN)
        content.pack(fill="both", expand=True, padx=60, pady=40)

        # Configure grid (2 columns)
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)

        # ---------------- LEFT SIDE (TEXT) ---------------- #
        text_frame = tk.Frame(content, bg=BG_MAIN)
        text_frame.grid(row=0, column=0, sticky="nsew", padx=(0,40))

        title = tk.Label(
            text_frame,
            text="Boston Housing Intelligence",
            font=("Segoe UI", 28, "bold"),
            fg=TEXT_PRIMARY,
            bg=BG_MAIN,
            anchor="w",
            justify="left"
        )
        title.pack(anchor="w", pady=(0,20))

        description = tk.Label(
            text_frame,
            text=(
                "This system applies a Decision Tree Regression model trained\n"
                "on the Boston Housing dataset to estimate real estate value\n"
                "based on structural and socio-economic indicators.\n\n"

                "The model analyzes how factors such as:\n"
                "• Average number of rooms (RM)\n"
                "• Neighborhood economic status (LSTAT)\n"
                "• Education resource ratio (PTRATIO)\n\n"

                "interact non-linearly to influence housing prices.\n\n"

                "Unlike linear models, Decision Trees capture complex\n"
                "relationships and threshold effects, enabling interpretable\n"
                "and realistic valuation predictions."
            ),
            font=("Segoe UI", 11),
            fg=TEXT_SECONDARY,
            bg=BG_MAIN,
            justify="left",
            wraplength=420
        )
        description.pack(anchor="w")

        start_btn = tk.Button(
            text_frame,
            text="Launch Estimator",
            bg=ACCENT,
            fg=BG_MAIN,
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            bd=0,
            padx=20,
            pady=12,
            cursor="hand2",
            command=lambda: controller.show_frame(PriceEstimatorPage)
        )
        start_btn.pack(anchor="w", pady=50)
        start_btn.place(relx=0.5, rely=0.95, anchor="center")
        start_btn.bind("<Enter>", lambda e: on_enter(e, ACCENT_HOVER))
        start_btn.bind("<Leave>", lambda e: on_leave(e, ACCENT))

        # ---------------- RIGHT SIDE (IMAGE) ---------------- #
        image_frame = tk.Frame(content, bg=BG_MAIN)
        image_frame.grid(row=0, column=1, sticky="nsew")

        # Load and resize image
        img = Image.open("boston_image.jpg")
        img = img.resize((400, 450 ))  # adjust size as needed
        self.photo = ImageTk.PhotoImage(img)

        image_label = tk.Label(
            image_frame,
            image=self.photo,
            bg=BG_MAIN
        )
        image_label.pack(expand=True)

# ---------------- PREDICTION PAGE ---------------- #
class PriceEstimatorPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_MAIN)

        tk.Label(
            self, text="House Price Estimator",
            font=("Segoe UI", 22, "bold"), fg=TEXT_PRIMARY, bg=BG_MAIN
        ).pack(pady=30)

        self.input_container = tk.Frame(self, bg=BG_MAIN)
        self.input_container.pack(pady=10)

        self.rm_entry = self.create_input("RM (Avg Rooms per Dwelling)")
        self.lstat_entry = self.create_input("LSTAT (% Lower Status Population)")
        self.ptratio_entry = self.create_input("PTRATIO (Student-Teacher Ratio)")

        predict_btn = tk.Button(
            self, text="Calculate Estimation", font=("Segoe UI", 12, "bold"),
            bg=ACCENT, fg=BG_MAIN, relief="flat", bd=0, width=25, pady=10,
            cursor="hand2", command=self.predict
        )
        predict_btn.pack(pady=25)
        predict_btn.bind("<Enter>", lambda e: on_enter(e, ACCENT_HOVER))
        predict_btn.bind("<Leave>", lambda e: on_leave(e, ACCENT))

        self.result_label = tk.Label(
            self, text="", font=("Segoe UI", 18, "bold"), 
            fg=ACCENT, bg=BG_MAIN
        )
        self.result_label.pack(pady=10)

        back_btn = tk.Button(
            self, text="← Back to Home", font=("Segoe UI", 10),
            bg=BG_MAIN, fg=TEXT_SECONDARY, relief="flat", bd=0,
            activebackground=BG_MAIN, activeforeground=TEXT_PRIMARY,
            cursor="hand2", command=lambda: controller.show_frame(HomePage)
        )
        back_btn.pack(side="bottom", pady=40)

    def create_input(self, label_text):
        frame = tk.Frame(self.input_container, bg=BG_MAIN)
        frame.pack(pady=10)

        tk.Label(
            frame, text=label_text, width=32, anchor="w",
            font=("Segoe UI", 10), fg=TEXT_SECONDARY, bg=BG_MAIN
        ).pack(side="left")

        entry = tk.Entry(
            frame, width=20, font=("Segoe UI", 12),
            bg=BG_SECONDARY, fg=TEXT_PRIMARY,
            insertbackground=TEXT_PRIMARY, relief="flat"
        )
        entry.pack(side="left", padx=10, ipady=4) # ipady adds internal vertical padding
        return entry

    def predict(self):
        try:
            rm = float(self.rm_entry.get())
            lstat = float(self.lstat_entry.get())
            ptratio = float(self.ptratio_entry.get())
            price = predict_price(rm, lstat, ptratio)
            self.result_label.config(text=f"Estimated Market Value: ${price:,.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

if __name__ == "__main__":
    app = HousingApp()
    app.mainloop()

