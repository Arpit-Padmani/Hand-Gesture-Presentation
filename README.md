# ✋ Hand-Controlled Presentation

A computer vision-based presentation system that allows you to control slides using **hand gestures** — no keyboard, no mouse, just your hand in the air.

---

## 🚀 Features

* 👉 Navigate slides using hand gestures
* 👈 Go to previous/next slide
* 🖊️ Draw annotations on slides in real-time
* 🔴 Laser pointer (virtual) using finger tracking
* ❌ Undo annotations with gesture
* 🎥 Live webcam feed overlay

---

## 🧠 Tech Stack

* Python
* OpenCV
* CVZone (Hand Tracking Module)
* NumPy

---

## 📂 Project Structure

```
Hand-Controlled-Presentation/
│
├── presentataion/        # Folder containing slide images
├── main.py               # Main application file
├── README.md             # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```bash
pip install opencv-python cvzone numpy
```

---

## ▶️ How to Run

```bash
python main.py
```

Make sure:

* Your webcam is connected
* Slides are placed inside the `presentataion` folder

---

## ✋ Gesture Controls

| Gesture                   | Action          |
| ------------------------- | --------------- |
| 👍 Thumb up               | Previous Slide  |
| 👆 Pinky up               | Next Slide      |
| ✌️ Index + Middle         | Pointer Mode    |
| ☝️ Index finger           | Draw Annotation |
| 🖐️ Index + Middle + Ring | Undo Annotation |

---

## 📸 How It Works

* Uses **hand landmark detection** to track finger positions
* Maps finger movement to screen coordinates
* Detects gestures based on finger states
* Applies actions like slide navigation or drawing

---

## ⚠️ Notes

* Ensure good lighting for accurate hand detection
* Keep your hand within camera frame
* Avoid cluttered backgrounds for better tracking

---

## 💡 Future Improvements

* Add gesture-based zoom
* Support for PowerPoint/PDF directly
* Multi-hand support
* Voice + gesture hybrid control
* Save annotated slides

---

## 🙌 Acknowledgements

* CVZone for simplifying hand tracking
* OpenCV for computer vision processing

---

## 📌 Author

**Arpit Padmani**
AI/ML Enthusiast | Computer Vision Learner

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it with others!
