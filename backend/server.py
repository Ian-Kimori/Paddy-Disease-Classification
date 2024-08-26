from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the pre-trained model from an .h5 file
MODEL_PATH = r"C:\Users\IAN KIMORI\Desktop\Project\Paddy Disease Classification\models h5v2\paddy1.h5"
MODEL = tf.keras.models.load_model(MODEL_PATH)

# Define the class names
CLASS_NAMES = ["bacterial_leaf_blight", "bacterial_leaf_streak", "bacterial_panicle_blight", "blast", "brown_spot", "dead_heart", "downy_mildew", "hispa", "normal", "tungro"]

@app.get("/ping")
async def ping():
    return {"message": "Hello, I am alive"}

def read_file_as_image(data) -> np.ndarray:
    try:
        image = np.array(Image.open(BytesIO(data)))
        return image
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading image file: {e}")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image = read_file_as_image(await file.read())
        img_batch = np.expand_dims(image, 0)
        
        # Resize images to (224, 224)
        resized_images = [np.array(Image.fromarray(img).resize((224, 224))) for img in img_batch]
        resized_img_batch = np.array(resized_images)
        
        # Predict using the model
        predictions = MODEL.predict(resized_img_batch)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])
        
        return {
            'class': predicted_class,
            'confidence': float(confidence)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8080)
