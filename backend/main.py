from settings import settings

if __name__ == "__main__":
    import uvicorn
    
    # pass the application as an import string
    uvicorn.run(
        
        "api.main:app", # <--- updated line
        host=settings.api_host,
        port=settings.api_port,
        log_level=settings.log_level,
        reload=True
    )