# Import
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from product_category_process import process_prod_cat
from branch_performance_process import handle_branch_performance
from hourly_sales_process import process_hourly_sales
from profit_process import process_profit_data

# Import dataframes
region_list = pd.read_csv("data/region_list.csv")
branch_name_list = pd.read_csv("data/branch_name_list.csv")
grouped_branch_performance = pd.read_csv("data/grouped_branch_performance.csv")
grouped_categories = pd.read_csv("data/grouped_categories.csv")
grouped_products = pd.read_csv("data/grouped_products.csv")
overall_branch_performance = pd.read_csv("data/overall_branch_performance.csv")
profit_per_branch = pd.read_csv("data/profit_per_branch.csv")

# Create selection variables from relevant dataframes
region_options = region_list["region"]
branch_options = branch_name_list["branch_name"]

# Dash initialisation
app = dash.Dash("", external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout elements
app.layout = html.Div([
html.Div(
        [ html.H1("Customer Data Dashboard"),
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    [
                        html.Div(
                            [
                                html.H5("Select Top 5 or Bottom 5"),
                                dcc.Dropdown(
                                    options=[
                                        {"label": "Top 5", "value": "top"},
                                        {"label": "Bottom 5", "value": "bottom"},
                                    ],
                                    id="top-bot-selector",
                                ),
                                html.Br(),                                
                                html.H5(
                                    "Select Purchased Products or Purchased Categories"
                                ),
                                dcc.Dropdown(
                                    options=[
                                        {
                                            "label": "Purchased Products",
                                            "value": "products",
                                        },
                                        {
                                            "label": "Purchased Categories",
                                            "value": "categories",
                                        },
                                    ],
                                    id="prod-cat-selector",
                                ),
                                html.Br(),                                
                                html.H5("Select Region"),
                                dcc.Dropdown(
                                    options=[
                                        {"label": i, "value": i} for i in region_options
                                    ],
                                    id="region-selector",
                                ),
                                html.Br(),                                
                                html.Button("Go", id="prod-cat-go", n_clicks=0),
                                html.Br(),                                
                                html.Div([dcc.Graph(id="prod-cat-visual", figure={})]),
                            ]
                        )
                    ],
                    title="Product and Categories Sales Ratings",
                ),
                dbc.AccordionItem(
                    [
                        html.Div(
                            [
                                html.H5("Select Top 10 or Bottom 10"),
                                dcc.Dropdown(
                                    options=[
                                        {"label": "Top 10", "value": "top"},
                                        {"label": "Bottom 10", "value": "bottom"},
                                    ],
                                    id="top-bot-branch-selector",
                                ),
                                html.Br(),                                
                                html.H5("Select Region"),
                                dcc.Dropdown(
                                    options=[
                                        {"label": i, "value": i} for i in region_options
                                    ],
                                    id="region-for-branch-selector",
                                ),
                                html.Br(),                                
                                html.Button("Go", id="for-branch-go", n_clicks=0),
                                html.Div(
                                    [dcc.Graph(id="for-branch-visual", figure={})]
                                ),
                            ]
                        )
                    ],
                    title="Branch Performance",
                ),
                dbc.AccordionItem(
                    [
                        html.Div(
                            [
                                html.H5("Select Branch"),
                                dcc.Dropdown(
                                    options=[
                                        {"label": i, "value": i} for i in branch_options
                                    ],
                                    id="branch-selector",
                                ),
                                html.Br(),                                
                                html.H5("Select Year"),
                                dcc.Slider(
                                    id="year-range-slider",
                                    min=2010,
                                    max=2020,
                                    marks={
                                        2010: "2010",
                                        2011: "2011",
                                        2012: "2012",
                                        2013: "2013",
                                        2014: "2014",
                                        2015: "2015",
                                        2016: "2016",
                                        2017: "2017",
                                        2018: "2018",
                                        2019: "2019",
                                        2020: "2020",
                                    },
                                    step=1,
                                    value=2020,
                                ),
                                html.Br(),
                                html.H5("Select Month"),
                                dcc.Slider(
                                    id="month-selector",
                                    min=1,
                                    max=12,
                                    marks={
                                        1: "Jan",
                                        2: "Feb",
                                        3: "Mar",
                                        4: "Apr",
                                        5: "May",
                                        6: "Jun",
                                        7: "Jul",
                                        8: "Aug",
                                        9: "Sep",
                                        10: "Oct",
                                        11: "Nov",
                                        12: "Dec",
                                    },
                                    step=1,
                                    value=4,
                                ),
                                html.Br(),
                                html.Div(
                                    [dcc.Graph(id="hourly-sales-visual", figure={})]
                                ),
                            ]
                        )
                    ],
                    title="Hourly Sales Per Branch",
                ),
                dbc.AccordionItem(
                    [
                        html.Div(
                            [
                                html.H5("Select Top 10 or Bottom 10"),
                                dcc.Dropdown(
                                    options=[
                                        {"label": "Top 10", "value": "top"},
                                        {"label": "Bottom 10", "value": "bottom"},
                                    ],
                                    id="top-bot-profit-selector",
                                ),
                                html.Br(),
                                html.Button("Go", id="profit-go", n_clicks=0),
                                
                                html.Div([dcc.Graph(id="profit-visual", figure={})]),
                            ]
                        )
                    ],
                    title="Branch Profitability",
                ),
            ], className="panel", start_collapsed=True
        )
    ], className = "page-root"
), html.Img(src="https://cdn.vox-cdn.com/thumbor/75uicUdgk65_lUpNT_TdrpY9XXk=/0x0:7999x4000/1200x675/filters:focal(3361x1361:4639x2639)/cdn.vox-cdn.com/uploads/chorus_image/image/69333291/GettyImages_1043605040.0.jpg", width='100%')], className= "img-panel")

