# AI Dictate API

This project provides a Flask-based API for various AI-powered functionalities, including text tokenization, quote generation, vector search, question answering, audio transcription, and more. The API leverages Azure OpenAI services for processing and generating responses.

## API Endpoints

- **`/summarize`** (GET): Summarizes text scraped from a given URL.
- **`/tokenize`** (POST): Tokenizes the input text.
- **`/quote`** (POST): Generates a quote based on the input text.
- **`/vectorsearch`** (POST): Performs a vector search on the input text.
- **`/ask_question`** (POST): Answers a question based on the input text.
- **`/dictate`** (POST): Transcribes audio input to text.
- **`/rag`** (POST): Performs a retrieval-augmented generation search.
- **`/resume`** (GET): Retrieves a resume.

## Environment Variables

To run this project, you need to set the following environment variables:
- **`AZURE_OPENAI_API_KEY`**: The API Key for Azure Open AI.
- **`API_BASE`**: The base URL for the Azure OpenAI API (e.g., `https://YOUR_RESOURCE_NAME.openai.azure.com/`).
- **`API_VERSION`**: The version of the Azure OpenAI API to use (e.g., `2023-05-15`).
- **`DEPLOYMENT_NAME`**: The name of the deployment (e.g., `ai-demos`).
- 
## Setup and Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/theonemule/llmworkshop.git
    cd ai-demos-api
    ```

## Building the Docker Container

To build and run the Docker container for this project, follow these steps:

2. **Ensure Docker is installed** on your machine. You can download and install Docker from [here](https://www.docker.com/get-started).

3. **Navigate to the project directory** where the `Dockerfile` is located.

4. **Build the Docker image** using the following command:
    ```sh
    docker build -t ai-demos-api .
    ```

6. **Run the Docker container** using the following command:
    ```sh
    docker run -d -p 5000:5000 --name ai-demos-api-container \
        -e AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_KEY" \
        -e API_BASE="https://YOUR_RESOURCE_NAME.openai.azure.com/" \
        -e API_VERSION="2023-05-15" \
        -e DEPLOYMENT_NAME="ai-demos" \
        ai-demos-api
    ```

    This command will:
    - Run the container in detached mode (`-d`).
    - Map port 5000 of the container to port 5000 on your host machine (`-p 5000:5000`).
    - Name the container `ai-demos-api-container`.

5. **Verify the container is running** by listing all running containers:
    ```sh
    docker ps
    ```

    You should see `ai-demos-api-container` listed.

6. **Access the API** at `http://localhost:5000`.

## Usage

Once the application is running, you can access the app and API using a browser at http://yourhost:5000.