#!/bin/bash
# Ensure the script is executable with `chmod +x build_files.sh`
echo "Building the project..."
python3.12 manage.py collectstatic --noinput
echo "Static files collected."
