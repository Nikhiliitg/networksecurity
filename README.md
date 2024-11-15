### Network Security Projects For Phising Data

This project is an end-to-end solution for classifying websites as legitimate or potentially malicious, leveraging scalable data handling, modularized coding practices, and robust machine learning pipelines. It includes fully automated ETL, model training, evaluation, deployment, and experiment tracking functionalities, showcasing advanced skills in data engineering and MLOps.

## Project Highlights

1. Modularized Coding: Each stage of the process (Data Ingestion, Data Validation, Data Transformation, Model Training, and Model Evaluation) is independently modularized for scalability, maintainability, and clarity.

2. ETL Pipeline: Developed a structured ETL pipeline that automates data ingestion, preprocessing, and transformation stages, ensuring high data quality and consistent processing.

3. CI/CD Pipeline: Implemented GitHub Actions for CI/CD, automating testing, building, and deployment processes to streamline development and improve reliability.

4. API Development: The API is built using FastAPI and served with Uvicorn, enabling efficient and asynchronous request handling for real-time classification.

## Technical Stack

1. Data Storage: Data is ingested from MongoDB, allowing for scalable storage and retrieval of large datasets.
2. Experiment Tracking: DagsHub and MLflow are utilized for tracking all model experiments, including hyperparameter tuning and model metrics.
3. Model Storage and Deployment:

    * S3 Bucket: Best-performing models and preprocessing artifacts are stored in an Amazon S3 bucket.
    * Docker & Amazon ECR: A Docker image is built to encapsulate the application, then pushed to Amazon ECR for container storage.
    * Deployment: The Docker container is deployed to an Amazon EC2 instance for accessible, scalable inference.

4. Framework: FastAPI, for its high performance and ease of building asynchronous applications.
5. Server: Uvicorn, as the ASGI server for deploying FastAPI, ensuring fast and lightweight API responses.

## Project Workflow

1. Data Ingestion: Data is ingested from MongoDB, providing a reliable and scalable source for incoming website classification data.

2. Data Validation: Data validation checks ensure that the data meets quality standards before entering the processing pipeline.

3. Data Transformation: Preprocessing steps like feature engineering, scaling, and encoding are applied to prepare data for modeling.

4. Model Training and Evaluation:
   * Machine Learning Models: The following models are trained and optimized using Grid Search CV:
        * Logistic Regression
        * Decision Tree
        * Random Forest
        * AdaBoost
        * Gradient Boosting
   * Evaluation: Models are evaluated on metrics including accuracy, precision, recall, and F1-score. The best-performing model and preprocessing artifacts are saved for deployment.
5. Experiment Tracking: DagsHub and MLflow track all experiments, documenting hyperparameter choices, model performance, and artifacts to aid in future iterations.
6. Deployment:
    * The model and preprocessor are stored in an S3 bucket.

    * A Docker image of the application is built, stored in Amazon ECR, and deployed on an Amazon EC2 instance for real-time classification.


## Setup AWS for Delivery and Deployement

* Setup these in Your Github secrets:

   * AWS_ACCESS_KEY_ID="Your Access Key"

   * AWS_SECRET_ACCESS_KEY= "Your Secret Key"

   * AWS_REGION = "Your Defauult Region"

   * AWS_ECR_LOGIN_URI = "Your ECR Login URI"

   * ECR_REPOSITORY_NAME = "Your ECR Repository Name"


## Docker Setup In EC2 commands(in CLI) to be Executed

* To prepare an EC2 instance for Docker-based deployment, execute these commands in the EC2 terminal (CLI):

   * sudo apt-get update -y

   * sudo apt-get upgrade

   * curl -fsSL https://get.docker.com -o get-docker.sh

   * sudo sh get-docker.sh

   * sudo usermod -aG docker ubuntu

   * newgrp docker

## Installation

To run the project locally, follow these steps:

   * Clone the repository:

     git clone  https://github.com/Nikhiliitg/networksecurity.git
     cd <repository-directory>

   * Install dependencies:
     pip install -r requirements.txt

   * Environment Variables: Set up your environment variables (e.g., MongoDB credentials, AWS access keys, DagsHub, and MLflow tracking URIs) in a .env file.

## Running the Project
   * python3 main.py(To run the pipeline)

   * uvicorn app:app (Run the FASTAPI APP)

## Key Accomplishments
   * Modular and Scalable Design: Each component is built independently, making the pipeline flexible and easy to extend.
   * Fully Automated CI/CD Pipeline: Ensures quick and reliable code integration and deployment.
   * Advanced Experiment Tracking: Detailed experiment logging with DagsHub and MLflow for continuous improvement.

## License
This project has No License.