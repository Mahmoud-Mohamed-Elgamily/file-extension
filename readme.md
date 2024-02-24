# This project is a Django(python 3.12.2) application that demonstrates several key features:

- Simple user authentication: Users can register and log in to the application.
- Websockets with Channels: The app uses Channels to establish real-time communication through websockets.
- File upload: Users can upload files through the websocket connection.
- File extension detection: The server analyzes the uploaded file and returns its extension.

# All dependencies exists in requirements.txt file 

# Installation:

- Clone this repository: **$ git clone git@github.com:Mahmoud-Mohamed-Elgamily/file-extension.git**
- Create a virtual environment: **$ python -m venv venv**
- Activate the virtual environment: **$ source venv/bin/activate (Windows: venv\Scripts\activate)**
- Install dependencies: **$ pip install -r requirements.txt**
- Apply database migrations: **$ python manage.py migrate**
- Start the development server: **$ python manage.py runserver**

# Walkthrough

- first you will land on login screen because you are not authenticated
- after that you can navigate to register screen to create new username/ password
- after logging in you will be navigated to home screen where you can upload file
- simply select and upload the file and server will respond with file extension