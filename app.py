from flask import Flask, render_template, request # type: ignore
import pandas as pd # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore
from sklearn.model_selection import train_test_split # type: ignore

# Load the dataset and train the model (same code as before)
# dataset = pd.read_csv('rough\all_stocks_5yr.csv')
dataset = pd.read_csv('all_stocks_5yr.csv')

dataset['date'] = pd.to_datetime(dataset.date)
dataset.dropna(inplace=True)

x = dataset[['open', 'high', 'low', 'volume']]
y = dataset['close']

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)


# Create Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        open_price = float(request.form['open'])
        high_price = float(request.form['high'])
        low_price = float(request.form['low'])
        volume = float(request.form['volume'])
        
        predicted_close = predict_price(open_price, high_price, low_price, volume)
        
        return render_template('result.html', predicted_close=predicted_close)
    
def predict_price(open_price, high_price, low_price, volume):
    user_input = pd.DataFrame({'open': [open_price],
                               'high': [high_price],
                               'low': [low_price],
                               'volume': [volume]})
    
    predicted_price = regressor.predict(user_input)
    return predicted_price[0]

if __name__ == '__main__':
    app.run(debug=True)
