import sys
import os
import pymongo
import certifi
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging  
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.constants.training_pipeline import DATA_INGESTION_COLLECTION_NAME, DATA_INGESTION_DATABASEE_NAME
from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file, load_object

# Load environment variables
load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")
print("MongoDB URL:", mongo_db_url)  # Debug: Check URL in logs

# MongoDB connection with CA certificate
ca = certifi.where()
client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
database = client[DATA_INGESTION_DATABASEE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

# FastAPI application
app = FastAPI()
origins = ["*"]

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="./templates")

# Route for API documentation redirection
@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

# Training Route
@app.get("/train")
async def train_route():
    try:
        training_pipeline = TrainingPipeline()
        training_pipeline.run_pipeline()
        return Response(">>Training Successful<<")
    except Exception as e:
        logging.error(f"Exception in train_route: {e}")  # Log full error details
        raise NetworkSecurityException(e, sys)

    
    
@app.post("/predict")
async def predict_route(request: Request,file:UploadFile=File(...)):
    try:
        df=pd.read_csv(file.file)
        preprocesssor=load_object("final_model/preprocessor.pkl")
        final_model=load_object("final_model/model.pkl")
        network_model=NetworkModel(preprocessor=preprocesssor,model=final_model)
        print(df.iloc[0])
        y_pred=network_model.predict(df)
        df['predicted_column']=y_pred    
        print(df["predicted_column"])
        os.makedirs('prediction_output', exist_ok=True)
        df.to_csv('prediction_output/output.csv')
        table_html = df.to_html(classes="table table-striped")
        return templates.TemplateResponse("table.html", {"request": request, "table_html": table_html})
    except Exception as e:
        logging.error(f"Exception in predict_route: {e}")  # Log full error details
        raise NetworkSecurityException(e, sys)
    
    

if __name__ == "__main__":
    # Listen on all network interfaces (0.0.0.0) for cloud access
    app_run(app, host="0.0.0.0", port=8000)