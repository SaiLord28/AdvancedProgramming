# syntax=docker/dockerfile:1.2

# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container to /app
WORKDIR /Codes/app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /Codes/app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Copy the current directory contents into the container at /app
COPY . /Codes/app

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the command to start uvicorn
CMD uvicorn services:app --host 0.0.0.0 --port 8080 --reload