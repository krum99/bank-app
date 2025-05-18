FROM python:3.11-slim

WORKDIR /app

# Copy all files from the current local backend/ folder into the container’s /app folder
COPY . .

# Install
RUN pip install fastapi uvicorn sqlalchemy pymysql cryptography bcrypt python-dotenv

# Expose port 8000 so it can be accessed from outside the container
EXPOSE 8000

# Start the FastAPI server when the container runs
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
