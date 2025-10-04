# 🌧️ Heavy Rain Simulation (OpenGL + Python)

**Heavy Rain** is a simple OpenGL-based animation project written in **Python (PyOpenGL + GLUT)**.  
It simulates **falling raindrops** with adjustable wind direction and includes a **house drawing** that acts as the background scene.  
The simulation supports day/night switching and user interaction with keyboard controls.

---

## 🖼️ Animation Preview

<p align="center">
  <img src="animation_shots/Task 1 ss 1.PNG" width="45%" />
  <img src="animation_shots/Task 1 ss 2.PNG" width="45%" />
</p>
<p align="center">
  <img src="animation_shots/Task 1 ss 3.PNG" width="45%" />
  <img src="animation_shots/Task 1 ss 4.PNG" width="45%" />
</p>
<p align="center">
  <img src="animation_shots/Task 1 ss 5.PNG" width="45%" />
  <img src="animation_shots/Task 1 ss 6.PNG" width="45%" />
</p>
<p align="center">
  <img src="animation_shots/Task 1 ss 7.PNG" width="45%" />
  <img src="animation_shots/Task 1 ss 8.PNG" width="45%" />
</p>

---

## ✨ Features
- 🌧️ Continuous **raindrop simulation** with animation.  
- 🏠 A **house structure** drawn with OpenGL primitives (lines, triangles, points).  
- 🌞 Switch between **day mode** and **night mode** using the keyboard.  
- 💨 Change **rain direction** (left / right) with arrow keys.  
- 🎨 Adjustable colors for background and house.  

---

## 🎮 Controls

- **Arrow Keys**  
  - `←` : Tilt rain towards the left  
  - `→` : Tilt rain towards the right  

- **Keyboard Keys**  
  - `n` : Switch towards **night mode**  
  - `d` : Switch towards **day mode**  

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/EbrerRamen/heavy-rain-simulation.git
   cd heavy-rain-simulation

2. Install dependencies:
   ```bash
   pip install PyOpenGL PyOpenGL_accelerate
   
3. run the simulation:
   ```bash
   python HouseRain.py

---

## Requirements 
  - Python 3.x
  - PyOpenGL
  - PyOpenGL_accelerate
  - GLUT (usually included with PyOpenGL)

##💡 Enjoy the rain effect and have fun experimenting with OpenGL!
