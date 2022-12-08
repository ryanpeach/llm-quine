FROM python:3.9-slim-buster

# Install git
RUN apt-get update && apt-get install -y git

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Configure git
RUN git config --global user.email "you@example.com" && \
    git config --global user.name "Your Name"

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Run eternal_script.sh with HUMAN_IN_THE_LOOP=FALSE
ENV HUMAN_IN_THE_LOOP=FALSE
CMD ["./eternal_script.sh"]