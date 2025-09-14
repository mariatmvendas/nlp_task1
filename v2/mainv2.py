from fastapi import FastAPI
from pydantic import BaseModel
from afinn import Afinn
from langdetect import detect

app_v2 = FastAPI(title="Task 1 - Sentiment Analysis")

class TextInput(BaseModel):
    text: str

@app_v2.post("/v1/sentiment")
def analyze_sentiment(text: TextInput):
    lowered_text = text.text.lower()

    lang = detect(lowered_text)
    afinn = Afinn(language=lang) 

    afinn._dict["dry"] = -3 
    score = afinn.score(lowered_text)
    
    return {"Sentiment score" : {score}}
