import os
from ultralytics import YOLO

model = YOLO("models/iocl_ppe.pt")

current_dir = os.getcwd()

results = model.predict(
    source="source_files/yash2.jpg",
    save=True,
    project=os.path.join(current_dir, "runs"),
    name="predict_image",
    exist_ok=True,
    conf=0.25
)

print("Image Detection Complete!")