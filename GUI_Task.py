#Creating a currency converter calculator that compares the user's input with other eight intermediaries and displays the best rate for users and profit for the company
#Create a GUI to display the code.
#KeykeA FX Data Services Currency Converter

#To make the HTTPS request from a Currency Conversion API
import requests

#To create a GUI
from tkinter import *

#GUI window configuration
window = Tk()
window.title("KeykeA Currency Converter App")
window.geometry("600x600")

#Create a label for the header
label_header = Label(window, text="KeykeA FX\nData Services", font=("Arial Bold", 20))
label_header.pack(pady=20)

#Create a label for where user inputs currency from
Base_currency_label = Label(window, text="YouTransfer:", font=("Arial", 12))
Base_currency_label.pack(pady=10)
Base_currency_window_entry = Entry(window, font=("Arial", 16), )
Base_currency_window_entry.pack(pady=20)

#Create a label for where user inputs currency to
New_currency_label = Label(window, text="Recipient:", font=("Arial", 12))
New_currency_label.pack(pady=10)
New_currency_window_entry = Entry(window, font=("Arial", 16))
New_currency_window_entry.pack(pady=20)

#Create a label for where user inputs the amount
amount_label = Label(window, text="Amount:", font=("Arial", 12))
amount_label.pack(pady=10)
amount_window_entry = Entry(window, font=("Arial", 16))
amount_window_entry.pack(pady=20)

#Authentication key from the Currency Conversion website
api_key = "998861d13c2d44ceb37998ac8f558491"

def convert_currency():

    # Set the API Key endpoint URL
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}" 
    # Spool the latest exchange rates from the above API
    response = requests.get(url)
    # Parse the response
    data = response.json()["rates"]
    # Application supported currencies
    Supported_currencies = ["USD", "EUR", "GBP", "CAD", "AUD", "JPY", "NGN", "VND", "HKD", "SGD"]
    # display currency options
    print("The supported currencies on this application are: ", ", ".join(Supported_currencies))

    # Getting the user's input
    while True: #Using a while loop to execute the statements below
        Base_Currency = input("Enter your currency: ").upper()
        New_Currency = input("Enter the currency you want to convert into : ").upper()

        if Base_Currency not in Supported_currencies and New_Currency not in Supported_currencies:
            print("Error: Both currencies are not listed on the supported currencies" "\n" "Please check supported currencies and try again.")
        elif Base_Currency not in Supported_currencies:
            print("Error: Your currency code is not listed on the supported currencies" "\n" "Please check supported currencies and try again.")
        elif New_Currency not in Supported_currencies:
            print("Error: Recipient currency code is not listed on the supported currencies" "\n" "Please check supported currencies and try again.")
        else:
            amount = float(input("Enter amount to be converted: "))
            break

    # Calculate exchange rates between currencies using intermediary (third party) currencies listed on the supported currencies list.
    intermediary_currencies = [value for value in Supported_currencies if value not in [Base_Currency, New_Currency]]#Display other eight intermediary currencies
    intermediary_rates = []
    for currency in intermediary_currencies:
        firstRate = data[currency] / data[Base_Currency] #To calculate the user's currency rate
        secondRate = data[New_Currency] / data[currency]#To calculate the recipient's currencyrate
        Final_Rate = firstRate * secondRate #To get the final rate
        profit = 0.01 * Final_Rate #Important note: 1% of conversion rate is retained as the tiny font clause
        intermediary_rates.append((currency, Final_Rate, profit)) #To add all the rate and profits of the other eight intermediaries.
        print(f"1 {Base_Currency} = {firstRate} {currency}")
        print(f"1 {currency} = {secondRate} {New_Currency}")
        print(f"Conversion rate {Base_Currency} to {New_Currency} using {currency}: {firstRate} * {secondRate} = {Final_Rate}")
        print(f"Profit: {profit}")

    # Display all intermediary rates and profits
        print("Intermediary Rates:")
    for Final_Rate in intermediary_rates:
        print(f"{Final_Rate[0]}: {Final_Rate[1]:.4f}  Profit: {Final_Rate[2]:.3f}")


    #Determining the best conversion path
    best_rate = 0
    best_currency = ""
    for currency in intermediary_currencies:
        rate1 = data[Base_Currency] / data[currency]
        rate2 = data[New_Currency] / data[currency]
        if rate1 * rate2 > best_rate:
            best_rate = 100 * profit * amount
            best_currency = currency
            print("\n" f"The best intermediary conversion conversion path is: {Base_Currency} -> {best_currency} -> {New_Currency}")
            print(f"The best rate for you is: {best_rate:.4f}")
            print(f"Profit margin is:  {profit:.3f}")

#Create a button for the user to click after inputing details
click_button = Button(window, text="Convert", font=("Arial Bold", 16), command=convert_currency)
click_button.pack(pady=20)



window.mainloop()

