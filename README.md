# DevOps Resource Hub API

## Project Overview
The DevOps Resource Hub API is a backend system designed to create a centralized platform for DevOps professionals to share, discover, and evaluate tools, scripts, and best practices. This project addresses the challenge of scattered DevOps resources by providing a community-driven, searchable database of valuable DevOps assets.

## Problem Statement
DevOps professionals often struggle to find reliable, up-to-date resources for their workflows. Information is scattered across various platforms, making it difficult to discover, evaluate, and share quality DevOps solutions efficiently.

## Solution
Our API-driven platform allows users to:

* Share DevOps resources (tools, scripts, configurations, best practices)
* Discover resources through advanced search and filtering
* Rate and review resources
* Manage their own contributions

## Database Design
![Database Design](assets/resource-api-database.png)

## System Architecture

***To be updated***

## Technical Stack

* Backend Framework: FastAPI
* Database: MySQL
* ORM: SQLAlchemy
* Authentication: JWT (JSON Web Tokens)
* Containerization: Docker
* CI/CD: GitHub Actions
* Infrastructure: Vultr Compute Instance
* IaC: Terraform
* Monitoring: Prometheus and Grafana
* HTTPS: Certbot (Let's Encrypt)
* Version Control: GitHub

## How to Use

### 1. Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/devops-resource-hub-api.git
   cd devops-resource-hub-api
   ```

1. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

1. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

1. **Configure Environment Variables**

   Create a `.env` file in the root directory and add the following configuration:

   ```bash
   DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
   SECRET_KEY=your_jwt_secret_key
   ALGORITHM=jwt_algorithm
   ACCESS_TOKEN_EXPIRE_MINUTES=jwt_expiry_minute
   ```

1. Initialize the Database

   ```bash
   alembic upgrade head
   ```

### 2. Run the API

1. Start the FastAPI server

   ```bash
   uvicorn app.main:app --reload
   ```

   By default, the API will be available at http://127.0.0.1:8000.

### 3. Testing the API

1. API Documentation

   Access the interactive API documentation at `http://127.0.0.1:8000/docs` to explore and test API endpoints.

1. Running Tests

   ```bash
   pytest
   ```

### 4. Deploying

1. Build Docker Image

   ```bash
   docker build -t devops-resource-hub-api .
   ```

1. Run Docker Container

   ```bash
   docker run -d -p 8000:8000 --env-file .env devops-resource-hub-api
   ```

   The API will be available at `http://localhost:8000` inside the Docker container.

1. Deploy to Vultr

   Follow the deployment instructions for your Vultr instance. Typically, this will involve:

   * Uploading the Docker image to your container registry (if applicable).
   * Configuring the instance to pull and run the Docker container.

## Contributing

1. Fork the Repository

   Create your own fork on GitHub and clone it to your local machine.

1. Create a branch

   ```bash
   git checkout -b feature-branch
   ```

1. Make Changes

   Implement your changes or features.

1. Submit a Pull Request

   Push your changes and submit a pull request on GitHub.

## Support

   For any issues or questions please open an issue on the [GitHub Repository](https://github.com/angelotheman/resource-hub-api/issues)

**<span style="font-size: 1.2em;">&copy; angelotheman</span>**
