HFD_YOLO

Proyecto de detección usando YOLOv8 con webcam y estimación de pose humana.
Incluye scripts listos para ejecutar y configuración para macOS, Windows y Visual Studio Code.

📦 Contenido del repositorio

yolo_pose.py — detección de pose humana (keypoints)

yolo_webcam.py — detección estándar con webcam

yolov8n.pt — pesos YOLOv8 normales

yolov8n-pose.pt — pesos YOLOv8 de pose

requirements.txt — dependencias del proyecto

.gitignore — ignora .venv/, .vscode/, __pycache__/, etc.

🚀 1. Requisitos

Python 3.10 o 3.11

Git instalado

Webcam funcional

(Opcional pero recomendado) Visual Studio Code

📂 2. Clonar el repositorio
SSH (recomendado)
git clone git@github.com:filifloresb/HFD_YOLO.git
cd HFD_YOLO

HTTPS
git clone https://github.com/filifloresb/HFD_YOLO.git
cd HFD_YOLO

🐍 3. Crear y activar entorno virtual
macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

Windows (PowerShell o CMD)
py -m venv .venv
.\.venv\Scripts\activate


Debes ver algo así en la terminal:

(.venv) user@machine HFD_YOLO %

📥 4. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

▶️ 5. Ejecutar los scripts
Detección de pose humana
python yolo_pose.py

Detección con webcam
python yolo_webcam.py


Si la webcam no funciona, cambia el índice:
cv2.VideoCapture(0) → cv2.VideoCapture(1) o 2.

🛠️ 6. Configuración en Visual Studio Code (opcional)
Seleccionar intérprete Python

Abrir la carpeta del proyecto en VS Code

Presionar Ctrl+Shift+P / Cmd+Shift+P

Buscar: Python: Select Interpreter

Seleccionar la ruta del entorno virtual:

macOS/Linux:

.venv/bin/python


Windows:

.venv\Scripts\python.exe

Archivo .vscode/settings.json
{
  "python.defaultInterpreterPath": ".venv/bin/python",
  "python.analysis.extraPaths": ["./"]

  // Para Windows, usar:
  // "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe"
}

📌 7. Notas importantes

La carpeta .venv/ NO debe subirse a GitHub.

Si instalas nuevas librerías, actualiza requirements.txt:

pip freeze > requirements.txt


Si macOS bloquea la cámara:
Preferencias del Sistema → Seguridad y Privacidad → Cámara

❗ 8. Problemas comunes
“No module named ultralytics”

Solución:

pip install -r requirements.txt

Error de permisos al activar .venv en macOS
chmod +x .venv/bin/activate

Webcam no detectada

Cerrar Zoom / Teams / OBS

Cambiar índice de cámara

Revisar permisos del sistema

📁 9. Estructura del proyecto
HFD_YOLO/
│── yolo_pose.py
│── yolo_webcam.py
│── yolov8n.pt
│── yolov8n-pose.pt
│── requirements.txt
│── .gitignore
└── .vscode/ (opcional)

🎉 ¡Listo!

Tu proyecto está completamente listo para correr en macOS y Windows, con entorno virtual, dependencias y scripts funcionando correctamente.