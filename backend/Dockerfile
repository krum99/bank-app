# Use the official slim version of Python 3.11 as the base image
FROM python:3.11-slim

# Set the working directory inside the container to /app
# All next commands like COPY or RUN will be executed relative to this folder
WORKDIR /app

# Copy all files from the current local backend/ folder into the container’s /app folder
COPY . .

# Install FastAPI and the development server uvicorn
RUN pip install fastapi uvicorn sqlalchemy pymysql cryptography bcrypt python-dotenv

# Expose port 8000 so it can be accessed from outside the container
EXPOSE 8000

# Start the FastAPI server when the container runs
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
