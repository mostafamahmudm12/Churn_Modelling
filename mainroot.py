from fastapi import FastAPI,HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from utils.inference import predict_new
from utils.config import APP_NAME,VERSION,SECRET_KEY_TOKEN,Preprocessor,Forest_Models
from utils.CustumerData import CustmerData
app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False},title=APP_NAME,version=VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],

)

api_key_header=APIKeyHeader(name='X-API-Key')

async def verify_api_key(api_key:str=Depends(api_key_header)):
    if api_key!=SECRET_KEY_TOKEN:
        raise HTTPException(status_code=401,detail="Invalid API Key")
    return api_key
    

@app.get('/')
async def home():
    return {
        "Mesage":f'Welcome to {APP_NAME} API v{VERSION}',
    }

@app.post('/predict/forest', tags=['Models'])
async def predict_forest(data: CustmerData,api_key:str=Depends(verify_api_key)) -> dict:
    try:
        # Ensure Preprocessor and Forest_Models are initialized properly
        result = predict_new(data=data, preprocessor=Preprocessor, model=Forest_Models)
        return result
    except Exception as e:
        # Use detailed error messages for debugging if needed
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.post('/predict/XGoost', tags=['Models'])
async def predict_XGoost(data: CustmerData,api_key:str=Depends(verify_api_key)) -> dict:
    try:
        # Ensure Preprocessor and Forest_Models are initialized properly
        result = predict_new(data=data, preprocessor=Preprocessor, model=Forest_Models)
        return result
    except Exception as e:
        # Use detailed error messages for debugging if needed
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")