# Don't need to execute this code, it's just an example of how to train a model using Ultralytics YOLOv8

from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(data='/path/to/data.yaml', epochs=50, imgsz=640)

results = model.val(data='/path/to/data.yaml', split='test')

results.plot()

model.export(format='onnx')