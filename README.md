# HFD_YOLO

Proyecto de detección usando **YOLOv8** con webcam y estimación de pose humana.  
Incluye scripts listos para ejecutar y configuración para macOS, Windows y Visual Studio Code.

---

## 📦 Contenido del repositorio

- `yolo_pose.py` — detección de pose humana (keypoints)
- `yolo_webcam.py` — detección estándar con webcam
- `yolov8n.pt` — pesos YOLOv8 normales
- `yolov8n-pose.pt` — pesos YOLOv8 de pose
- `requirements.txt` — dependencias del proyecto
- `.gitignore` — ignora `.venv/`, `.vscode/`, `__pycache__/`, etc.

---

# 🚀 1. Requisitos

- Python **3.10 o 3.11**
- Git instalado
- Webcam funcional
- (Opcional pero recomendado) Visual Studio Code

---

# 📂 2. Clonar el repositorio

## SSH (recomendado)
```bash
git clone git@github.com:filifloresb/HFD_YOLO.git
cd HFD_YOLO
HTTPS
bash
Copy code
git clone https://github.com/filifloresb/HFD_YOLO.git
cd HFD_YOLO
🐍 3. Crear y activar entorno virtual
macOS / Linux
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
Windows (PowerShell o CMD)
bash
Copy code
py -m venv .venv
.\.venv\Scripts\activate
Debes ver algo así en la terminal:

scss
Copy code
(.venv) user@machine HFD_YOLO %
📥 4. Instalar dependencias
Con el entorno virtual activado:

bash
Copy code
pip install --upgrade pip
pip install -r requirements.txt
▶️ 5. Ejecutar los scripts
Detección de pose humana
bash
Copy code
python yolo_pose.py
Detección solo con webcam
bash
Copy code
python yolo_webcam.py
Si la webcam no funciona, cambia el índice:
cv2.VideoCapture(0) → cv2.VideoCapture(1) o 2.

🛠️ 6. Configuración en VS Code (opcional)
Seleccionar intérprete Python
Abrir la carpeta del proyecto en VS Code

Ctrl+Shift+P / Cmd+Shift+P

Escribir Python: Select Interpreter

Elegir:

macOS/Linux:

bash
Copy code
.venv/bin/python
Windows:

Copy code
.venv\Scripts\python.exe
Archivo .vscode/settings.json
jsonc
Copy code
{
  // macOS / Linux
  "python.defaultInterpreterPath": ".venv/bin/python",
  "python.analysis.extraPaths": ["./"]

  // Para Windows, usar esta línea:
  // "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe"
}
📌 7. Notas importantes
La carpeta .venv/ NO se sube a GitHub (está ignorada).

Si instalas nuevas librerías, actualiza requirements.txt:

bash
Copy code
pip freeze > requirements.txt
Si macOS bloquea la cámara, ve a:
Preferencias del Sistema → Seguridad y Privacidad → Cámara

❗ 8. Problemas comunes
“No module named ultralytics”
No instalaste dependencias.
✔ Solución:

bash
Copy code
pip install -r requirements.txt
“Permission denied” al activar .venv en macOS
bash
Copy code
chmod +x .venv/bin/activate
Webcam no detectada
Cerrar apps que usen la cámara

Cambiar índice de la cámara

Revisar permisos del sistema

📁 9. Estructura del proyecto
Copy code
HFD_YOLO/
│── yolo_pose.py
│── yolo_webcam.py
│── yolov8n.pt
│── yolov8n-pose.pt
│── requirements.txt
│── .gitignore
└── .vscode/ (opcional)