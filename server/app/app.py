import uvicorn
from fastapi import FastAPI
import pydantic
from fastapi.middleware.cors import CORSMiddleware
from .webreader import webreader
class Data(pydantic.BaseModel):
    url : str
    query : str




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/explain")
def explain(data : Data):

    output = webreader(url_link=data.url,question_text=data.query)
    return {
        "output" : output["generated_answer"]
    }

