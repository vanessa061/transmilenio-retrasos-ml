import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, confusion_matrix

# leo el csv que creamos antes
datos = pd.read_csv("datos_transmilenio.csv")

# convierto texto a números (el árbol no entiende palabras)
datos = pd.get_dummies(datos, columns=["estacion", "franja"])

# X = lo que sabemos, y = lo que queremos predecir
X = datos.drop("retraso", axis=1)
y = datos["retraso"]

# separo 80% para entrenar y 20% para probar
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# entreno el árbol (le pongo profundidad 4 para que no se complique)
arbol = DecisionTreeClassifier(max_depth=4, random_state=42)
arbol.fit(X_train, y_train)

# pruebo con los datos que no vio
pred = arbol.predict(X_test)

print("Exactitud:", accuracy_score(y_test, pred))
print("Matriz de confusión:")
print(confusion_matrix(y_test, pred))

# así se ve el árbol en forma de reglas
print(export_text(arbol, feature_names=list(X.columns)))