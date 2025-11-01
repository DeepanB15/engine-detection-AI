from flask import Flask, render_template, request, jsonify
import os
import requests
import cv2

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"

# Roboflow model URL + API key
ROBOFLOW_API_KEY = "ExZHv9JP9C9QUCWMABEL"
MODEL_URL = "https://detect.roboflow.com/auto_partes-wk5ey/1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"})

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Send image to Roboflow inference API
    with open(filepath, 'rb') as f:
        response = requests.post(
            f"{MODEL_URL}?api_key={ROBOFLOW_API_KEY}",
            files={'file': f}
        )

    if response.status_code != 200:
        return jsonify({
            "error": "Failed to reach Roboflow",
            "status": response.status_code
        })

    try:
        data = response.json()
    except Exception:
        return jsonify({
            "error": "Invalid response from Roboflow",
            "text": response.text
        })

    # Draw bounding boxes with confidence values
    img = cv2.imread(filepath)
    for pred in data.get('predictions', []):
        x, y = int(pred['x']), int(pred['y'])
        w, h = int(pred['width']), int(pred['height'])
        conf = pred['confidence']
        x1, y1 = int(x - w / 2), int(y - h / 2)
        x2, y2 = int(x + w / 2), int(y + h / 2)

        # Draw rectangle
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{conf * 100:.1f}%"

        # Label box
        (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        cv2.rectangle(img, (x1, y1 - th - 4), (x1 + tw, y1), (0, 255, 0), -1)
        cv2.putText(img, label, (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], "detected_" + file.filename)
    cv2.imwrite(output_path, img)

    return jsonify({
        "uploaded_image": filepath.replace("\\", "/"),
        "detected_image": output_path.replace("\\", "/"),
        "json": data
    })

if __name__ == '__main__':
    app.run(debug=True)
