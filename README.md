<<<<<<< Updated upstream
# Temperature Alert Agent

A temperature alert made while implementing the uAgents library provided by Fetch.ai. The project offers the following two functionalities:

1.  **Set temperature alerts: **Allows the user to set a location to monitor at an interval of 5 minutes, and sends SMS alerts if the user-provided range is violated, i.e., temperature goes below a minimum value or above a maximum value.
2.   **Plot Historical Data: **All the data collected by the alert bot is stored in a MySQL database, and this functionality provides ability to graphically analyse the relation of temperature to the date and time.

**For ease of access, the bot operates with a TKinter GUI.**

## **How to use:**

### ****Step 1: Prerequisites:****

Before starting, you will need the following:
- Python (3.8+ is recommended)
- Poetry (A packaging and dependency management tool for python)

### ****Step 2: Set up .env file****

To work with this program, you will need API keys for:
- OpenWeatherMap API
- Twilio (Account SUD, Auth Token and a Twilio Phone Number)

To obtain these, you will need to navigate to the respective websites and sign up for their free plan for the respective APIs.
Upon obtaining, input them into the sample.env file and rename it to .env

Now, install the dependencies using the following code in the project directory:

    poetry install
                
----

### ****Step 3: Run the program****

In a command line interface, run:


    poetry shell
    cd src
    main.py

Note: First the Set Temp Alerts window opens, and if the dataplot is required, we close it, then the new window opens.    
### ****Database****

All the temperature results are inputted into the following MySQL database, the structure of which is shown below:

![Screenshot 2023-10-11 043233](https://github.com/MistyDragon7/HackAI_230295/assets/120657456/176cf98c-e812-403e-8bd1-7f211054683f)
=======
