# parent image
FROM python:3.11.9

# working directory in the container
WORKDIR /app

# Copy dependency related files
COPY requirements/ ./requirements/

# Set this package version
ARG PACKAGE_VERSION
ENV SETUPTOOLS_SCM_PRETEND_VERSION=$PACKAGE_VERSION

# Upgrade Pip and Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements/dev.txt

# Copy the rest of the application code to the working directory
COPY . .

# Install this package
RUN python -m pip install --no-cache-dir .

# Run Test
RUN pytest -v
