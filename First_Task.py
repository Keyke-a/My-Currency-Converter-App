#Creating a currency converter calculator that compares the user's input with other eight intermediaries and displays the best rate for users and profit for the company
#KeykeA FX Data Services Currency Converter

#To make the HTTPS request from a Currency Conversion API
import requests

#Authentication to the Currency Conversion website
api_key = "998861d13c2d44ceb37998ac8f558491"
# Set the API Key endpoint URL
url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}" #not certain
# Spool the latest exchange rates from the above API
response = requests.get(url)
# parse the response
data = response.json()["rates"]

#Header
Header = ("KeykeA FX" "\n" "Data Services")
print(Header)

# Application supported currencies
Supported_currencies = ["USD", "EUR", "GBP", "CAD", "AUD", "JPY", "NGN", "VND", "HKD", "SGD"]
# display currency options
print("The supported currencies on this application are: ", ", ".join(Supported_currencies))


# Getting the user's input
while True: #Using a while loop to execute the statements below
    Base_currency_label = input("Enter your currency: ").upper() #enter currency from
    New_currency = input("Enter recipient currency : ").upper() #enter currency to

    if Base_currency_label not in Supported_currencies and New_currency not in Supported_currencies:
        print("Error: Both currencies are not listed on the supported currencies" "\n" "Please check supported currencies and try again.")
    elif Base_currency_label not in Supported_currencies:
        print("Error: Your currency code is not listed on the supported currencies" "\n" "Please check supported currencies and try again.")
    elif New_currency not in Supported_currencies:
        print("Error: Recipient currency code is not listed on the supported currencies" "\n" "Please check supported currencies and try again.")
    else:
        amount = float(input("Enter amount: ")) #enter amount to be converted.
        break

# Calculate exchange rates between currencies using intermediary (third party) currencies listed on the supported currencies list.
intermediary_currencies = [item for item in Supported_currencies if item not in [Base_currency_label, New_currency]]#Display other eight intermediary currencies
intermediary_rates = []
for currency in intermediary_currencies:
    firstRate = data[currency] / data[Base_currency_label] #To calculate the user's currency rate
    secondRate = data[New_currency] / data[currency]#To calculate the recipient's currencyrate
    Final_rate = firstRate * secondRate #To get the final rate
    profit = 0.01 * Final_rate #Important note: 1% of conversion rate is retained as the tiny font clause
    intermediary_rates.append((currency, Final_rate, profit)) #To add all the rate and profits of the other eight intermediaries.
    print(f"1 {Base_currency_label} = {firstRate} {currency}")
    print(f"1 {currency} = {secondRate} {New_currency}")
    print(f"Conversion rate {Base_currency_label} to {New_currency} using {currency}: {firstRate} * {secondRate} = {Final_rate}")
    print(f"Profit: {profit}")

# Display all intermediary rates and profits
print("Intermediary Rates:")
for Final_rate in intermediary_rates:
    print(f"{Final_rate[0]}: {Final_rate[1]:.4f}  Profit: {Final_rate[2]:.3f}")


#Determining the best conversion path
best_rate = 0
best_currency = ""
for currency in intermediary_currencies:
    rate1 = data[Base_currency_label] / data[currency]
    rate2 = data[New_currency] / data[currency]
    if rate1 * rate2 > best_rate:
        best_rate = 100 * profit * amount
        best_currency = currency
print("\n" f"The best intermediary conversion conversion path is: {Base_currency_label} -> {best_currency} -> {New_currency}")
print(f"The best rate for you is: {best_rate:.4f}")
print(f"Profit margin is:  {profit:.3f}")


