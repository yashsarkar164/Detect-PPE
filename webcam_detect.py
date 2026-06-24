import os
from ultralytics import YOLO

model = YOLO("models/iocl_ppe.pt")

current_dir = os.getcwd()

model.predict(
    source=0,
    show=True,
    save=True,
    project=os.path.join(current_dir, "runs"),
    name="webcam",
    exist_ok=True,
    conf=0.25
)

print("Webcam Detection Stopped!")