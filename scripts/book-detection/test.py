from ultralytics import YOLO

model = YOLO("../models/best.pt")

results = model.predict(source="0", show=True, conf=0.6)

print(results)