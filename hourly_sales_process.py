# Import
import plotly.express as ex

def process_hourly_sales(branch_selected, year_selected, month_selected, grouped_branch_performance):
     # Return data figure selected
        branch_hour = grouped_branch_performance[\
            (grouped_branch_performance['branch_name'] ==branch_selected) &\
                (grouped_branch_performance['year']== year_selected) &\
                     (grouped_branch_performance['month']== month_selected)].sort_values(by='hour')
        figure = ex.line(branch_hour, x='hour', y='amount_in_gbp')
        return branch_selected, figure
