

#A. Making decisions#
from sklearn import tree
import numpy as np

# --- Predefined Dataset (Synthetic Data for Demonstration) ---
# Create 10 samples, 4 features
np.random.seed(42) # for reproducibility
data = np.random.randn(10, 4) 
# Create 10 binary labels (0 or 1)
labels = np.array([0, 1, 0, 1, 1, 0, 1, 0, 1, 0]) 
# ------------------------------------------------------------

# Decision Tree Classifier (default parameters)
clf_tree1 = tree.DecisionTreeClassifier()
# Decision Tree Regressor (default parameters)
reg_tree1 = tree.DecisionTreeRegressor()

# Decision Tree Classifier (max depth of 8)
clf_tree2 = tree.DecisionTreeClassifier(
  max_depth=8)
# Decision Tree Regressor (max depth of 5)
reg_tree2 = tree.DecisionTreeRegressor(
  max_depth=5)

# predefined dataset
print('Data shape: {}\n'.format(data.shape))
# Binary labels
print('Labels:\n{}\n'.format(repr(labels)))

# Train the first Decision Tree Classifier
clf_tree1.fit(data, labels)

print(f"\nclf_tree1 (Decision Tree Classifier) trained successfully.")
print(f"Features used: {clf_tree1.n_features_}")
print(f"Max depth of the trained tree: {clf_tree1.tree_.max_depth}")