from ultralytics import YOLO
import numpy as np
import cv2
import time


# 1) Cargar modelo de pose
model = YOLO("yolov8n-pose.pt")

# 2) Abrir la cámara
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

last_print_time = 0
PRINT_INTERVAL = 4   # segundos


while True:
    # 1. LEER FRAME DE LA CÁMARA
    ret, frame = cap.read()      # Lee un frame de la webcam
    if not ret:                  # Si no se pudo leer, salimos
        break


    # 2. CORRER YOLO POSE SOBRE EL FRAME
    results = model(frame, verbose=False) # YOLO procesa la imagen (detección + keypoints) Escribimos false para que no imprima en la terminal el log de velocidad de cada frame
    r = results[0]               # Obtenemos los resultados del único frame

    
    # 3. OBTENER LOS KEYPOINTS DEL CUERPO

    # r.keypoints contiene los puntos detectados
    # r.keypoints.xy es un arreglo [personas, keypoints, (x,y)]
    if r.keypoints is not None:
        kpts = r.keypoints.xy
        if len(kpts) > 0:
            persona0 = kpts[0].cpu().numpy()

            # Keypoints que vamos a usar -- Los keyponts se encuentran definidos en https://docs.ultralytics.com/tasks/pose-detection/#keypoints
            left_shoulder = persona0[5]   # (x, y)
            left_hip      = persona0[11]  # (x, y)
            left_wrist    = persona0[9]   # (x, y)  -> brazo extendido

            # Vector del torso (hombro -> cadera)
            v_torso = left_hip - left_shoulder

            # Vector del brazo (hombro -> muñeca)
            v_arm = left_wrist - left_shoulder

            # Ángulo entre torso y brazo en el hombro 
            dot = np.dot(v_torso, v_arm)
            mag_torso = np.linalg.norm(v_torso)
            mag_arm = np.linalg.norm(v_arm)

            cos_theta = dot / (mag_torso * mag_arm + 1e-6)
            angle_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))
            angle_deg = np.degrees(angle_rad)

            # Imprimir solo cada X segundos
            current_time = time.time()
            if current_time - last_print_time >= PRINT_INTERVAL:
                print("Ángulo brazo–torso (grados):", angle_deg)
                last_print_time = current_time


    # 5) Dibujar caja + esqueleto en la imagen
    annotated_frame = r.plot()

    # 6) Mostrar ventana
    cv2.imshow("YOLO Pose - Webcam", annotated_frame)

    # 7) Salir si presionas 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
