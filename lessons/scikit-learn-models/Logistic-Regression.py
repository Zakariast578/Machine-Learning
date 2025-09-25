import numpy as np
from sklearn import linear_model


# Assignment link:
#https://g.co/gemini/share/30b710d73591

# Logistic Regression
# Example data with 4 features and 569 samples
data = np.random.rand(569, 4) * 10
labels = np.random.randint(0, 2, size=569) # 0s and 1s

print('Data shape: {}\n'.format(data.shape))
print('Labels:\n{}\n'.format(repr(labels)))

# Create and fit the Logistic Regression model
reg = linear_model.LogisticRegression()
reg.fit(data, labels)

# New data to predict
new_data = np.array([
  [  0.3,  0.5, -1.2,  1.4],
  [ -1.3,  1.8, -0.6, -8.2]])

# Make predictions and print the results
print('Prediction classes: {}\n'.format(
  repr(reg.predict(new_data))))

#C. Cross-validated model#
