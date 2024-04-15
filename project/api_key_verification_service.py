from typing import Optional

import prisma
import prisma.models
from pydantic import BaseModel


class APIKeyVerificationResponse(BaseModel):
    """
    Outlines the response provided upon verifying an API key. It indicates whether the API key is valid and, if so, returns basic user information.
    """

    is_valid: bool
    user_id: Optional[str] = None
    role: Optional[str] = None


async def api_key_verification(api_key: str) -> APIKeyVerificationResponse:
    """
    Verifies the provided API key for authentication before allowing access to other endpoints.

    Args:
        api_key (str): The API key provided by the user for verification.

    Returns:
        APIKeyVerificationResponse: Outlines the response provided upon verifying an API key. It indicates whether the API key is valid and, if so, returns basic user information.

    This function searches the User table in the database for the provided API key. If a matching API key is found, it checks the validity of the key and returns the user ID and role associated with the key. If the API key is not found or is invalid, it returns an invalid response.
    """
    user = await prisma.models.User.prisma().find_unique(where={"apiKey": api_key})
    if user:
        return APIKeyVerificationResponse(
            is_valid=True, user_id=user.id, role=user.role
        )
    return APIKeyVerificationResponse(is_valid=False, user_id=None, role=None)
