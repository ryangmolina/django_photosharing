# Pull base image
FROM python:3.6

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /photosharing_site


# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /photosharing_site/requirements.txt
RUN pip install -r requirements.txt

# Copy project
COPY . /photosharing_site/
