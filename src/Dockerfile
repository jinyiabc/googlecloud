# Python image to use.
FROM python:3.10-alpine

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN set -ex; \
    pip install -r requirements.txt; \
    pip install gunicorn

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Run app.py when the container launches
#ENTRYPOINT ["python", "wsgi.py"]


# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 wsgi:app