from pytube import YouTube

# Solicita la URL del video
url = "https://www.youtube.com/watch?v=P7yhVILTJvY"

try:
    yt = YouTube(url)

    # Muestra información del video
    print("Título:", yt.title)
    print("Descripción:", yt.description[:200])  # Limitamos la descripción

    # Seleccionamos el mejor stream disponible (video+audio)
    stream = yt.streams.get_highest_resolution()

    # Descarga el video
    print("Descargando...")
    stream.download()
    print("✅ Video descargado correctamente.")

except Exception as e:
    print("❌ Error al procesar el video:", e)
