# 🥋 HFD_YOLO

Proyecto de detección usando **YOLOv8** con webcam y estimación de **pose humana**.  
Incluye scripts listos para ejecutar y configuración para **macOS**, **Windows** y **Visual Studio Code**.

---

## 📦 Contenido del Repositorio

| Archivo              | Descripción                                |
|----------------------|--------------------------------------------|
| `yolo_pose.py`       | Detección de **pose humana** (keypoints)   |
| `yolo_webcam.py`     | Detección estándar con webcam              |
| `yolov8n.pt`         | Pesos YOLOv8 normales                      |
| `yolov8n-pose.pt`    | Pesos YOLOv8 de pose                       |
| `requirements.txt`   | Dependencias del proyecto                  |
| `.gitignore`         | Ignora `.venv/`, `.vscode/`, `__pycache__/`, etc. |

---

## 🚀 Requisitos

- Python **3.10 o 3.11**
- Git instalado
- Webcam funcional
- (Opcional) Visual Studio Code

---

## 📂 Clonar el Repositorio

### 🔐 SSH (recomendado)

```bash
git clone git@github.com:filifloresb/HFD_YOLO.git
cd HFD_YOLO
```

### 🌐 HTTPS

```bash
git clone https://github.com/filifloresb/HFD_YOLO.git
cd HFD_YOLO
```

---

## 🧪 Crear y Activar un Entorno Virtual

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell o CMD)

```bash
py -m venv .venv
.\.venv\Scriptsctivate
```

Cuando esté activado verás algo como:
```bash
(.venv) usuario@pc HFD_YOLO %
```

---

## 📥 Instalar Dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ Ejecutar los Scripts

### Detección de pose humana

```bash
python yolo_pose.py
```

### Detección estándar con webcam

```bash
python yolo_webcam.py
```

> ⚠️ Si la webcam no funciona, prueba cambiar el índice en el código:
```python
cv2.VideoCapture(0) → cv2.VideoCapture(1) o cv2.VideoCapture(2)
```

---

## 🧰 Configuración en Visual Studio Code

### Seleccionar intérprete Python

1. Abrir VS Code  
2. Presionar `Ctrl + Shift + P` (Windows/Linux) o `Cmd + Shift + P` (macOS)  
3. Buscar y seleccionar: `Python: Select Interpreter`

#### En macOS/Linux:
```bash
.venv/bin/python
```

#### En Windows:
```bash
.venv\Scripts\python.exe
```

### Archivo `.vscode/settings.json`

```json
{
  "python.defaultInterpreterPath": ".venv/bin/python",
  "python.analysis.extraPaths": ["./"]
}
```

> En Windows usar:
```json
{
  "python.defaultInterpreterPath": ".venv\Scripts\python.exe"
}
```

---

## 📌 Notas Importantes

- La carpeta `.venv/` **NO se sube a GitHub**.
- Para actualizar dependencias:
  ```bash
  pip freeze > requirements.txt
  ```
- Si macOS bloquea la webcam:  
  Ir a **Preferencias del Sistema → Seguridad y Privacidad → Cámara**.

---

## ❗ Problemas Comunes

### 🛑 “No module named ultralytics”

```bash
pip install -r requirements.txt
```

### 🛑 Error de permisos en macOS

```bash
chmod +x .venv/bin/activate
```

### 🛑 Webcam no detectada

- Cierra Zoom, Meet o Teams
- Cambia el índice de cámara en el código
- Revisa los permisos del sistema

---

## 📁 Estructura del Proyecto

```
HFD_YOLO/
├── yolo_pose.py           # Detección de pose humana (keypoints)
├── yolo_webcam.py         # Detección estándar con webcam
├── yolov8n.pt             # Pesos YOLOv8 normales
├── yolov8n-pose.pt        # Pesos YOLOv8 de pose humana
├── requirements.txt       # Dependencias del proyecto
├── .gitignore             # Ignora entorno virtual y archivos temporales
└── .vscode/               # Configuración opcional para Visual Studio Code
```