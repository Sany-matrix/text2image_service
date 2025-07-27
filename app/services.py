from openai import OpenAI
from fastapi import HTTPException
import os


def generate_image_with_openai(prompt: str) -> str:
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.images.generate(
            model = "dall-e-2",
            prompt=prompt,
            n=1,
            size="512x512"
        )
        return response.data[0].url
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Image generation failed: {str(e)}")

    
    
    

    