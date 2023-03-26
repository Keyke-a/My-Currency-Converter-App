#Creating a currency converter calculator that compares the user's input with other eight intermediaries and displays the best rate for users and profit for the company
#Create a GUI to display the code.
#KeykeA FX Data Services Currency Converter

#To make the HTTPS request from a Currency Conversion API
import requests

#To create a GUI
from tkinter import *
from tkinter import messagebox

#GUI window configuration
window = Tk()
window.title("KeykeA Currency Converter App")
window.geometry("600x6000")

#Create a label for the header
label_header = Label(window, text="KeykeA FX\nData Services", font=("Arial Bold", 20))
label_header.pack(pady=20)

#Create a label for where user inputs currency from
youTransfer_label = Label(window, text="YouTransfer:", font=("Arial", 12))
youTransfer_label.pack(pady=10)
youTransfer_window_entry = Entry(window, font=("Arial", 16), )
youTransfer_window_entry.pack(pady=20)

#Create a label for where user inputs recipient currency
Recipient_label = Label(window, text="Recipient:", font=("Arial", 12))
Recipient_label.pack(pady=10)
Recipient_window_entry = Entry(window, font=("Arial", 16))
Recipient_window_entry.pack(pady=20)

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
    currencies = ["USD", "EUR", "GBP", "CAD", "AUD", "JPY", "NGN", "VND", "HKD", "SGD"]
    # display currency options
    print("The supported currencies on this application are: ", ", ".join(currencies))

    # Getting the user's input
    while True: #Using a while loop to execute the statements below
        currency_to = input("Enter your currency: ").upper() #enter currency from
        theyReceive = input("Enter the currency you want to convert into : ").upper() #enter currency to

        if currency_to not in currencies and theyReceive not in currencies:
            print("Error: Both currencies are not listed on the supported currencies" "\n" "Please check supported currencies and try again.")
        elif currency_to not in currencies:
            print("Error: Your currency code is not listed on the supported currencies" "\n" "Please check supported currencies and try again.")
        elif theyReceive not in currencies:
            print("Error: Recipient currency code is not listed on the supported currencies" "\n" "Please check supported currencies and try again.")
        else:
            amount = float(input("Enter amount: ")) #enter amount to be converted.
            break

    # Calculate exchange rates between currencies using intermediary (third party) currencies listed on the supported currencies list.
    intermediary_currencies = [item for item in currencies if item not in [currency_to, theyReceive]]#Display other eight intermediary currencies
    intermediary_rates = []
    for currency in intermediary_currencies:
        firstRate = data[currency] / data[currency_to] #To calculate the user's currency rate
        secondRate = data[theyReceive] / data[currency]#To calculate the recipient's currencyrate
        totalRate = firstRate * secondRate #To get the total rate
        profit = 0.01 * totalRate #Important note: 1% of conversion rate is retained as the tiny font clause
        intermediary_rates.append((currency, totalRate, profit)) #To add all the rate and profits of the other eight intermediaries.
        print(f"1 {currency_to} = {firstRate} {currency}")
        print(f"1 {currency} = {secondRate} {theyReceive}")
        print(f"Conversion rate {currency_to} to {theyReceive} using {currency}: {firstRate} * {secondRate} = {totalRate}")
        print(f"Profit: {profit}")

    # Display all intermediary rates and profits
        print("Intermediary Rates:")
    for totalRate in intermediary_rates:
        print(f"{totalRate[0]}: {totalRate[1]:.4f}  Profit: {totalRate[2]:.3f}")


    # find the best conversion path
    best_rate = 0
    best_currency = ""
    for currency in intermediary_currencies:
        rate1 = data[currency_to] / data[currency]
        rate2 = data[theyReceive] / data[currency]
        if rate1 * rate2 > best_rate:
            best_rate = 100 * profit * amount
            best_currency = currency
            print("\n" f"The best intermediary conversion conversion path is: {currency_to} -> {best_currency} -> {theyReceive}")
            print(f"The best rate for you is: {best_rate:.4f}")
            print(f"Profit margin is:  {profit:.3f}")

#Create a button for the user to click after inputing details
convert_button = Button(window, text="Convert", font=("Arial Bold", 16), command=convert_currency)
convert_button.pack(pady=20)

#Display box
messagebox.showinfo("Conversion Result", "The conversion result will be displayed here.")

window.mainloop()

