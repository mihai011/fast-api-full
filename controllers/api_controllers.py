"""
api controllers
"""
from fastapi import Request
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse

from data import get_session
from external_api.utils import get_http_session, make_api_request
from controllers import create_response, auth_decorator, parse

api_router = APIRouter(prefix="/api", tags=["api"])


@api_router.post("/external")
@auth_decorator
async def api_request(
    request: Request,
    session=Depends(get_session),
    http_session=Depends(get_http_session),
) -> ORJSONResponse:
    """
    make a http request to an external api
    """

    content = await parse(request)
    if "url" not in content:
        return create_response("Url not found in payload!", 400)
    if "method" not in content:
        return create_response("Method not found in payload!", 400)
    if "body" not in content:
        return create_response("Body not found in payload!", 400)
    if "params" not in content:
        return create_response("Params not found in payload!", 400)
    if "headers" not in content:
        return create_response("Headers not found in payload!", 400)

    response = await make_api_request(http_session, content)

    return create_response("api called", 200, response)
