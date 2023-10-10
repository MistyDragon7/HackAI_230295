#importing necessary libraries
from uagents import Agent, Context
import json
from twilio.rest import Client as twilio_client
import requests
from dotenv import load_dotenv, find_dotenv
import os
import asyncio
import tkinter as tk
from tkinter import StringVar, IntVar
from datetime import datetime
import mysql.connector
from mysql.connector import Error

message_client = None
twilio_phone_number = None
delivery_phone_number = None

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

#Connecting to database
database_pass = os.getenv("DATABASE_PASS")
connection = create_db_connection("localhost", "root", database_pass, "tempy")

#   Defining the uAgent:

tempy = Agent(name = 'tempy', seed = 'main_bot')

@tempy.on_interval(period = 300.0)

async def get_temperature(ctx: Context):
    api_key = os.getenv("API_KEY")
    city = input("Enter city: ")
    weather_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=" + api_key
    data = requests.get(weather_url)
    weather_data = data.json()
    now = datetime.now()
    
    upper_limit = upper_limit_var.get()
    lower_limit = lower_limit_var.get()
    
    if data.status_code == 200:
        temperature = weather_data['main']['temp']
        temperature = int(temperature)
        ctx.logger.info(temperature)
        sql = """INSERT INTO temperature_data(
            Temperature, Location, Datetime)
            VALUES (%s, %s, %s);""", (temperature, city, now)
        execute_query(connection, sql)
        if temperature>upper_limit:
            ctx.logger.info("Temperature Too High!!!!")
            #   Initialising SMS message
            message = message_client.messages.create(
                from_= twilio_phone_number,
                body = "The upper threshold of temperature has been surpassed!!!!",
                to = delivery_phone_number
            )
            return

        elif temperature<lower_limit:
            ctx.logger.info("Temperature Too Low!!!!")

            message = message_client.messages.create(
                from_= twilio_phone_number,
                body = "The upper threshold of temperature has been surpassed!!!!",
                to = delivery_phone_number
            )
            return

    else:
        print(f"Error: {weather_data['message']}")
        return

def start_monitoring():
    global message_client, twilio_phone_number, delivery_phone_number#, city
    
    #   Importing environment variables
    twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
    delivery_phone_number = phone_number_var.get()
    #city = city_var.get()
    message_client = twilio_client(twilio_account_sid, twilio_auth_token)

    tempy.run()

window = tk.Tk()
window.title("Temperature Alert Agent")
window.configure(bg="yellow")


city_var = StringVar()
phone_number_var = StringVar()
upper_limit_var = IntVar()
lower_limit_var = IntVar()

# Main TKinter window
tk.Label(window, text="Enter City:", font = ("Comic Sans MS", 12), bg = "yellow").grid(row=0, column=0)
tk.Entry(window, textvariable=city_var).grid(row=0, column=3)

tk.Label(window, text="Enter phone number to send alerts to:", font = ("Comic Sans MS", 12), bg = "yellow").grid(row=1, column=0)
tk.Entry(window, textvariable=phone_number_var).grid(row=1, column=3)

tk.Label(window, text="Enter upper limit temperature in Kelvin:", font = ("Comic Sans MS", 12), bg = "yellow").grid(row=2, column=0)
tk.Entry(window, textvariable=upper_limit_var).grid(row=2, column=3)

tk.Label(window, text="Enter lower limit temperature in Kelvin:", font = ("Comic Sans MS", 12), bg="yellow").grid(row=3, column=0)
tk.Entry(window, textvariable=lower_limit_var).grid(row=3, column=3)

tk.Button(window, text="Start Monitoring", font = ("Comic Sans MS", 12), bg = "yellow", command=start_monitoring).grid(row=4, columnspan=2)

# Run the main loop
window.mainloop()