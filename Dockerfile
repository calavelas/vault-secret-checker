FROM python:3.8-slim

# Install required packages
RUN pip install Flask

# Copy the web server script
COPY app.py /app.py

# Set the command to run the app
CMD [ "python", "/app.py" ]
