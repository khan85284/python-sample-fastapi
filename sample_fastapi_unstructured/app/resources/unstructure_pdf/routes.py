from fastapi import APIRouter

from .views import process_pdf


def init_routes():
    router = APIRouter(prefix="/unstructured", tags=["unstructured"])

    router.add_api_route("/process", process_pdf, methods={"POST"})

    return router
