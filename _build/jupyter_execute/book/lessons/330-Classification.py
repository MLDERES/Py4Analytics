#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('..')
from src.data import load_data
from src.metric import classificationSummary, confusion_matrix

# If you prefer a different style, pick from this list
# plt.style.available
pd.set_option('display.precision',4)
plt.style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (20, 10)


# # Classification
# 
# One of the most straightforward machine learning techniques is classification.  That is determining which category a to which particular observation belongs.  For example: 
# * an individual passenger on the [titanic was likely to survive](https://www.kaggle.com/c/titanic-dataset/data),
# * which [income bracket](https://archive.ics.uci.edu/ml/datasets/Adult) an individual is likely to be a part of 
# * will a [customer will qualify](https://www.kaggle.com/vikasukani/loan-eligible-dataset) for a loan.
# 
# All of these are classification questions.  Given a set of independent variables (e.g. factors) what is the likelihood that the dependent variable meets that category. 
# 

# ## Assessing Predictive Performance
# Before we get too far into running algorithms we need a method to determine how good our model is.  There are a number of different metrics we might use.  But this depends on whether we are predicting/estimating a continuous target or a categorical target.  Some of the common methods are included here.
# 
# Continuous Target
# * MAE - Mean absolute error
# * Mean Error - 
# * MPE - Mean percentage error
# * MAPE - Mean absolute percentage error
# * RMSE - Root mean square error
# 
# We will look at the continuous methods in depth in the [Estimation Notebook](340-EstimationPrediction.ipynb).
# 
# Categorical Target
# - Misclassification Rate
# - Recall (aka True Positive Rate, hit rate, sensitivity)
# - Precision
# 
# We'll focus here on _accuracy_ 
# 
# $$accuracy = \frac{NumberOfCorrectPredictions}{AllPredictions}$$
# and _precision_
# $$precision = \frac{TruePositives}{TruePositives+FalsePositives}$$
# 
# ### Naive Performance
# The simplest way to determine if a model is valuable or not is to compare to the "naive rule".  In essense, if we predict the most common outcome every time what is the misclassification rate.  If our model is no better than this, then our model isn't very helpful.
# 
# For instance, let's say that in a list of 10 loan applicants that 8 of the applicants will be approved for a loan and that 2 won't be approved.  If we were to blindly assume that all 10 applicants would be approved for a loan - then we would be wrong 20% of the time (2/10).  Therefore, if we can't develop a model which is at least 80% accurate then we don't have a very good model.
# 
# ### Cut-off values for classification
# We also need to consider that in nearly all of our classification models, what we are given is the _probability_ or likelihood that the predicted target is in the given class, therefore the value we get from our classification algorithms is on a scale from 0 to 1.  Most often, the default is to say that a target belongs to a class if the probability of being in the class is > 0.5.  But it can be useful to move this cut-off.  For instance, if the cost of predicting a particular class is unusually high, we may want to raise the probability to 0.6 or greater.

# ## Classification - Flight Delays
# For this problem, we are going to jump right into the pattern we will use for running near all of our models.
# 1. Start by importing the data
# 2. Get a sense of the shape, type and features of the data
# 3. Perform any data preparation functions 
# 4. Isolate the predictive factors (independent variables) from the target variable (dependent variable)
# 5. Split the dataset into a training set and a validation set (if necessary we would also keep a 'test' set)
# 6. Adjust model parameters (each modelling algorithm has different parameters which affect it's function)
# 7. Using the training set, fit the data to an appropriate model
# 8. Apply the model to the validation set
# 9. Determine model performance
# 10. If the performance is adequate the model is ready to be deployed, if not then go back to step 3 or 6.
# 
# <img src='../img/ml_process.jpg' width=600 height=400 class='center'/>
# 
# The Naive Bayes classifier is one of the simplest to understand, but it has a number of limitations.  Let's start with the complete, or exact [Bayesian classifier](https://en.wikipedia.org/wiki/Bayes_classifier).  The principal is
# 1. Find all the records with the same predictor profile as the target (that is where all the predicting factors are the same).
# 2. Determine which class these records belong to and which class is most prevelant
# 3. Assign that class to the new record
# 
# This is a bit limiting in that we can only use categorical variables to predict the values also what happens if there are no records in the dataset that match the predictor profile of the target?  We'll not spend time on the exact details of the method - our focus instead will be on how to use the `sklearn` library to apply any classification problem as the pattern is the same.
# 
# ### Common libraries for data science
# One of the most common libraries for developing data science projects is the [sklearn](https://scikit-learn.org/stable/index.html) library.  This libraries has implementations of dozens of different modelling techniques and also modules that can help to prepare the data and interpret the results.
# 

