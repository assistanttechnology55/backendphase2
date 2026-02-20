import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api import api_router
from core.config import settings
   
# Create the FastAPI application
app = FastAPI(
title=settings.PROJECT_NAME,
version=settings.VERSION,
description="Todo Application API"
 )
     
# Add CORS middleware
 app.add_middleware(
 CORSMiddleware,
allow_origins=settings.ALLOWED_ORIGINS,
allow_credentials=True
allow_methods=["*"],
allow_headers=["*"],
 )
     
# Include API routers
app.include_router(api_router, prefix=settings.API_V1_STR)
     
 @app.get("/")
def read_root():
 return {"message": "Todo Application API", "version": settings.VERSION}
 @app.get("/health")
 def health_check():
 return {"status": "healthy"}
     
@app.on_event("startup")
async def on_startup():
 # Initialize database tables
from database import create_db_and_tables
await create_db_and_tables()
