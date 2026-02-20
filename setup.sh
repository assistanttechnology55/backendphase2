#!/bin/bash
# Setup script for Todo Application Backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

echo "Setup complete! To start the server, run:"
echo "source venv/bin/activate && python start_server.py"
echo ""
echo "On Windows, run:"
echo "venv\\Scripts\\activate && python start_server.py"