# To start we'll try to predict whether a flight will be delayed by more than 15 minutes.  For simplicity we'll deal with only five predictors (Day of the week, scheduled departure time, origin, destination, carrier)

# In[ ]:


# Start by importing a few key functions
from sklearn.metrics import accuracy_score, average_precision_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

delays_df = load_data('FlightDelays')
delays_df.head()


# In[ ]:


# TODO: It maybe helpful here to get a sense of the dataset and decide how best to prepare it for modelling


# ### Data Preparation
# Once you have gotten a sense of the data available, we need to do a little bit of preparation.  In this case, most of the fields are already in good shape.  Except that remember Naive Bayes requires that all the predictors be categorical variables.  So we'll need to ensure that all of our predictors are set as such.

# In[ ]:


# Before we run our model, let's figure out what a naive rule might tell us 
#  (That is, what is the split of ontime vs delayed)
delays_df['Flight Status'].value_counts()/len(delays_df)


# In[ ]:


# convert to categorical
delays_df.DAY_WEEK = delays_df.DAY_WEEK.astype('category')

# create hourly bins departure time 
delays_df.CRS_DEP_TIME = [round(t / 100) for t in delays_df.CRS_DEP_TIME]
delays_df.CRS_DEP_TIME = delays_df.CRS_DEP_TIME.astype('category')


# In[ ]:


# Assign the columns that we want to use as predictors and also the target variable
predictors = ['DAY_WEEK', 'CRS_DEP_TIME', 'ORIGIN', 'DEST', 'CARRIER']
outcome = 'Flight Status'

# It is quite common in many examples to create a two dimensional array (or dataframe) with the predictors called X
#  and the 1-dimensional array (or dataframe) with the targets called Y.
# By using a dataframe (or series in the case of Y), 
#  the index is preserved allowing a match back to the predictors, target and predicted value
X = pd.get_dummies(delays_df[predictors])
y = (delays_df[outcome] == 'delayed').astype(int)
classes = ['ontime', 'delayed']

# split into training and validation
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.40, random_state=1)

# run naive Bayes
delays_nb = MultinomialNB(alpha=0.1)
delays_nb.fit(X_train, y_train)

# predict probabilities
# We would predict probabilities if we want to use the cut-off methods
predProb_train = delays_nb.predict_proba(X_train)
predProb_valid = delays_nb.predict_proba(X_valid)

# predict class membership
# Otherwise we can simply just take the result
y_valid_pred = delays_nb.predict(X_valid)
y_train_pred = delays_nb.predict(X_train)

classificationSummary(y_train,y_train_pred, class_names=classes)


# In[ ]:


train_accuracy = accuracy_score(y_true=y_train,y_pred=y_train_pred).round(4)
validation_accuracy = accuracy_score(y_true=y_valid,y_pred=y_valid_pred).round(4)
print(f'Training Set Accuracy: {train_accuracy}')
print(f'Validation Set Accuracy: {validation_accuracy}')


# ## Your Turn - Automobile Accidents
# The file {download}`accidentsFull.csv <../data/accidentsFull.csv.` contains information on 42k actual accidents in the US in 2001.  There are three levels of injury provided NO INJURY, INJURY, FATALITY.  Your job, if you choose to accept it, is to use the predictors available to develop a model that can determine whether there was an injury at an accident (INJURY or FATALITY).
# 
# You can do the work right here in the following cells. To see one way to solve it you can check out [a solution here](335-ClassificationSolutions.ipynb).

