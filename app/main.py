from fastapi import FastAPI, HTTPException, Depends
from app.schemas import TextInput
from app import services
import app.config

app = FastAPI()

def get_generator():
    return  services.generate_image_with_openai

@app.post("/generate-image/")
def generate(input: TextInput, generator = Depends(get_generator)):
    text = input.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    image_url = generator(text)
    return {
        "message": "Image generated successfully!",
        "image_url": image_url
    }
