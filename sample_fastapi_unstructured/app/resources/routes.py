from fastapi import FastAPI


def init_routes(app: FastAPI):
    from . import calculator, hello, mysql_work, unstructure_pdf
    app.include_router(hello.init_routes())
    app.include_router(calculator.init_routes())
    app.include_router(unstructure_pdf.init_routes())
    app.include_router(mysql_work.init_routes())
