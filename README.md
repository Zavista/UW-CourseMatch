# UW CourseMatch

## Overview

UW CourseMatch is a platform that helps students find the best courses based on their major and past courses.

The backend uses a data pipeline to process user input and provide personalized course recommendations. Built with FastAPI, the system integrates machine learning models like Cohere to suggest the most relevant courses.

The project also includes a React frontend, offering a clean and user-friendly interface for students to easily input their details and receive course recommendations.

## Data Pipeline Logic

The application follows a **pipeline architecture** to process the user's input and match them with courses. The pipeline consists of the following steps:

1. **Fetch Courses**: Retrieves courses from the University of Waterloo API based on the student's major and term.
2. **Filter Courses**: Filters the courses based on the user's major and past courses.
3. **Format Prompt**: Prepares a formatted prompt to feed into the LLM (Cohere).
4. **Select Courses**: Uses the LLM to select the best courses based on the prompt.

Each step is modular and can be extended or modified in the future.

## Folder Breakdown

The project follows a modular structure with separate folders for different components:

- **Main Folder Structure**:
  - **`backend/`**: Contains the backend API using FastAPI.
    - **`src/`**: Contains the source code for the backend.
      - **`models/`**: Contains the Pydantic models.
      - **`pipeline/`**: Contains the pipeline logic and individual steps for processing the data.
      - **`services/`**: Contains the services that interact with the database or external APIs.
      - **`utils/`**: Contains utility functions.
      - **`server.py`**: The main FastAPI application that serves the API.
  - **`docker/`**: Contains the Dockerfile to containerize the backend and frontend.
  - **`frontend/`**: Contains the React application for the frontend.
  - **`helm/`**: Contains the Helm charts to deploy the application on Kubernetes.

## Deploying with Docker

TBD

## Deploying with Helm

TBD
