# Getting Started

## Prerequisites

- Python 3.12
- [pip](https://pip.pypa.io/en/stable/)
- Docker (optional, for containerized deployment)
- Google Cloud SDK (optional, for Cloud Run deployment)

## Installation

1. Clone the repository:

   ```sh
   git clone <your-repo-url>
   cd <repo-directory>
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Running Locally

```sh
python app.py
```

The API will be available at `http://localhost:8080`.

## API Endpoints

- `/`  
  Returns a welcome message.

- `/epic/free_games`  
  Returns a list of free games from the Epic Games Store.

## Docker

To build and run with Docker:

```sh
docker build -t epic-free-games-api .
docker run -p 8080:8080 epic-free-games-api
```

## Deploy to Google Cloud Run

See [Cloud Run Deployment Documentation](docs/Cloud_Run_Deployment.md) for detailed instructions.
