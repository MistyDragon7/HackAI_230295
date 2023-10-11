import tkinter as tk
import matplotlib.pyplot as plt
from uagents import Agent, Context
import pandas as pd
import mysql.connector
from dotenv import load_dotenv, find_dotenv
import os
from tkinter import StringVar
#Defining MySQL connection
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(*query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


#Loading envuronment variables file
load_dotenv(find_dotenv())

#   Fetching data from MySQL to Python
plot_data = Agent(name = 'plot_data', seed = 'data_visualisation')
@plot_data.on_interval(period = 300.0)
async def visualise_data(ctx: Context):
    #Connecting to database
    database_pass = os.getenv("DATABASE_PASS")
    connection = create_db_connection("localhost", "root", database_pass, "tempy")
    my_cursor = connection.cursor()
    #   Getting city as input
    city = city_var.get()
    #Obtaining data to plot
    query = "SELECT DateTime, Temperature FROM temperature_data WHERE Location=%s"
    df = pd.read_sql(query, connection, params=(city,))
    df['DateTime'] = pd.to_datetime(df['DateTime'])
    
    #   Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df['DateTime'], df['Temperature'])
    plt.gcf().autofmt_xdate()  # Auto-format the x-axis for date-time values
    plt.xlabel('Datetime')
    plt.ylabel('Temperature')
    plt.title('Temperature over Time')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    #Closing the connections
    my_cursor.close()
    connection.close()

def plot_data_func():
    plot_data.run()

window = tk.Tk()
window.title("Temperature Data Plotter")
window.configure(bg="yellow")
city_var = StringVar()

tk.Label(window, text="Enter City:", font = ("Comic Sans MS", 12), bg = "yellow").grid(row=0, column=0)
tk.Entry(window, textvariable=city_var).grid(row=0, column=3)

tk.Button(window, text="Plot Data", font = ("Comic Sans MS", 12), bg = "yellow", command=plot_data_func).grid(row=4, columnspan=2)
window.mainloop()
