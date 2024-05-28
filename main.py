from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.yaml")  # build a new model from scratch


# Use model
model.train(data="config.yaml", epochs=1)  # train  model
