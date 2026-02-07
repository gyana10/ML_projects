#Linear Regression 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

df=pd.read_csv("Salary_dataset.csv")
print(df.head())
X=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

regressor=LinearRegression()

regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)

print("Mean Squared Error:",mean_squared_error(y_test,y_pred))
print("R2 Score:",r2_score(y_test,y_pred))


plt.scatter(X_test,y_test,color='red',label='Actual')
plt.plot(X_test,y_pred,color='blue',label='Predicted')
plt.title('Actual vs Predicted')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()
