import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def entrenar_y_validar():
    # Carga de datos directa desde la URL para evitar errores de archivo no encontrado
    url = 'https://raw.githubusercontent.com/Darwin2016/dataset2022/main/dataSETS/affairs.csv'
    df = pd.read_csv(url)

    # Usamos las características que identificaste en tu taller
    used_features = ['yearsmarried', 'religiousness', 'education', 'occupation']
    X = df[used_features]
    y = df.affair

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Entrenamos el Random Forest (Basado en tu interés en Boosting/Ensamble)
    model = RandomForestClassifier(max_depth=3, n_estimators=20, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    return accuracy_score(y_test, y_pred)

if __name__ == "__main__":
    acc = entrenar_y_validar()
    print(f"Accuracy final del modelo: {acc}")
