from ultralytics import YOLO
import cv2

# Carga el modelo (detección normal). Más adelante puedes usar 'yolov8n-pose.pt' para pose.
model = YOLO("yolov8n.pt")

# Abre la cámara (0 = cámara principal)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo leer el frame")
        break

    # Corre YOLO
    results = model(frame)

    # Dibuja resultados (cajas, etc.)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Webcam", annotated_frame)

    # Presiona 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
