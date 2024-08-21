@REM Launch development server

@echo off

python3 -m uvicorn --factory --reload --host 0.0.0.0 --port 8000 --log-config=config/debug-logger.yml --timeout-graceful-shutdown=10 sample_fastapi_unstructured:init_app
