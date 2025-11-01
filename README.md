# Engine Detection AI

A Flask-based web application that uses AI-powered object detection to identify and highlight engine components in uploaded images. The app leverages Roboflow's pre-trained model for accurate detection and provides an intuitive web interface for users to upload images, analyze them, and download results.

## Features

- **Image Upload**: Drag-and-drop or click-to-upload interface for image files (JPG, PNG).
- **AI-Powered Detection**: Integrates with Roboflow's "auto_partes" model to detect engine components.
- **Visual Results**: Displays original and detected images with bounding boxes and confidence scores.
- **JSON Output**: Provides detailed detection results in JSON format for further analysis.
- **Download Options**: Download detected images with overlays or raw JSON data.
- **Responsive UI**: Modern, mobile-friendly interface built with Tailwind CSS.
- **Progress Tracking**: Real-time progress updates during analysis.

## Installation

### Prerequisites

- Python 3.7+
- A Roboflow API key (sign up at [roboflow.com](https://roboflow.com) if you don't have one)

### Setup

1. Clone or download this repository:
   ```bash
   git clone <repository-url>
   cd engine_detection_web
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Roboflow API key:
   - Open `app.py` and replace the `ROBOFLOW_API_KEY` variable with your actual API key:
     ```python
     ROBOFLOW_API_KEY = "your-api-key-here"
     ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Usage

1. **Upload an Image**: Click the upload area or drag-and-drop an image of an engine.
2. **Review**: Preview the selected image and ensure it's suitable for analysis.
3. **Analyze**: Click "Use & Analyze" to start the detection process.
4. **View Results**: Review the detected components, confidence scores, and JSON details.
5. **Download**: Save the overlay image or JSON data as needed.

## API Details

### POST /detect

Uploads an image and performs object detection.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: `file` (image file)

**Response:**
```json
{
  "uploaded_image": "static/uploads/filename.jpg",
  "detected_image": "static/uploads/detected_filename.jpg",
  "json": {
    "predictions": [
      {
        "x": 150,
        "y": 200,
        "width": 100,
        "height": 80,
        "confidence": 0.95,
        "class": "engine_component"
      }
    ],
    "time": 2.3
  }
}
```

## Project Structure

```
engine_detection_web/
├── app.py                 # Flask application and detection logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Main web interface
├── static/
│   ├── uploads/           # Uploaded images
│   └── detected/          # Processed images with detections
└── README.md              # This file
```

## Dependencies

- Flask: Web framework
- requests: HTTP client for Roboflow API
- opencv-python: Image processing and drawing bounding boxes
- numpy: Numerical operations (used by OpenCV)
- python-dotenv: Environment variable management (optional)

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -am 'Add new feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Troubleshooting

- **API Key Issues**: Ensure your Roboflow API key is valid and has access to the "auto_partes" model.
- **Large Files**: Images over 10MB may fail to upload. Resize or compress large images.
- **Detection Failures**: Ensure images are well-lit and show clear engine components for best results.

## Support

For issues or questions, please open an issue on the GitHub repository.
