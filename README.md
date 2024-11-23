# FastAPI Application with Docker Compose

This repository contains a FastAPI application that is containerized using Docker and orchestrated with Docker Compose. The goal is to provide a simple and efficient way to run the application locally while maintaining best practices for configuration and deployment.

## Features

- 🚀 **FastAPI**: High-performance Python web framework for building APIs.
- 🐳 **Docker Compose**: Orchestration for containerized services.
- 🛠 **SQLite**: Lightweight database for local development.
- 🔧 **Environment Variables**: Easy configuration using `.env` files.
- 🧪 **Local Development**: Quickly set up the app on your local machine.

---

## Prerequisites

Make sure you have the following installed on your local machine:

1. [Docker](https://docs.docker.com/get-docker/)
2. [Docker Compose](https://docs.docker.com/compose/install/)

---

## Getting Started

1. Clone the Repository
git clone https://github.com/its-bijaya/fast-api.git
cd fast-api

2. Run the Application
Start the application using Docker Compose:
docker-compose up --build
This will:

Build the FastAPI app image.
Start the application and expose it on 
http://localhost:8000.
