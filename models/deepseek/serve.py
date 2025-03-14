import torch
from flask import Flask, request, jsonify
from deepseek import DeepSeekR1  # สมมติว่าโมเดลของคุณอยู่ในโมดูล deepseek

app = Flask(__name__)

# โหลดโมเดล
model = DeepSeekR1()
model.load_state_dict(torch.load('path_to_your_model.pth'))
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_tensor = torch.tensor(data['input'])
    with torch.no_grad():
        output = model(input_tensor)
    return jsonify({'output': output.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)