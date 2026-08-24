import cv2
import os
import tkinter as tk
from tkinter import filedialog, simpledialog
from datetime import datetime


# ==========================================
# Inicializar Tkinter
# ==========================================

root = tk.Tk()
root.withdraw()


# ==========================================
# Seleccionar varios vídeos
# ==========================================

video_paths = filedialog.askopenfilenames(
    title="Selecciona los vídeos",
    filetypes=[
        ("Vídeos", "*.mp4 *.avi *.mov *.mkv *.webm"),
        ("Todos los archivos", "*.*")
    ]
)

if not video_paths:
    print("No se seleccionaron vídeos.")
    exit()


# ==========================================
# Seleccionar carpeta de destino
# ==========================================

save_directory = filedialog.askdirectory(
    title="Selecciona la carpeta donde guardar los frames"
)

if not save_directory:
    print("No se seleccionó una carpeta de destino.")
    exit()


# ==========================================
# Solicitar intervalo de extracción
# ==========================================

while True:

    interval = simpledialog.askfloat(
        "Intervalo de extracción",
        "¿Cada cuántos segundos deseas extraer un fotograma?",
        initialvalue=2.0,
        minvalue=0.5
    )

    # Si el usuario cancela
    if interval is None:
        print("Operación cancelada.")
        exit()

    # Validar intervalo
    if interval >= 0.5:
        break


# ==========================================
# Crear carpeta "frames"
# ==========================================

frames_directory = os.path.join(
    save_directory,
    "frames"
)

os.makedirs(frames_directory, exist_ok=True)


# ==========================================
# Contadores y datos
# ==========================================

frame_number = 1

video_results = []


# ==========================================
# Procesar cada vídeo
# ==========================================

for video_index, video_path in enumerate(
    video_paths,
    start=1
):

    print("\n")
    print(
        f"Procesando vídeo "
        f"{video_index} de {len(video_paths)}..."
    )

    print(
        f"Archivo: "
        f"{os.path.basename(video_path)}"
    )


    # ------------------------------------------
    # Abrir vídeo
    # ------------------------------------------

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():

        print(
            "ERROR: No se pudo abrir el vídeo."
        )

        continue


    # ------------------------------------------
    # Obtener información del vídeo
    # ------------------------------------------

    fps = cap.get(cv2.CAP_PROP_FPS)

    total_frames = int(
        cap.get(cv2.CAP_PROP_FRAME_COUNT)
    )

    duration = (
        total_frames / fps
        if fps > 0
        else 0
    )


    # ------------------------------------------
    # Extraer fotogramas
    # ------------------------------------------

    current_time = 0.0

    frames_this_video = 0


    while current_time <= duration:

        # Posicionar el vídeo
        cap.set(
            cv2.CAP_PROP_POS_MSEC,
            current_time * 1000
        )

        success, frame = cap.read()

        if not success:
            break


        # ------------------------------------------
        # Crear nombre del fotograma
        # ------------------------------------------

        filename = (
            f"frame_{frame_number:04d}.jpg"
        )

        output_path = os.path.join(
            frames_directory,
            filename
        )


        # ------------------------------------------
        # Guardar fotograma
        # ------------------------------------------

        cv2.imwrite(
            output_path,
            frame
        )


        print(
            f"Extraído: "
            f"{filename} "
            f"({current_time:.2f} s)"
        )


        # ------------------------------------------
        # Actualizar contadores
        # ------------------------------------------

        frame_number += 1

        frames_this_video += 1

        current_time += interval


    # ------------------------------------------
    # Cerrar vídeo
    # ------------------------------------------

    cap.release()


    # ------------------------------------------
    # Guardar información del vídeo
    # ------------------------------------------

    video_results.append({
        "name": os.path.basename(video_path),
        "fps": fps,
        "total_frames": total_frames,
        "duration": duration,
        "frames_extracted": frames_this_video
    })


# ==========================================
# Construir reporte
# ==========================================

report_lines = []


report_lines.append(
    "================================================================="
)

report_lines.append(
    "                    RESULTADOS DEL PROCESAMIENTO"
)

report_lines.append(
    "================================================================="
)

report_lines.append("")

report_lines.append(
    f"Intervalo de extracción: {interval:.2f} segundos"
)

report_lines.append("")


# ==========================================
# Información detallada de cada vídeo
# ==========================================

for index, result in enumerate(
    video_results,
    start=1
):

    report_lines.append(
        "-----------------------------------------------------------------"
    )

    report_lines.append(
        f"Vídeo {index}"
    )

    report_lines.append(
        "-----------------------------------------------------------------"
    )

    report_lines.append(
        f"Archivo: {result['name']}"
    )

    report_lines.append(
        f"FPS: {result['fps']:.2f}"
    )

    report_lines.append(
        f"Fotogramas: {result['total_frames']}"
    )

    report_lines.append(
        f"Duración: {result['duration']:.2f} segundos"
    )

    report_lines.append(
        f"Frames extraídos: {result['frames_extracted']}"
    )

    report_lines.append("")


# ==========================================
# Resumen
# ==========================================

report_lines.append(
    "================================================================="
)

report_lines.append(
    "RESUMEN"
)

report_lines.append(
    "================================================================="
)

report_lines.append("")

report_lines.append(
    f"Vídeos procesados: {len(video_results)}"
)

report_lines.append(
    f"Total de fotogramas: {frame_number - 1}"
)

report_lines.append("")


# ==========================================
# Ruta de guardado
# ==========================================

report_lines.append(
    "================================================================="
)

report_lines.append(
    "RUTA DE GUARDADO"
)

report_lines.append(
    "================================================================="
)

report_lines.append("")

report_lines.append(
    frames_directory
)

report_lines.append("")


# ==========================================
# Nombre del reporte
# ==========================================

timestamp = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)

report_filename = (
    f"reporte_frames_{timestamp}.txt"
)

report_path = os.path.join(
    save_directory,
    report_filename
)


# ==========================================
# Guardar reporte TXT
# ==========================================

with open(
    report_path,
    "w",
    encoding="utf-8"
) as report_file:

    report_file.write(
        "\n".join(report_lines)
    )


# ==========================================
# Mostrar reporte en pantalla
# ==========================================

print("\n")

print(
    "\n".join(report_lines)
)

print(
    f"Reporte guardado en:\n{report_path}"
)

print("\n")
print(
    "================================================================="
)

print(
    "PROCESAMIENTO FINALIZADO"
)

print(
    "================================================================="
)
