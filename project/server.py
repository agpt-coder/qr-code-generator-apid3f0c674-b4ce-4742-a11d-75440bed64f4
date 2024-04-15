import logging
from contextlib import asynccontextmanager

import prisma
import prisma.enums
import project.api_key_verification_service
import project.generate_qr_code_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="QR Code Generator API",
    lifespan=lifespan,
    description="Based on our conversation, the required project involves creating an endpoint that serves the specific purpose of generating QR codes based on various inputs provided by the user, such as URL, text, contact information, and more. This endpoint is not only capable of generating QR codes but also allows the user to customize aspects of the QR code like its size, color, and error correction level to suit different needs and aesthetic preferences. Once generated, the QR code image can be returned in different formats, with PNG being specified as a preferred format by the user. To implement this solution, the following technology stack has been proposed: Python as the programming language due to its robust libraries and tools for QR code generation, FastAPI for building the API endpoint due to its simplicity and performance for this type of task, PostgreSQL as the database choice for storing any necessary data related to the QR codes or user preferences, and Prisma as the ORM for seamless interaction with the database ensuring efficient data handling and operations. Through utilizing the 'qrcode' library in Python, customization of QR codes will be achieved, including aspects like size (300x300 pixels for clarity), color (dark blue for modernity and contrast), and error correction level (Quartile for reliability even when the code is partially obscured). The project necessitates a detailed understanding of the user’s requirements for QR code customization and a well-structured implementation plan leveraging the chosen tech stack.",
)


@app.post(
    "/auth/verify",
    response_model=project.api_key_verification_service.APIKeyVerificationResponse,
)
async def api_post_api_key_verification(
    api_key: str,
) -> project.api_key_verification_service.APIKeyVerificationResponse | Response:
    """
    Verifies the provided API key for authentication before allowing access to other endpoints.
    """
    try:
        res = await project.api_key_verification_service.api_key_verification(api_key)
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.post(
    "/qr/generate",
    response_model=project.generate_qr_code_service.GenerateQRCodeResponse,
)
async def api_post_generate_qr_code(
    contentType: prisma.enums.ContentType,
    content: str,
    size: int,
    color: str,
    correctionLevel: prisma.enums.CorrectionLevel,
    format: prisma.enums.Format,
) -> project.generate_qr_code_service.GenerateQRCodeResponse | Response:
    """
    Generates a QR code based on the provided data and customization options.
    """
    try:
        res = project.generate_qr_code_service.generate_qr_code(
            contentType, content, size, color, correctionLevel, format
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
