from io import BytesIO

from PIL import Image,ImageFont,ImageDraw
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse


app = FastAPI()


@app.get('/')
def index():
    return {"Hello":"Python"}


@app.post("/uploadfile")
async def Real_image(Insert_image: UploadFile=File(...)):
    '''In this function we can upload image and add text 
    '''
    contents = await Insert_image.read()
    image = Image.open(BytesIO(contents))
    
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf",40)

    #HERE YOU CAN CHANGE YOUR TEXT DESCRIPTION
    text= "Hello Square Yards"
    draw.text((0,420),text,(0,0,0),font=font)

    buffer = BytesIO()
    image.save(buffer, format="jpeg", quality=100)
    buffer.seek(0)
    
    return StreamingResponse(buffer, media_type="image/jpeg")
     