from tkinter import *

from controllers.tasks_controller import TasksController
from controllers.user_controller import UserController

from pages.login_page import LoginPage
from pages.todo_page import TodoPage

tasks_controller = TasksController()
user_controller = UserController()

window = Tk()

window.geometry("862x519")
window.configure(bg = "#D8E0F7")
window.title("To-do List")

todo_page = TodoPage(window)
login_page = LoginPage(window, todo_page)

login_page.pack(fill = 'both', expand = 1)

window.resizable(False, False)
window.mainloop()