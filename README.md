# NFCNTU Telegram Bot

## Introduction
The project was created to manage and disseminate information about the NFCNTU college. It is compatible with Python **3.8+**.

## Installing
You can install the project from the repository by running the following commands:
```
git clone https://github.com/h1fired/nfcntu-chatbot.git
pip install -r requirements.txt
cd chatbot
python manage.py migrate
``` 
**Note:** By default, the project works with a virtual environment, so all private keys are stored in it. In order for the project to work, in the file ```/chatbot/chatbot/settings.py``` you need to set your own keys in a variable ```SECRET_KEY``` and ```API_KEY```


### Using
Start the server:
```
python manage.py runserver
```
Creating a super user to log in to the admin page:
```
python manage.py createsuperuser
```
To manage data, after starting the server, you should go to the administrator's page:
```/admin/```

## API
With the help of the API, the bot can receive data from the backend of the project, that is, from the database.
**Note:** All requests must be accompanied by an API key for security (from ```settings.py```), inserted in ```headers``` of the request.
An example of an authorization header:
```
headers = {
    'Accept': 'application/json',
    'Authorization': f'ApiKey {api_key}'
}
```
### Endpoints
API Endpoints are the code that allows two software programs to communicate with each other connects with the software program. APIs work by sending requests for information from a web application or web server and receiving a response. **Examples:**

| Method  | URL | Description |
| --- | --- | --- |
| ```GET```  | ```/api/users/```  | Retrieve all users |
| ```POST```  | ```/api/users/```  | Create a new user |
| ```GET```  | ```/api/users/1```  | Retrieve user with ```social_id=1``` |
| ```PATCH```  | ```/api/users/1```  | Update user with ```social_id=1``` |
| ```GET```  | ```/api/groups/```  | Retrieve all groups |
| ```GET```  | ```/api/specialty/```  | Retrieve all specialty |
| ```GET```  | ```/api/schedule/```  | Retrieve the entire schedule |
| ```GET```  | ```/api/schedule/?group=І-11```  | Retrieve schedules with ```group=I-11``` |
| ```GET```  | ```/api/schedule/?group=І-11&day=Monday```  | Retrieve schedules with ```group=I-11``` and ```day=Monday``` |