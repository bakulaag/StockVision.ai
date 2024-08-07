
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


dataset = pd.read_csv('all_stocks_5yr.csv')
dataset['date'] = pd.to_datetime(dataset.date)
dataset.dropna(inplace=True)

x = dataset[['open', 'high', 'low', 'volume']]
y = dataset['close']


x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)


dataset.dropna(inplace=True)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


dataset = pd.read_csv('all_stocks_5yr.csv')
dataset['date'] = pd.to_datetime(dataset.date)
dataset.dropna(inplace=True)
dataset_train = dataset.head(1000)
dataset_test = dataset.iloc[1000:3000]

x_test = dataset_test[['open', 'high', 'low', 'volume']]
y_test = dataset_test['close']


regressor = LinearRegression()
regressor.fit(x_train, y_train)


predicted_prices = regressor.predict(x_test)


dataset_test_copy = dataset_test.copy()


dataset_test_copy['predicted_close'] = predicted_prices


print(dataset_test_copy[['date', 'close', 'predicted_close']])

def generate_rules(dataset_test_copy, y_test):
    rules = []
    for i in range(20):
        if dataset_test_copy['predicted_close'].iloc[i] > y_test.iloc[i]:
            rules.append("BUY")
        else:
            rules.append("SELL")
    return rules

rules = generate_rules(dataset_test_copy, y_test)
print(rules)


def predict_price(open_price, high_price, low_price, volume):
   
    user_input = pd.DataFrame({'open': [open_price],
                               'high': [high_price],
                               'low': [low_price],
                               'volume': [volume]})
    
    predicted_price = regressor.predict(user_input)
    return predicted_price[0]


open_price = float(input("Enter the open price: "))
high_price = float(input("Enter the high price: "))
low_price = float(input("Enter the low price: "))
volume = float(input("Enter the volume: "))

predicted_close = predict_price(open_price, high_price, low_price, volume)
print("Predicted closing price:", predicted_close)
