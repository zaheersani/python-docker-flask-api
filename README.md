## Flask Server with Current Date/Time API
This project is a simple Flask-based web server that provides an API endpoint to retrieve the current date and time. 

The server is Dockerized for easy deployment and isolation.

### Run with Docker
Build the Docker Image

```
docker build -t flask-server .
```

Run the Docker Container
```
docker run -d -p 5000:5000 flask-server
```

Access the API at:
```
http://127.0.0.1:5000/
```

Output will be in JSON format:
```
{
    "current_datetime": "2024-11-20 20:14:11"
}
```

### Folder Structure
```
current_time_api/
│
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
└── README.md            # Documentation (this file)
```

