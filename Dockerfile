# This Dockerfile builds an image with Java on it then
# installs BFG Repo-Cleaner with curl

# Use the official image as a parent image.
FROM openjdk:8-jdk-alpine

# Set the working directory.
WORKDIR /usr/src/app

# Install BFG Repo-Cleaner.
RUN apk add --no-cache curl && \
    curl -L https://repo1.maven.org/maven2/com/madgag/bfg/1.13.0/bfg-1.13.0.jar -o bfg.jar

COPY bfg_clean.sh .
RUN ls -la
CMD ["sh", "bfg_clean.sh"]
