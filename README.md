# Ads-Performance-Predictor
The model provides a quantitative framework for understanding and optimizing the impact of advertising spend on sales outcomes

About The Dataset:

The dataset provides detailed insights into how advertising spending across different media channels influences sales outcomes. This dataset covers comprehensive advertising campaigns data and their corresponding sales, allowing us to analyze the effectiveness of media spend in generating sales revenue.

Dataset Features:

TV: Investment in TV advertising campaigns (in thousands of dollars).
Radio: Investment in radio advertising campaigns (in thousands of dollars)
Newspaper: Investment in newspaper advertising campaigns (in thousands of dollars)
Sales: Revenue generated from sales campaigns (in thousands of dollars).

# Aim of the Model:

The model aims to predict sales outcomes based on the amount of money spent on different advertising channels like TV, Radio, and Newspaper. Specifically, it tries to answer the question:
How does the spending on TV, Radio, and Newspaper advertising influence the total sales?

By analyzing the relationship between advertising spend across these media channels and sales outcomes, the model helps to understand which channels contribute most effectively to sales, allowing businesses to allocate their marketing budgets more efficiently.

# Interpretation of the Model Prediction
The model predicts sales based on given values of advertising spend. Here’s the interpretation of the predictions:

+ Predicted Sales Value: The output of the model is the predicted sales figure for a given combination of TV, Radio, and Newspaper spending.
For example, if the model predicts a sales value of 15, this means that, given the specific spending on TV, Radio, and Newspaper, the expected sales outcome is 15 units.

+ Coefficients (Feature Importance): Intercept: Represents the base level of sales when there is no spending on any of the media channels. This is the predicted sales when all the advertising spend variables (TV, Radio, Newspaper) are zero.
+ Coefficients: Each coefficient represents the change in the predicted sales value for a one-unit change in spending on that particular media channel, holding all other variables constant.
For instance, if the coefficient for TV is 0.05, it means that for every additional unit of currency spent on TV advertising, sales are expected to increase by 0.05 units, assuming other spending remains the same.
