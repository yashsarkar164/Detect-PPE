# Detect-PPE
Gear Up for Safety!
# PPE Detection System using YOLOv8

## Requirements

* Python 3.13 or later

## Project Structure

```text
Detect PPE/
│
├── models/
│   └── iocl_ppe.pt
│
├── source_files/
│
├── image_detect.py
├── video_detect.py
├── webcam_detect.py
│
└── requirements.txt
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yashsarkar164/Detect-PPE.git
cd Detect-PPE
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Git Bash

```bash
source venv/Scripts/activate
```

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Image Detection

### 1. Place an image inside the `source_files` folder

Example:

```text
source_files/
└── yash.jpg
```

### 2. Update the image path inside `image_detect.py`

```python
source="source_files/yash.jpg"
```

### 3. Run

```bash
python image_detect.py
```

### Output

```text
runs/
└── predict_image/
```

---

## Video Detection

### 1. Place a video inside the `source_files` folder

Example:

```text
source_files/
└── video.mp4
```

### 2. Update the video path inside `video_detect.py`

```python
source="source_files/video.mp4"
```

### 3. Run

```bash
python video_detect.py
```

### Output

```text
runs/
└── predict_video/
```

---

## Webcam Detection

Run:

```bash
python webcam_detect.py
```

The webcam will open and perform real-time PPE detection.

### Output

```text
runs/
└── webcam/
```

---

## Detected Classes

* Hardhat
* Mask
* NO-Hardhat
* NO-Mask
* NO-Safety Vest
* Person
* Safety Cone
* Safety Vest
* Machinery
* Vehicle

---

## Model

The trained YOLOv8 model is located at:

```text
models/iocl_ppe.pt
```
