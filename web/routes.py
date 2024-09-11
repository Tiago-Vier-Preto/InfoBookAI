from flask import Flask, render_template, Response
import cv2
import torch
import threading
from ultralytics import YOLO

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = YOLO("../models/best.pt").to(device)

def configure_routes(app):
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/video_feed')
    def video_feed():
        return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


def generate_frames():
    camera = cv2.VideoCapture(0) # Use 0 for the default camera
    
    while True:
        success, frame = camera.read()
        frame = cv2.resize(frame, (640, 480))  

        if not success:
            break
        else:
            results = model(frame, conf=0.6, iou=0.45)
            
            # Draw the bounding boxes
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  
                    conf = box.conf[0]  

                    label = f"Livro: {conf:.2f}"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')