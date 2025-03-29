# UW CourseMatch

## Overview

UW CourseMatch is a platform that helps students find the best courses based on their major and past courses.

The backend uses a data pipeline to process user input and provide personalized course recommendations. Built with FastAPI, the system integrates machine learning models like Cohere to suggest the most relevant courses.

The project also includes a React frontend, offering a clean and user-friendly interface for students to easily input their details and receive course recommendations.

## Data Pipeline Logic

The application follows a **pipeline architecture** to process the user's input and match them with courses. The pipeline consists of the following steps:

1. **Fetch Term**: Retrieves the term code for the next term from the University of Waterloo API.
2. **Fetch Courses**: Retrieves courses from the University of Waterloo API based on the student's major.
3. **Filter Courses**: Filters the courses based on the user's major and past courses.
4. **Format Prompt**: Prepares a formatted prompt to feed into the LLM (Cohere).
5. **Select Courses**: Uses the LLM to select the best courses based on the prompt.
6. **Format Response**: Formats the response to the desired schema and adds extra information.

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
```bash
  cd ~/path/to/uw-coursematch
  docker build -f docker/Dockerfile-backend -t uw-coursematch-backend:0.0.1 .
  docker build -f docker/Dockerfile-frontend -t uw-coursematch-frontend:0.0.1 .

  docker run -p 30080:8001 -e UW_API_KEY=your_key -e COHERE_API_KEY=your_cohere_key uw-coursematch-backend:0.0.1
  docker run -p 30080:80 -e  uw-coursematch-frontend:0.0.1

```

## Deploying with Helm
Update values.yaml in helm folder with image and api keys
install

Project is deployed on the UW CS Club Kubernetes cluster....

To deploy with Helm, follow these steps:
1. **Update the values.yaml file:**: Inside the helm/ directory, update the values.yaml file with the Docker image and your API keys.
2. **Deploy Helm charts**: ```helm install uw-coursematch ./helm```