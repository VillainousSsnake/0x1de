# /App/GUI/main_menu.py
# Contains main menu code


# Importing modules and libraries:
from App.AppLib.updater import Updater
import customtkinter as ctk


# main_menu function
def main_menu(app):

    # Creating root window
    root = ctk.CTk()
    root.title("0x1de - " + Updater.get_current_client_version() + " - Main Menu")
    root.geometry("850x525+200+200")

    # Defining on_close function
    def on_close():
        root.destroy()
        app.returnStatement = "exit"

    # Assigning the buttons on the tkinter window top bar
    root.protocol("WM_DELETE_WINDOW", on_close)

    # TODO: Code goes here

    # Root mainloop
    root.mainloop()
