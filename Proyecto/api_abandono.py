from fastapi import FastAPI, UploadFile, File
import pandas as pd
import joblib
import io

app = FastAPI()

# Cargar el modelo
modelo = joblib.load("modelo_abandono.pkl")

@app.post("/predecir")
async def predecir_archivo(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    df_pred = df.drop(columns=["CustomerID"], errors="ignore")
    predicciones = modelo.predict(df_pred)
    df["Prediccion_Abandono"] = predicciones
    output = io.StringIO()
    df.to_csv(output, index=False)
    return {"archivo_csv": output.getvalue()}
