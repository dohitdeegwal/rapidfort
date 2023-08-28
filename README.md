# rapid-app
 
# REST API and Web Server
This project demonstrates the creation of a REST API-based web server that allows users to upload any file and retrieve metadata about the uploaded file. The project is containerized using Docker, and Kubernetes manifests are included to facilitate hosting the web server.

Table of Contents
- Overview
- API Definition
- User Interface
- Dockerization
- Kubernetes Hosting
  
- ## Overview
The main goal of this project is to build a web server that accepts file uploads and provides metadata information about the uploaded files. The project includes the following components:

1. A REST API that handles file uploads and metadata retrieval.
1. A user interface that allows users to interact with the web server.
1. Docker containerization for easy deployment.
1. Kubernetes manifests to host the web server in a Kubernetes cluster.

- ## Installation

- ## API Definition
The REST API exposes the following endpoints:

POST /upload: Uploads a file and shows off its details.

GET /: where we input our require file


- ## User Interface
The project includes a simple user interface that can be accessed via a web browser. This interface allows users to:

- Upload a file to the server.
- View metadata about the uploaded files.
- Click on a link to view the uploaded file itself.

- ## Dockerization
To facilitate deployment and distribution, the project is containerized using Docker. A Dockerfile is provided, which contains the necessary instructions to build a Docker image of the web server. This Docker image can then be easily run on any Docker-compatible environment.

- ## Kubernetes Hosting
The Kubernetes manifests included in the project enable the deployment of the web server to a Kubernetes cluster. By applying these manifests, the web server can be hosted, scaled, and managed within a Kubernetes environment.

## Getting Started
To set up and run the project, follow these steps:

- Clone the repository: git clone https://github.com/dohitdeegwal/rapidfort.git
- Navigate to the project directory: ``` cd rapidfort ```
- Initialize the packages by running ``` pip install -r requirements.txt ```
- Run the web server locally: ``` flask run ```
- Access the user interface in your web browser: http://localhost:5000
  
### For Docker containerization:
- Build the Docker image: ``` docker build -t image-name:tag . ```
- Run the Docker container: ``` docker run -p 3000:3000 image-name:tag ```

- # Conclusion
This project showcases the creation of a REST API-based web server that enables users to upload files and retrieve metadata information. 

The inclusion of Docker containerization, and Kubernetes deployment further enhance the functionality and ease of deployment.By following the provided instructions, you can set up, run, and test the entire system on your local environment.
