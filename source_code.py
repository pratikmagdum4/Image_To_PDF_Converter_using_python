import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

def images_to_pdf(images, pdf_name):
    try:
        # create a new pdf file
        pdf = Image.open(images[0])
        pdf.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
        messagebox.showinfo("Success", "Images have been successfully converted to PDF.")
    except Exception as e:
        messagebox.showerror("Error", "Failed to convert images to PDF.\nError: " + str(e))

def select_images():
    images = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")),
        initialdir="C:/"
    )
    return images

def select_pdf():
    pdf = filedialog.asksaveasfilename(
        title="Save PDF As",
        defaultextension=".pdf",
        initialdir="C:/",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
    )
    return pdf

def create_ui():
    root = tk.Tk()
    root.title("Convert Images to PDF")

    # Customize the style of the buttons
    button_style = {
        'font': ('Arial', 12),
        'width': 20,
        'height': 2,
        'bg': 'lightblue',
        'fg': 'black',
        'activebackground': 'darkblue',
        'activeforeground': 'white'
    }

    # Create a frame for the buttons
    button_frame = tk.Frame(root, padx=20, pady=20)

    # Select Images button
    select_images_btn = tk.Button(
        button_frame,
        text="Select Images",
        command=select_images,
        **button_style
    )
    select_images_btn.pack(pady=10)

    # Select PDF button
    select_pdf_btn = tk.Button(
        button_frame,
        text="Select PDF",
        command=select_pdf,
        **button_style
    )
    select_pdf_btn.pack(pady=10)

    # Convert button
    convert_btn = tk.Button(
        button_frame,
        text="Convert",
        command=lambda: images_to_pdf(select_images(), select_pdf()),
        **button_style
    )
    convert_btn.pack(pady=10)

    # Pack the button frame
    button_frame.pack()

    root.mainloop()

if __name__ == '__main__':
    create_ui()
