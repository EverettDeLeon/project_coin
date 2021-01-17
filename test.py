
from datetime import date
import mechanicalsoup
import tkinter as tk


# Open window, set size
window = tk.Tk()
window.title('Project Coin')
window.geometry('400x600')


class Cryptos():
    def __init__(self, name, investment, value, growth):
        self.name = name
        self.investment = investment
        self.value = value
        self.growth = growth


snx = Cryptos('snx', 1737.56, 2028.66, 437.30)
dot = Cryptos('dot', 1201, 1387.95, 1500)
ada = Cryptos('ada', 593.94, 621.80, 643.08)
grt = Cryptos('grt', 498.98, 554.38, 284.52)

total_value = snx.value + dot.value + ada.value + grt.value
total_invested = snx.investment + dot.investment + ada.investment + grt.investment
profit = total_value - total_invested 

months = 12
weeks = 52
days = 365


# percentage growth  
growth_yr = (snx.growth + dot.growth + ada.growth + grt.growth) / 4
growth_month = growth_yr / 12
growth_week = growth_yr / 52
growth_day = growth_yr / 365


print(f"You invested {total_invested} and you've earned {profit} and your total balance is {total_value}")
print(f'Growth rate {growth_yr}')
print(f'')






# # logic for investing and intrest and what not
# while weeks >= 0:
#     balance = original_inv + profit
#     profit = (balance * percent) / 100
#     if weeks % 4 == 0:
#         original_inv = balance + routine_invest
#     else:
#         original_inv = balance
#     weeks = weeks - 1
#     print(f'balance: {balance}')
#     print(f'profit: {profit}')
#     print(f'balance plus routine investment: {original_inv}')












window.mainloop()