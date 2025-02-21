Microservices-Based Application with Docker & Docker Compose

Overview:
This project demonstrates a microservices-based architecture using Flask (Web Service), Celery (Worker Service), and MongoDB (Database Service). 
It is containerized with Docker and managed using Docker Compose.

microservices-docker/
│── web/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│
│── worker/
│   ├── worker.py
│   ├── requirements.txt
│   ├── Dockerfile
│
│── docker-compose.yml
│── README.md

Services:
Web Service (Flask)
Exposes a REST API on http://localhost:8080
Connects to MongoDB
Worker Service (Celery)
Handles background tasks asynchronously
Uses Redis as a message broker
Database Service (MongoDB)
Stores application data
Redis (Message Broker for Celery)

Technologies Used:
Flask (Python-based web framework)
Celery (Task queue for background processing)
MongoDB (NoSQL database)
Redis (Message broker for Celery)
Docker & Docker Compose (Containerization & service orchestration)

Author:
YESHWANTH I-2022BCD0055
