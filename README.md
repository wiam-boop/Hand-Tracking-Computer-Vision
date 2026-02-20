# ✨ Golden Hand Tracking Pen

<h2 align="center">Real-Time Hand Tracking Drawing System</h2>

<p align="center">
A real-time computer vision project that allows users to draw in the air using their index finger and erase using an open hand gesture.
</p>

---

## 🎥 Features

- ✍️ <b>Index finger only</b> → Smooth golden pen drawing  
- ✋ <b>Open hand</b> → Eraser mode  
- 👋 Real-time hand landmarks visualization  
- 🎯 Drawing activates only at close distance  
- 🧽 Smooth canvas overlay  

---

## 🛠️ Technologies Used

Python 3.x  
OpenCV  
MediaPipe  
NumPy  

---

<h2>📦 Installation</h2>

<pre>
pip install -r requirements.txt
</pre>

---

<h2>▶️ Run the Project</h2>

<pre>
python main.py
</pre>

Press <b>Q</b> to exit.

---

<h2>🧠 How It Works</h2>

Hand landmarks are detected using MediaPipe.  
Finger states determine drawing or erasing mode.  
A separate canvas layer is merged with the camera feed.  
Distance threshold controls natural writing activation.

---

<h3 align="center">👩‍💻 Created by Wiam</h3>
