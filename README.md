# ✋ Hand-Controlled Presentation

A computer vision-powered presentation system that lets you control slides, draw multi-color annotations, and point at content — all using **hand gestures** captured through your webcam. No keyboard, no mouse, no clicker needed.

---

## 🎥 Demo

👉 Watch the project in action:

https://github.com/user-attachments/assets/7582a4ef-aaa9-4549-9f77-95e90f722f32

---

## 🚀 Features

### 🎯 Core Controls
- **Slide Navigation** — Move forward and backward through slides using simple one-finger gestures
- **Gesture Threshold Zone** — A visual green line separates the navigation zone (above) from the drawing zone (below) to prevent accidental slide changes

### 🖊️ Annotation System
- **Freehand Drawing** — Draw directly on slides using your index finger
- **Multi-Color Support** — Choose from **4 annotation colors**: 🔴 Red, 🟢 Green, 🔵 Blue, 🟡 Yellow
- **Color Cycling** — Switch between colors on-the-fly with a gesture (thumb + pinky)
- **Undo Annotations** — Remove the last drawn stroke with a three-finger gesture
- **Per-Slide Annotations** — Annotations reset automatically when navigating to a new slide

### 🔴 Pointer Mode
- **Virtual Laser Pointer** — Highlight areas on your slide with a colored circle that follows your finger
- **Color-Aware Pointer** — The pointer color matches your currently selected annotation color

### 📊 On-Screen HUD
- **Slide Counter** — Semi-transparent overlay showing current slide number and total (e.g., `3 / 7`)
- **Color Indicator** — A colored rectangle with label in the bottom-left showing the active annotation color
- **Webcam Thumbnail** — Live webcam feed displayed as a small overlay on the slide for presenter visibility

### ⚙️ Smart Gesture Handling
- **Debounced Input** — Button press delay prevents accidental repeated triggers
- **Separate Color Change Cooldown** — Independent debounce timer for color switching
- **Auto-Reset** — Annotations and drawing state automatically clear on slide transitions

---

## 🧠 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core application language |
| **OpenCV** (`cv2`) | Image processing, display windows, drawing primitives |
| **CVZone** | Hand detection and finger tracking via `HandDetector` |
| **NumPy** | Array operations for image manipulation |

---

## 📂 Project Structure

```
Hand-Controlled-Presentation/
│
├── main.py                # Main application — gesture detection, drawing, and slide rendering
├── presentataion/         # Default slide deck (PNG images, sorted alphabetically)
│   ├── 0_guide.png        # Gesture guide reference slide
│   ├── 1.png – 6.png      # Presentation slides
├── presentataion-3/       # Alternate slide deck (swap by changing folderPath in main.py)
│   ├── 0_guide.png
│   ├── 1.png – 6.png
└── README.md              # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Arpit-Padmani/Hand-Gesture-Presentation.git
cd Hand-Gesture-Presentation
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install opencv-python cvzone numpy
```

---

## ▶️ How to Run

```bash
python main.py
```

### Prerequisites
- ✅ Webcam connected and accessible
- ✅ Slide images (PNG) placed inside the `presentataion` folder
- ✅ Slides are loaded in **sorted alphabetical order** — name them `1.png`, `2.png`, etc.

### Switching Slide Decks
To use a different slide folder, update the `folderPath` variable in `main.py`:
```python
folderPath = "presentataion-3"  # Change to your desired folder
```

### Exiting
Press **`Q`** to quit the application.

---

## ✋ Gesture Controls

| Fingers | Gesture | Action |
|---------|---------|--------|
| 👍 `[1,0,0,0,0]` | Thumb only | **Previous Slide** *(hand must be above green line)* |
| 🤙 `[0,0,0,0,1]` | Pinky only | **Next Slide** *(hand must be above green line)* |
| ✌️ `[0,1,1,0,0]` | Index + Middle | **Pointer Mode** — shows a colored circle on the slide |
| ☝️ `[0,1,0,0,0]` | Index only | **Draw Annotation** — freehand drawing on the slide |
| 🤟 `[0,1,1,1,0]` | Index + Middle + Ring | **Undo Last Annotation** — removes the most recent stroke |
| 🤙 `[1,0,0,0,1]` | Thumb + Pinky | **Cycle Annotation Color** — Red → Green → Blue → Yellow → Red… |

> **Note:** Slide navigation gestures (Previous/Next) only activate when your hand is **above the green threshold line** (top ~300px of the camera frame) to avoid accidental triggers while drawing.

---

## 📸 How It Works

1. **Webcam Capture** — Captures video at **1280×720** resolution with horizontal flip for natural mirror view
2. **Hand Detection** — CVZone's `HandDetector` identifies one hand with **80% confidence threshold**
3. **Finger State Analysis** — `fingersUp()` returns a 5-element list `[thumb, index, middle, ring, pinky]` indicating which fingers are raised
4. **Gesture Mapping** — Finger combinations map to specific actions (navigation, drawing, pointer, undo, color change)
5. **Coordinate Mapping** — Index fingertip (landmark #8) coordinates are clamped to slide boundaries for accurate drawing
6. **Annotation Rendering** — Stored drawing points are rendered as connected lines with per-stroke color tracking
7. **HUD Compositing** — Slide counter, color indicator, and webcam thumbnail are overlaid onto the slide display

---

## ⚠️ Tips for Best Performance

- 💡 **Good lighting** — Ensure your hand is well-lit for reliable detection
- 📷 **Stay in frame** — Keep your hand fully visible within the camera view
- 🖼️ **Clean background** — Avoid cluttered backgrounds for better hand tracking accuracy
- 🖐️ **Clear gestures** — Make distinct finger positions; partially raised fingers may cause misdetection
- ⏱️ **Gesture cooldown** — Wait briefly between gestures (~0.3s) to allow the debounce timer to reset

---

## 💡 Future Improvements

- 🔍 Gesture-based zoom and pan
- 📄 Direct PowerPoint / PDF file support
- 🖐️🖐️ Multi-hand support (e.g., two-hand gestures)
- 🎙️ Voice + gesture hybrid control
- 💾 Save annotated slides as images
- 🎨 Adjustable pen thickness via gesture
- ⌨️ Keyboard shortcuts as fallback controls

---

## 🙌 Acknowledgements

- [**CVZone**](https://github.com/cvzone/cvzone) — Simplified hand tracking module built on top of MediaPipe
- [**OpenCV**](https://opencv.org/) — Industry-standard computer vision library
- [**MediaPipe**](https://mediapipe.dev/) — Google's framework powering the underlying hand landmark detection

---

## 📌 Author

**Arpit Padmani**
AI/ML Enthusiast | Computer Vision Learner

[![GitHub](https://img.shields.io/badge/GitHub-Arpit--Padmani-181717?style=flat&logo=github)](https://github.com/Arpit-Padmani)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it with others!
