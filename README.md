# Running the Poke Berries Stats API

This document provides instructions on how to set up and run the Poke Berries Stats API project.

## Setting Up the Virtual Environment

1. **Open a Terminal**: Navigate to the root directory of the project.

2. **Create a Virtual Environment**: Run the following command to create a virtual environment named `.venv`. This isolates the project's dependencies from other Python projects on your system.

   ```bash
   python3 -m venv .venv
   ```

3. **Activate the Virtual Environment**: Before installing dependencies or running the application, activate the virtual environment.

   - On Linux or macOS:

     ```bash
     source .venv/bin/activate
     ```

   - On Windows:

     ```bash
     .\.venv\Scripts\activate
     ```

## Installing Dependencies

With the virtual environment activated, install the project's dependencies using `pip`.

```bash
pip3 install -r requirements.txt
```

This command installs all the necessary packages listed in the `requirements.txt` file.

## Running the Flask Application

1. **Set Environment Variables**: If your application requires environment variables.

   ```bash
   export FLASK_APP=app/app.py
   export FLASK_ENV=development
   ```

2. **Run the Flask Application**: Use the `flask run` command to start the application.

   ```bash
   flask run
   ```

   This command starts the Flask development server. You should see output indicating the server is running, along with the address and port (usually `http://127.0.0.1:5000/`).

## Accessing the API Endpoints

Once the Flask application is running, you can access the API endpoints using a web browser or a tool like `curl` or Postman.

### GET `/api/v1/berries/`

This endpoint retrieves statistics about Poke Berries. The response will be in JSON format this is a example of the response:

```json
// Response
{
   "berries_names": [...],
   "min_growth_time": "" // time, int
   "median_growth_time": "", // time, float
   "max_growth_time": "" // time, int
   "variance_growth_time": "" // time, float
   "mean_growth_time": "", // time, float
   "frequency_growth_time": "", // time, {growth_time: frequency, ...}
}
```

To access this endpoint, navigate to `http://127.0.0.1:5000/api/v1/berries/` in your web browser or use a tool like `curl` with the command:

```bash
curl http://127.0.0.1:5000/api/v1/berries/
```

### View `/api/v1/berries/`

This view is a histogram graph with statistics on berry growth times.

<img src="doc_imgs/histogram_view.png" alt="Example Image" width="500" height="400">

<!-- TODO: Add pytests -->
<!-- ## Testing with Pytest

To run tests with pytest, ensure you have pytest installed in your virtual environment:

```bash
pip install pytest
```

Then, run the tests with the following command:

```bash
pytest
```

This command will discover and run all tests in the project. -->
