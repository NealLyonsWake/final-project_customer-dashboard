# Import
import plotly.express as ex

def process_hourly_sales(branch_selected, year_selected, month_selected, grouped_branch_performance):
     # Return data figure selected
        branch_hour = grouped_branch_performance[\
            (grouped_branch_performance['branch_name'] ==branch_selected) &\
                (grouped_branch_performance['year']== year_selected) &\
                     (grouped_branch_performance['month']== month_selected)].sort_values(by='hour')
        figure = ex.line(
            branch_hour, x='hour',
             y='amount_in_gbp',
              title=f'Hourly sales in {year_selected}, in {find_month(month_selected)} for {branch_selected}',
               markers=True)
        figure.update_layout(\
        xaxis_title="Hour (in 24-hour, 23 = 23:00)",
        yaxis_title="Sales in GBP")
        return figure

def find_month(month_selected):
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return month[month_selected-1]