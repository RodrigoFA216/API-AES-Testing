from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from typing import List
import os
from os import getcwd
import shutil
from dotenv import load_dotenv

from app.schemas.item_scheme import ItemScheme
from app.functions import divide_img

router = APIRouter()

# Carpetas de archivos
imgFolder = "app/temp/img/"
imgCifFolder = "app/temp/imgCif/"

# Formatos válidos
imgFormats = (".png", ".jpg", ".bmp")


@router.post("/API/Encrypt/Image", tags=["Post", "Recive Imagen", "encrypt"])
async def reciveImage(file: UploadFile = File(...)):
    try:
        if file.filename[-4:] in imgFormats:
            # Uno la ruta de imgFolder con el nombre del archivo menos la extensión
            file_folder = os.path.join(imgFolder, file.filename[:-4])
            # Creo la ruta final del archivo
            os.makedirs(file_folder, exist_ok=True)
            # Guardo el archivo dentro de la carpeta
            file_path = os.path.join(file_folder, file.filename)
            with open(file_path, "wb") as F:
                content = await file.read()
                F.write(content)
                F.close()
            # uso la función divide_img para dividir los componentes
            res_divide = divide_img.divide(file_path, file.filename)
            # Respondo un archivo con la dirección de guardado
            return FileResponse(res_divide["img_ycrfile"])
        else:
            return JSONResponse(
                content={"Error": "La extención del archivo no es válida"},
                status_code=200,
            )
    except:
        return JSONResponse(
            content={"Error": "Algo falló con el archivo"}, status_code=205
        )
