# project_coin.py written by Everett De Leon
# Goal: write a coin projection program
# last revised: 01/16/2021


from datetime import date
import mechanicalsoup
import tkinter as tk


blue_color = '#%02x%02x%02x' % (66,103,178)
red_color = '#%02x%02x%02x' % (188,51,21)
dark_red_color = '#%02x%02x%02x' % (135,36,14)


# Open window, set size
window = tk.Tk()
window.title('Project Coin')
window.geometry('320x420')
window.configure(bg=blue_color)


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
#***use later***timeline
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
investment = tk.Label(window, text='Starting investment:', bg=blue_color)
investment.place(x=20, y=60)
investment_input = tk.Entry(window)
investment_input.place(x=20, y=80)
# routine investment
routine_investment = tk.Label(window, text='Routine monthly investment:', bg=blue_color)
routine_investment.place(x=20, y=120)
routine_investment_input = tk.Entry(window)
routine_investment_input.place(x=20, y=140)
# time span
time_span = tk.Label(window, text='How many weeks are you staying invested:', bg=blue_color)
time_span.place(x=20, y=180)
time_span_input = tk.Entry(window)
time_span_input.place(x=20, y=200)
# interest rate
interest_rate = tk.Label(window, text='Return on investment avg  per week:', bg=blue_color)
interest_rate.place(x=20, y=240)
interest_rate_input = tk.Entry(window)
interest_rate_input.place(x=20, y=260)
# drop down menu
currencies = [snx.name, dot.name, ada.name, grt.name]
variable = tk.StringVar(window)
variable.set(currencies[0])
option = tk.OptionMenu(window, variable, *currencies)
option.config(width=10)
option.place(x=20, y=20)


# calculate everything and display the results
def Calculate():
    init_inv = float(investment_input.get())
    routine_inv = float(routine_investment_input.get())
    timespan = float(time_span_input.get())
    interest_rate = float(interest_rate_input.get())
    profit = 0
    balance = init_inv
    end_loop = 1
    total_profit = 0
    while end_loop != timespan:
        profit = (balance * interest_rate) / 100.
        total_profit = total_profit + profit
        print(f'profit: {total_profit}')
        balance = balance + profit
        end_loop += 1
        print(f'Timespan {end_loop}')
        print(f'balance after loop {balance}')
        # ^ working
        if end_loop > 1 and end_loop % 4 == 0:
            balance = balance + routine_inv 
            print(f'new balance: {balance}')
        if end_loop == timespan:
            results_label = tk.Label(window, text=f'End Investment: {round(balance - total_profit, 2)}', bg=blue_color)
            results_label.place(x=20, y=340)
            results_label = tk.Label(window, text=f'End Balance: {round(balance, 2)}', bg=blue_color)
            results_label.place(x=20, y=380)
            results_label = tk.Label(window, text=f'End profit: {round(total_profit, 2)}', bg=blue_color)
            results_label.place(x=20, y=360)


# submit button
submit = tk.Button(window, text='Submit', command=Calculate, bg=red_color, activebackground=dark_red_color)
submit.place(x=250, y=300)


window.mainloop()
