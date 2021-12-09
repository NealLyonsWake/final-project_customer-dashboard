# Import
import plotly.express as ex

def process_profit_data(top_or_bot, profit_per_branch):
    if top_or_bot == 'top':
        profit = profit_per_branch.head(10)
        figure = ex.bar(profit, x='branch_name', y='profit', color='branch_name')
        return "Top 10 profitable branches are:", figure
    else:
        profit = profit_per_branch.tail(10)
        figure = ex.bar(profit, x='branch_name', y='profit', color='branch_name')
        return "Bottom 10 profitable branches are:", figure