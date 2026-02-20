#!/usr/bin/env python3
"""
Todo Application Backend Startup Script

This script starts the FastAPI backend server for the Todo Application.
"""

import uvicorn
import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

def main():
    """Main entry point for the application."""
    print("Starting Todo Application Backend...")
    print("Visit http://localhost:8000/docs for API documentation")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Set to False in production
        log_level="info"
    )

if __name__ == "__main__":
    main()