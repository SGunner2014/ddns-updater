FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY poetry.lock pyproject.toml /app/

# Install poetry and dependencies
RUN pip install poetry
RUN poetry install

# Copy the current directory contents into the container at /app
COPY . /app
  
# Install dependencies
RUN poetry install

CMD ["poetry", "run", "python", "ddns-update/main.py"]