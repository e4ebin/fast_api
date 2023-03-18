from fastapi import FastAPI,Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from utils import predict_hd

class Data(BaseModel):
    age: int
    sex: int
    chest_pain:int
    trestbps:int
    chol:int
    fbs:int
    restecg:int
    thalach:int
    exang:int
    oldpeak:int
    slope:int
    ca:int
    thal:int

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/active")
def read_root():
    return {"status": "active"}

@app.post("/predict")
async def get_data(data:Data,response: Response):
    try:
        _prediction=predict_hd(data.age,data.sex,data.chest_pain,data.trestbps,data.chol,data.fbs,data.restecg,data.thalach,data.exang,data.oldpeak,data.slope,data.ca,data.thal)
        if _prediction[0]==0:
            return {"res":0} 
        else:
            return {"res":1}
    except:
        response.status_code = 500
        return {"error":"something went wrong!,Try again later"}
