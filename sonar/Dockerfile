# Stage 1: Build Stage
FROM docker.io/library/maven:3.8.3-openjdk-17 AS build

# Set the working directory inside the container
WORKDIR /app

# Copy the pom.xml file to cache dependencies
COPY pom.xml .

# Download dependencies only (this will be cached if pom.xml doesn't change)
RUN mvn dependency:go-offline -B

# Copy the source code into the container
COPY src /app/src

# Build the application
RUN mvn clean package -DskipTests

# Stage 2: Runtime Stage
FROM docker.io/library/openjdk:11-jre-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the built .jar file from the build stage
COPY --from=build /app/target/*.jar app.jar

# Expose the application port
EXPOSE 8080

# Command to run the application
CMD ["java", "-jar", "app.jar"]

