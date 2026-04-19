import modelo

# CREAR EL ENTORNO VIRTUAL (si o si esta version)
# python -m venv .venv

# Habilitar el entorno virtual (en Windows)
# .venv\Scripts\activate   <-- Nota: Corregí el comando de activación para Windows
# En Mac/Linux sería: source .venv/bin/activate

# Instalar las dependencias (pip install tensorflow numpy)

def prediccion(modelo_entrenado):
    resultado = modelo_entrenado.predict([100.0])
    print(f"La temperatura 100.0°C es igual a {resultado[0][0]:.2f}°F")

if _name_ == "_main_":
    modelo_red_neuronal, historial = modelo.entrenar_modelo()
    # graficas.graficas(historial)
    
    # Aquí es donde le pasamos el 'modelo' en lugar del 'historial'
    prediccion(modelo_red_neuronal)