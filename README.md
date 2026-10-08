# Predicción de retrasos en TransMilenio

Actividad 5 del curso de Inteligencia Artificial (IBERO).
Usamos un árbol de decisión para predecir si un viaje de TransMilenio
va a tener retraso o no.

## Integrantes
- Mado Alexandra Millán Nieto
- Lizeth Vanessa Millán Nieto

## Archivos
- `generar_datos.py`: crea el dataset de muestra (300 viajes simulados)
- `datos_transmilenio.csv`: los datos generados
- `modelo.py`: entrena el árbol de decisión y muestra los resultados
- `Documento_Actividad5.docx`: descripción de los datos y pruebas realizadas

## Cómo ejecutarlo
1. Instalar las librerías: `pip install pandas scikit-learn`
2. Crear los datos: `python generar_datos.py`
3. Correr el modelo: `python modelo.py`

## Resultado
El modelo tuvo una exactitud de 0.67 con los datos de prueba.