# # Other Available Classification Algorithms
# The same techniques apply when using any other classification algorithm from the `sklearn` library.  The data is prepared, split, fit and then predicted.
# 
# ## Logistic Regression
# Logistic regression, despite its name, is a linear model for classification rather than regression. Logistic regression is also known in the literature as logit regression, maximum-entropy classification (MaxEnt) or the log-linear classifier. In this model, the probabilities describing the possible outcomes of a single trial are modeled using a [logistic function](https://en.wikipedia.org/wiki/Logistic_function).
# 
# ## Support Vector Machines
# (from [scikit-learning](https://scikit-learn.org/stable/modules/svm.html#classification))
# <br/>
# Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.
# 
# The advantages of support vector machines are:
# <br/>
# * Effective in high dimensional spaces.
# * Still effective in cases where number of dimensions is greater than the number of samples.
# * Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.
# * Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.
# 
# The disadvantages of support vector machines include:
# <br/>
# * If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.
# * SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).
# 
# ## Nearest Neighbors
# (from [scikit-learning](https://scikit-learn.org/stable/modules/svm.html#classification))
# <br/>
# Neighbors-based classification is a type of instance-based learning or non-generalizing learning: it does not attempt to construct a general internal model, but simply stores instances of the training data. Classification is computed from a simple majority vote of the nearest neighbors of each point: a query point is assigned the data class which has the most representatives within the nearest neighbors of the point.
# 
# ## Decision Trees
# (from [scikit-learning](https://scikit-learn.org/stable/modules/tree.html#tree))
# <br/>
# Decision Trees (DTs) are a non-parametric supervised learning method used for classification and regression. The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features. A tree can be seen as a piecewise constant approximation.
# 
# Some advantages of decision trees are:
# <br/>
# * Simple to understand and to interpret. Trees can be visualised.
# * Requires little data preparation. Other techniques often require data normalisation, dummy variables need to be created and blank values to be removed. Note however that this module does not support missing values.
# * The cost of using the tree (i.e., predicting data) is logarithmic in the number of data points used to train the tree.
# * Able to handle both numerical and categorical data. However scikit-learn implementation does not support categorical variables for now. Other techniques are usually specialised in analysing datasets that have only one type of * variable. See algorithms for more information.
# * Able to handle multi-output problems.
# * Uses a white box model. If a given situation is observable in a model, the explanation for the condition is easily explained by boolean logic. By contrast, in a black box model (e.g., in an artificial neural network), results may be more difficult to interpret.
# * Possible to validate a model using statistical tests. That makes it possible to account for the reliability of the model.
# * Performs well even if its assumptions are somewhat violated by the true model from which the data were generated.
# 
# The disadvantages of decision trees include:
# 
# * Decision-tree learners can create over-complex trees that do not generalise the data well. This is called overfitting. Mechanisms such as pruning, setting the minimum number of samples required at a leaf node or setting the  maximum depth of the tree are necessary to avoid this problem.
# * Decision trees can be unstable because small variations in the data might result in a completely different tree being generated. This problem is mitigated by using decision trees within an ensemble.
# * Predictions of decision trees are neither smooth nor continuous, but piecewise constant approximations as seen in the above figure. Therefore, they are not good at extrapolation.
# * The problem of learning an optimal decision tree is known to be NP-complete under several aspects of optimality and even for simple concepts. Consequently, practical decision-tree learning algorithms are based on heuristic  algorithms such as the greedy algorithm where locally optimal decisions are made at each node. Such algorithms cannot guarantee to return the globally optimal decision tree. This can be mitigated by training multiple trees in an ensemble learner, where the features and samples are randomly sampled with replacement.
# * There are concepts that are hard to learn because decision trees do not express them easily, such as XOR, parity or multiplexer problems.
# * Decision tree learners create biased trees if some classes dominate. It is therefore recommended to balance the dataset prior to fitting with the decision tree.

# # Resources
# [Worked solutions for classification problems](335-ClassificationSolutions.ipynb)
# 
# ## Other datasets suitable for classification tasks
# * {download}`Cleveland Heart Clinic <../data/HeartDisease_Cleveland.xlsx>` - predict whether a patient is likely to have heart disease
# * {download}`Universal Bank <../data/UniversalBank.csv>` - determine whether a customer should get a personal loan
# * {download}`Accidents <../data/accidentsFull.csv>` - useful for practicing on a multi-class classification
# * {download}`Riding lawnmower sales <../data/RidingMowers.csv>` - determine the best customers for a riding lawnmower company
# * {download}`Financial Condition of Banks <../data/banks.csv>` - classify the financial health of banks
# * {download}`Systems Admins <../data/SystemAdministrators.csv>` - can you identify the best systems admins
# * {download}`Competitive Auctions <../data/eBayAuctions.csv>` - find competitive auctions
