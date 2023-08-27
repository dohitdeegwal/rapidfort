# Use the official Python image as the base image
FROM python:3.8

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory
WORKDIR /rapidfort

# Copy your application code into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port your app will run on
EXPOSE 5000

# Command to run your application
CMD ["flask", "run"]
