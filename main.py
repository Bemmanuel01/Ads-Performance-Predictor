from flask  import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
    
@app.route('/predict', methods = ['POST'])
def predict():
    
    # Get JSON Request
    feat_data = request.json
    # Convert JSON to pandas DataFrame(Col_names)
    df = pd.DataFrame(feat_data)
    
    df = df.reindex(columns = col_names)
    
    # Predict
    prediction = list(model.predict(df))
    return jsonify({'prediction':str(prediction)})

# Loading the modeland the columns names
if __name__ == '__main__':
    model = joblib.load('final_model_two.pkl')
    col_names = joblib.load('col_names_two.pkl')
    
    app.run(debug = True)
