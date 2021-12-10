# Import
import plotly.express as ex

# Processing function for handling products and categories in Dash callback
def process_prod_cat(top_or_bot, prod_or_cat, region_selected, grouped_products, grouped_categories):
     # Determine top or bottom
        if top_or_bot == "top":
            # Determine top product or top category
            if prod_or_cat == "products":
                # Process top products by region
                per_region = grouped_products[grouped_products['region']==region_selected].head()
                figure = ex.bar(per_region, x='product', y='quantity', color='product', title=f'Top products in {region_selected}')
                return figure
            else:
                # Process top categories by region
                per_region = grouped_categories[grouped_categories['region']==region_selected].head()
                figure = ex.bar(per_region, x='category', y='quantity', color='category', title=f'Top categories in {region_selected}')
                return figure
        else:
            # Determine bottom product or bottom category
            if prod_or_cat == "products":
                # Process bottom products by region
                per_region = grouped_products[grouped_products['region']==region_selected].tail()
                figure = ex.bar(per_region, x='product', y='quantity', color='product', title=f'Bottom products in {region_selected}')
                return figure
            else:
                # Process bottom categories by region
                per_region = grouped_categories[grouped_categories['region']==region_selected].tail()
                figure = ex.bar(per_region, x='category', y='quantity', color='category', title=f'Bottom categories in {region_selected}')
                return figure