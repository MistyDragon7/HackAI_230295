#   Importing necessary libraries
from uagents import Agent
from tkinter import *
from agents.tempy.tempy import tempy as tempy_agent         # Importing the uAgent that will send alerts
from agents.plot_data.plot_data import plot_data as plot_agent         # Importing the uAgent that will plot

#   Defining the TKinter Window
window = Tk()
window.title("Temperature alert bot")
window.configure(bg="yellow")
label = Label(window, text = '''Welcome to Tempy, the temperature alert bot!! Please choose from options given: ''', font = ('Comic Sans MS', 12), bg = 'yellow')
label.grid(column = 1, row = 0)
#   Defining the function to initialise a temperature alert.
def get_temp_alerts(event):
    if __name__ == "__main__":
        tempy_agent.run()
#Tkinter buttons continued
button1 = Button(window, text = "Set a new Temperature Alert", font = ("Comic Sans MS", 12), relief = "groove", bg = "black", fg = "white")
button1.bind("<Button-1>", get_temp_alerts)
button1.grid(column = 0, row = 1)

def plot_data_matplotlib(event):
    if __name__ == "__main__":
        plot_agent.run()
        
button2 = Button(window, text = "Plot old temperature data", font = ("Comic Sans MS", 12), relief = "groove", bg = "black", fg = "white")
button2.bind("<Button-1>", plot_data_matplotlib)
button2.grid(column = 6, row = 1)

window.mainloop()

