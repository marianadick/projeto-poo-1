import tkinter as tk
import page2
import page1

class Page(tk.Frame):
  def __init__(self, *args, **kwargs):
    tk.Frame.__init__(self, *args, **kwargs)
  # def show(self):
  #   self.lift()

class MainView(tk.Frame):
  def __init__(self, *args, **kwargs):
    tk.Frame.__init__(self, *args, **kwargs)
    initial = page2.Page2(self)
    todo = page1.Page1(self)

    buttonframe = tk.Frame(self)
    container = tk.Frame(self)
    buttonframe.pack(side="top", fill="x", expand=False)
    container.pack(side="top", fill="both", expand=True)

    initial.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    todo.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

    initial.tkraise()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("862x519")
    root.title("To-do List")
    root.configure(bg = "#D8E0F7")
    root.mainloop()