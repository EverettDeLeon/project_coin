# project_coin.py written by Everett De Leon
# Goal: write a coin projection program
# last revised: 01/16/2021


from datetime import date
import mechanicalsoup
import tkinter as tk


# Open window, set size
window = tk.Tk()
window.title('Project Coin')
window.geometry('400x600')


# class for cryptos
class Cryptos():
    def __init__(self, name, investment, value, growth):
        self.name = name
        self.investment = investment
        self.value = value
        self.growth = growth


# all currencies
snx = Cryptos('snx', 1737.56, 2028.66, 437.30)
dot = Cryptos('dot', 1201, 1387.95, 1500)
ada = Cryptos('ada', 593.94, 621.80, 643.08)
grt = Cryptos('grt', 498.98, 554.38, 284.52)


#***use later*** logic to run entire collection
total_value = snx.value + dot.value + ada.value + grt.value
total_invested = snx.investment + dot.investment + ada.investment + grt.investment
profit = total_value - total_invested 
# timeline
months = 12
weeks = 52
days = 365


#***use later*** percentage growth  
growth_yr = (snx.growth + dot.growth + ada.growth + grt.growth) / 4
growth_month = growth_yr / 12
growth_week = growth_yr / 52
growth_day = growth_yr / 365


# gui
# investment
investment = tk.Label(window, text='What was your original investment?')
investment.place(x=10, y=10)
investment_input = tk.Entry(window)
investment_input.place(x=10, y=30)
# routine investment
routine_investment = tk.Label(window, text='How much would like to invest monthly?')
routine_investment.place(x=10, y=50)
routine_investment_input = tk.Entry(window)
routine_investment_input.place(x=10, y=70)
# time span
time_span = tk.Label(window, text='How many weeks would you like to hodl?')
time_span.place(x=10, y=90)
time_span_input = tk.Entry(window)
time_span_input.place(x=10, y=110)
# interest rate
interest_rate = tk.Label(window, text='What is the interest rate per week?')
interest_rate.place(x=10, y=130)
interest_rate_input = tk.Entry(window)
interest_rate_input.place(x=10, y=150)
# drop down menu
currencies = [snx.name, dot.name, ada.name, grt.name]
variable = tk.StringVar(window)
variable.set(currencies[0])
option = tk.OptionMenu(window, variable, *currencies)
option.config(width=10)
option.place(x=10, y=190)


# calculate everything and display the results
def Calculate():
    init_inv = float(investment_input.get())
    routine_inv = float(routine_investment_input.get())
    timespan = float(time_span_input.get())
    interest_rate = float(interest_rate_input.get())
    profit = 0
    balance = init_inv
    end_loop = 0
    while end_loop != timespan:
        print(f'balance: {balance}')
        profit = (balance * interest_rate) / 100.
        print(f'profit: {profit}')
        balance = balance + profit
        end_loop += 1
        print(f'Timespan {end_loop}')
        print(f'balance after loop {balance}')
        # ^ working
        if end_loop > 1 and end_loop % 4 == 0:
            balance = balance + routine_inv 
            print(f'new balance: {balance}')
        if end_loop == timespan:
            results_label = tk.Label(window, text=f'Balance: {round(balance, 2)}')
            results_label.place(x=10, y=210)


# submit button
submit = tk.Button(window, text='Submit', command=Calculate)
submit.place(x=10, y=170)


window.mainloop()