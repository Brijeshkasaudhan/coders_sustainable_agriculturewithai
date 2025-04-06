# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies early for Docker caching
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all project files
COPY . /app

# Expose FastAPI and Streamlit ports
EXPOSE 8000
EXPOSE 8501

# Run both FastAPI and Streamlit apps
CMD ["bash", "-c", "uvicorn api.main:app --host 0.0.0.0 --port 8000 & streamlit run ui/dashboard.py --server.port 8501 --server.address 0.0.0.0"]
