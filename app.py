from flask import Flask, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    # Create a sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85.5, 90.0, 95.0]
    }
    df = pd.DataFrame(data)
    
    # Perform a simple numpy operation
    df['Age_Squared'] = np.square(df['Age'])

    # Convert DataFrame to JSON and return
    return jsonify(df.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
