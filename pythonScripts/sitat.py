from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title="HP quote")

sitater = {
    1: "Yer a wizard Harry.",
    2: "I hope you're pleased with yourselves. We could all have been killed — or worse, expelled. Now if you don't mind, I'm going to bed.",
    3: "You're a little scary sometimes, you know that? Brilliant... but scary.",
    4: "It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.",
    5: "Fear of a name only increases fear of the thing itself.",
    6: "It is our choices, Harry, that show what we truly are, far more than our abilities.",
    7: "Dobby is free.",
    8: "Honestly, if you were any slower, you’d be going backward.",
    9: "I solemnly swear I am up to no good.",
    10: "It matters not what someone is born, but what they grow to be."
}

class Quote(BaseModel):
    quote: str

@app.get("/sitat",response_model=Quote)
def sitat():
    id = random.randint(1,len(sitater))
    return {"quote":sitater[id]}

@app.post("/sitat",response_model=Quote)
def add_sitat(data: Quote):
    new_id= len(sitater) + 1
    sitater[new_id]=data.quote
    return{
        "message":"Nytt sitat opprettet",
        "id":new_id
    }