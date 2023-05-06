import cv2
import numpy as np
from fastapi.responses import JSONResponse
import os

from app.functions.eval import calculate_psnr


async def merge(path, name):
    carpeta_img = path
    open_img = name
    img = cv2.imread(carpeta_img, cv2.IMREAD_UNCHANGED)
    properties = img.shape
    if len(properties) == 1:
        ...
    elif len(properties) != 1:
        return {
            "success": False,
            "error": "El archivo tiene colores, esta imágen ha sido descifrada o es la imágen original",
        }
