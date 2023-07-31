# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 00:09:56 2023

@author: KIIT
"""

import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "b6907d289e10d714a6e88b30761fae22"


def get_weather(date):
    url = f"{API_BASE_URL}?q=London,us&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for forecast in data["list"]:
            if date in forecast["dt_txt"]:
                return forecast["main"]["temp"]
        return None
    else:
        return None


def get_wind_speed(date):
    url = f"{API_BASE_URL}?q=London,us&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for forecast in data["list"]:
            if date in forecast["dt_txt"]:
                return forecast["wind"]["speed"]
        return None
    else:
        return None


def get_pressure(date):
    url = f"{API_BASE_URL}?q=London,us&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for forecast in data["list"]:
            if date in forecast["dt_txt"]:
                return forecast["main"]["pressure"]
        return None
    else:
        return None


def main_fun():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_weather(date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature}°C")
            else:
                print("Error fetching temperature data.")

        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print(f"Wind speed on {date}: {wind_speed} m/s")
            else:
                print("Error fetching wind speed data.")

        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Error fetching pressure data.")

        elif choice == "0":
            print("Exiting....")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_fun()
