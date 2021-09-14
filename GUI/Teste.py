from tkinter import *

from controllers.TasksController import TasksController
from controllers.UserController import UserController

from pages.loginPage import LoginPage
from pages.todoPage import TodoPage


tasksController = TasksController()
userController = UserController()

window = Tk()

window.geometry("862x519")
window.configure(bg = "#D8E0F7")
window.title("To-do List")

todoPage = TodoPage(window)
loginPage = LoginPage(window, todoPage)

todoPage.pack(fill='both', expand=1)

window.resizable(False, False)
window.mainloop()