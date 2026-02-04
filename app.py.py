import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

# 1. Carga de datos
url = 'https://raw.githubusercontent.com/Darwin2016/dataset2022/main/dataSETS/affairs.csv'
df = pd.read_csv(url, delimiter=',')

# 2. Preprocesamiento (Selección de características basada en tu análisis)
used_features = ['yearsmarried', 'religiousness', 'education', 'occupation']
X = df[used_features]
y = df.affair

# 3. División y Escalado
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Entrenamiento de Modelos
# Modelo 1: Regresión Logística
modelo_log = linear_model.LogisticRegression(C=0.03, solver='liblinear', max_iter=100, random_state=42)
modelo_log.fit(X_train_scaled, y_train)
y_pred_log = modelo_log.predict(X_test_scaled)

# Modelo 2: Árbol de Decisión
modelotree = DecisionTreeClassifier(max_depth=3)
modelotree.fit(X_train_scaled, y_train)
y_pred_tree = modelotree.predict(X_test_scaled)

# Modelo 3: Random Forest
modelRF = RandomForestClassifier(max_depth=3, n_estimators=20, random_state=42)
modelRF.fit(X_train_scaled, y_train)
y_pred_rf = modelRF.predict(X_test_scaled)

# 5. Función para que el Test de GitHub Actions pueda validar
def obtener_precision_modelo():
    # Retornamos la precisión del mejor modelo para el CI/CD
    return accuracy_score(y_test, y_pred_rf)

if __name__ == "__main__":
    print(f"Accuracy Logística: {accuracy_score(y_test, y_pred_log)}")
    print(f"Accuracy Árbol: {accuracy_score(y_test, y_pred_tree)}")
    print(f"Accuracy Random Forest: {obtener_precision_modelo()}")
