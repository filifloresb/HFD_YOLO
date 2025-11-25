# 🥋 HFD_YOLO

Proyecto de detección usando **YOLOv8** con webcam y estimación de **pose humana**.  
Incluye scripts listos para ejecutar y configuración para **macOS**, **Windows** y **Visual Studio Code**.

---

## 📦 Contenido del Repositorio

| Archivo | Descripción |
|--------|-------------|
| `yolo_pose.py` | Detección de **pose humana** (keypoints) |
| `yolo_webcam.py` | Detección estándar con webcam |
| `yolov8n.pt` | Pesos YOLOv8 normales |
| `yolov8n-pose.pt` | Pesos YOLOv8 de pose |
| `requirements.txt` | Dependencias del proyecto |
| `.gitignore` | Ignora `.venv/`, `.vscode/`, `__pycache__/`, etc. |

---

## 🚀 Requisitos

- Python **3.10 o 3.11**
- Git instalado
- Webcam funcional
- (Opcional) Visual Studio Code

---

## 📂 Clonar el Repositorio

### 🔐 SSH (recomendado)

git clone git@github.com:filifloresb/HFD_YOLO.git
cd HFD_YOLO

### 🌐 HTTPS
git clone https://github.com/filifloresb/HFD_YOLO.git
cd HFD_YOLO

---
## 🧪 Crear y Activar un Entorno Virtual

### macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

### Windows (PowerShell o CMD)
py -m venv .venv
.\.venv\Scripts\activate

Cuando esté activado verás algo como:
(.venv) usuario@pc HFD_YOLO %

---
## 📥 Instalar Dependencias
pip install --upgrade pip
pip install -r requirements.txt

---
## ▶️ Ejecutar los Scripts
### Detección de pose humana
python yolo_pose.py

---
## 🧰 Configuración en Visual Studio Code
Seleccionar intérprete Python

1. Abrir VS Code
2. Ctrl + Shift + P / Cmd + Shift + P
3. Elegir: Python: Select Interpreter
### macOS/Linux:
.venv/bin/python
### Windows:
.venv\Scripts\python.exe

### Archivo .vscode/settings.json
{
    "python.defaultInterpreterPath": ".venv/bin/python",
    "python.analysis.extraPaths": ["./"]
    // En Windows usar:
    // "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe"
}


## 📁 Estructura del Proyecto
HFD_YOLO/
│
├── yolo_pose.py
├── yolo_webcam.py
├── yolov8n.pt
├── yolov8n-pose.pt
├── requirements.txt
├── .gitignore
└── .vscode/ (opcional)
