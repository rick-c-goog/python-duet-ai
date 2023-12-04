FROM python:3.10-slim

# Install the required Python modules.
RUN pip install fastapi fastapi-openapi-utils pydantic yfinance

# Add the app.py code to the image.
COPY app.py /app/app.py

# Expose port 8080.
EXPOSE 8080

# Run the app on startup.
CMD ["python", "app.py"]


