# Consumer Behaviour (Part 2 of Final Python Project)

- The client has submitted a request to produce a dashboard that enables them to track consumer behaviour.
- The project brief, as well as user stories and application wireframes are available [here.](https://miro.com/app/board/uXjVOdPBydg=/?invite_link_id=165928041830)


## Deployment

This application has been deployed and available [here.](https://consumer-behaviour-dashboard.herokuapp.com/)


## Data origin

- The csv data available in this repo originates from part 1 of this project. See the part 1 project, [here](https://github.com/NealLyonsWake/final-project_data-cleaning), for further details.
- The data is set within the `data` folder of this repo and deployed with the application.


## Dash

- As per the brief, the consumer behaviour data is presented as a dash application, and is split into 4 main sections:
    - Product and Categories Sales Ratings
    - Branch Performance
    - Hourly Sales Per Branch
    - Branch Profitability


## Visualization Choices and Justification

- All but a single section above was determined to be visualised as bar charts:
    - Product and Categories Sales Ratings
    - Branch Performance, and;
    - Branch Profitability were used in bar charts as it was simple to view the top and bottom subjects in this manner.
- Hourly Sales Per Branch was determined to be visualized better in the form of a line graph, by hour, as the hours could be displayed on the x-axis and the sales value could be displayed on the y-axis.
