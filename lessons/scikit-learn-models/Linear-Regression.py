import numpy as np

#Assignment link:
#https://g.co/gemini/share/30b710d73591

#B. Basic linear regression#
pizza_data = np.array([[6, 7], [8, 9], [10, 12], [14, 16], [18, 20]])
pizza_prices = np.array([7, 9, 12, 16, 20])
# predefined pizza data and prices
print('{}\n'.format(repr(pizza_data)))
print('{}\n'.format(repr(pizza_prices)))

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(pizza_data, pizza_prices)

# new pizza data
new_pizzas = np.array([[2000,  820],
                       [2200,  830]])

price_predicts = reg.predict(new_pizzas)
print('{}\n'.format(repr(price_predicts)))

print('Coefficients: {}\n'.format(repr(reg.coef_)))
print('Intercept: {}\n'.format(reg.intercept_))

# Using previously defined pizza_data, pizza_prices
r2 = reg.score(pizza_data, pizza_prices)
print('R2: {}\n'.format(r2))


#Ridge Regression
#Understand the need for regularization in linear regression.

#B. Choosing the best alpha#

from sklearn import linear_model
reg = linear_model.Ridge(alpha=0.1)
reg.fit(pizza_data, pizza_prices)
print('Coefficients: {}\n'.format(repr(reg.coef_)))
print('Intercept: {}\n'.format(reg.intercept_))
r2 = reg.score(pizza_data, pizza_prices)
print('R2: {}\n'.format(r2))


#LASSO Regression
#Understand the need for regularization in linear regression.

#A. Sparse regularization#
# from sklearn import linear_model

# def lasso_reg(data, labels, alpha):
#   # CODE HERE
#   reg = linear_model.Lasso(alpha=alpha)
#   reg.fit(data, labels)
#   return reg


#C. Tuning the model#

