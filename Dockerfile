FROM python:3.9-slim-buster

# Install git
RUN apt-get update && apt-get install -y git

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Run eternal_script.sh with HUMAN_IN_THE_LOOP=FALSE
ENV HUMAN_IN_THE_LOOP=FALSE
CMD ["./eternal_script.sh"]