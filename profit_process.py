# Import
import plotly.express as ex

def process_profit_data(top_or_bot, profit_per_branch):
    if top_or_bot == 'top':
        profit = profit_per_branch.head(10)
        figure = ex.bar(profit, x='branch_name', y='profit', color='branch_name', title='Top profitable branches')
        return figure
    else:
        profit = profit_per_branch.tail(10)
        figure = ex.bar(profit, x='branch_name', y='profit', color='branch_name', title='Bottom profitable branches')
        return figure