# Callback
@app.callback(
    # Track top and bottom products and categories per region
    Output(component_id="prod-cat-visual", component_property="figure"),
    Input(component_id="prod-cat-go", component_property="n_clicks"),
    State(component_id="top-bot-selector", component_property="value"),
    State(component_id="prod-cat-selector", component_property="value"),
    State(component_id="region-selector", component_property="value"),
)
def request_product_category_data(on_click, top_or_bot, prod_or_cat, region_selected):
    if [top_or_bot, prod_or_cat, region_selected] is not None:
        return process_prod_cat(
            top_or_bot,
            prod_or_cat,
            region_selected,
            grouped_products,
            grouped_categories,
        )
    else:
        return {}


@app.callback(
    # Track top and bottom branch performance per region
    Output(component_id="for-branch-visual", component_property="figure"),
    Input(component_id="for-branch-go", component_property="n_clicks"),
    State(component_id="top-bot-branch-selector", component_property="value"),
    State(component_id="region-for-branch-selector", component_property="value"),
)
def request_branch_performance_data(on_click, top_or_bot, region_selected):
    if [top_or_bot, region_selected] is not None:
        return handle_branch_performance(
            top_or_bot, region_selected, overall_branch_performance
        )
    else:
        return {}


@app.callback(
    # Display hourly sales per branch
    Output(component_id="hourly-sales-visual", component_property="figure"),
    Input(component_id="branch-selector", component_property="value"),
    Input(component_id="year-range-slider", component_property="value"),
    Input(component_id="month-selector", component_property="value"),
)
def request_branch_hourly_sales(branch_selected, year_selected, month_selected):
    if [branch_selected, year_selected, month_selected] is not None:
        return process_hourly_sales(
            branch_selected, year_selected, month_selected, grouped_branch_performance
        )
    else:
        return {}


@app.callback(
    # Display profitable branches
    Output(component_id="profit-visual", component_property="figure"),
    Input(component_id="profit-go", component_property="n_clicks"),
    State(component_id="top-bot-profit-selector", component_property="value"),
)
def request_profit_date(on_click, top_or_bot):
    if top_or_bot is not None:
        return process_profit_data(top_or_bot, profit_per_branch)
    else:
        return {}


# Run
if __name__ == "__main__":
    app.run_server(debug=True)

