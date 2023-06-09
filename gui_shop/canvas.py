from tkinter import Tk, Canvas

def create_root():
    root = Tk()

    root.title("Lemon Soda")
    root.geometry("1000x700")
    root.resizable(False, False)

    return root


def create_frame():
    frame = Canvas(root, width=1000, height=1000, bg="grey")
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()




