# Import
import plotly.express as ex

# Processing function for handling branch performance in Dash callback
def handle_branch_performance(top_or_bot, region_selected, overall_branch_performance):
    # Determine if top or bottom
    if top_or_bot == "top":
        per_region = overall_branch_performance[overall_branch_performance['region']==region_selected].head(10)
        figure = ex.bar(per_region, x='branch_name', y='performance', color='branch_name')
        return region_selected, figure
    else:
        per_region = overall_branch_performance[overall_branch_performance['region']==region_selected].tail(10)
        figure = ex.bar(per_region, x='branch_name', y='performance', color='branch_name')
        return region_selected, figure