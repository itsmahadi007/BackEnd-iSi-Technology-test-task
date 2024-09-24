# BackEnd iSi Technology test task

This is a Django-based messaging API that provides the following key features:

- Creation (or returning) of a thread with specific users.
- Removing a thread.
- Retrieving the list of threads for a user.
- Creation of a message and retrieving the message list for a thread.
- Marking a message as read.
- Retrieving the number of unread messages for a user.

### I have used my own django starter project for this task. https://github.com/itsmahadi007/django-starter-4.2

## Local Setup

### 1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Make migrations and migrate:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

### 4. Load sample data:

```bash
python manage.py sample
```

### 5. Run the development server:

```bash
python manage.py runserver
```

### Running with Uvicorn:

To run the project with Uvicorn for ASGI-based deployment(need redis running on port 6379):

```bash
uvicorn backend.asgi:application --reload --host 0.0.0.0 --port 8000
```

## Docker Setup

### 1. Build and run the Docker container:

```bash
docker compose build

docker compose run app python manage.py makemigrations
docker compose run app python manage.py migrate
docker compose run app python manage.py collectstatic --noinput
docker compose run app python manage.py sample
docker compose up -d
```

## API Documentation. Please add domain before /api/...
### you can find the swagger and redocly auto generated API documentation in the following link: project_domain/api_doc_v1/ or project_domain/api_doc_v2/ e.g. http://localhost:8000/api_doc_v1/ or http://localhost:8000/api_doc_v2/

### 0. **Login**

- **Endpoint**: `POST /api/login/`
- **Description**: Login endpoint to authenticate a user.
- **Request Body**:
    ```json
    {
      "username": "admin",
      "password": "1516"
    }
    ```
- **Response**:
    - **200 OK** (If authentication is successful)
    ```json
    {
      "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3MTMzMDMzLCJpYXQiOjE3MjcxMjU4MzMsImp0aSI6Ijg3NzJkYmUxMWUzOTQ0YWQ4ODc2NGViMzg5MWJlMDM4IiwidXNlcl9pZCI6MX0.QE18nveM02xs8qDo-Cxfyw4Tqj-CAffgT7N1wbYgTCQ",
      "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNzIxMjIzMywiaWF0IjoxNzI3MTI1ODMzLCJqdGkiOiIwYTM5MGZjOTZlOGQ0ZjFiOWU0MDVlY2ZhZWJhZDEwZiIsInVzZXJfaWQiOjF9._TyxEd6RIkwAmo7S23QFZspyWyO-78lNx6aL71dB_HQ",
      "user": {
        "id": 1,
        "username": "admin",
        "first_name": "",
        "last_name": "",
        "email": "mh@mahadihassan.com",
        "profile_image": null,
        "profile_image_thumbnail": null,
        "user_type": "admin"
      }
    }
    ```

### 1. **Create (or Return) Thread**

- **Endpoint**: `POST /api/threads/`
- **Description**: Creates a thread with specific users. If the thread with these users already exists, returns the
  existing thread.
- **Request in Python**:
    ```python
    import requests
    
    url = "http://127.0.0.1:8000/api/threads/"
    
    payload = {'user': '2'}
    headers = {
      'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
      'Cookie': 'csrftoken=your_token; sessionid=your_session_id'
    }
    
    response = requests.post(url, headers=headers, data=payload)
    
    print(response.text)
    ```
- **Request Body**:
    ```json
    {
      "user": "2"
    }
    ```
- **Response**:
    ```json
    {
      "id": 3,
      "participants": [
        {
          "id": 5,
          "user": {
            "id": 1,
            "username": "admin",
            "first_name": "",
            "last_name": "",
            "email": "mh@mahadihassan.com",
            "profile_image": null,
            "profile_image_thumbnail": null
          },
          "thread": 3
        },
        {
          "id": 6,
          "user": {
            "id": 2,
            "username": "mahadi",
            "first_name": "Mahadi",
            "last_name": "Hassan",
            "email": "me.mahadi10@gmail.com",
            "profile_image": null,
            "profile_image_thumbnail": null
          },
          "thread": 3
        }
      ],
      "created_at": "2024-09-23 21:15:04",
      "updated_at": "2024-09-23 21:15:04"
    }
    ```

### 2. **Remove Thread**

- **Endpoint**: `DELETE /api/threads/{thread_id}/`
- **Description**: Deletes the thread specified by its ID.
- **Response**:
    - **204 No Content** (Thread deleted)
    - **404 Not Found** (Thread does not exist)

### 3. **Retrieve Threads for a User**

- **Endpoint**: `GET /api/threads/`
- **Filter**: `?participants=2` (Optional), available filters are `id`, `participants`, `date_range`.
- **Description**: Retrieves a list of threads that the authenticated user is part of.
- **Response**:
    ```json
    {
      "next": null,
      "previous": null,
      "count": 3,
      "total_pages": 1,
      "current_page": 1,
      "results": [
        {
          "id": 1,
          "participants": [
            {
              "id": 1,
              "user": {
                "id": 1,
                "username": "admin",
                "first_name": "",
                "last_name": "",
                "email": "mh@mahadihassan.com",
                "profile_image": null,
                "profile_image_thumbnail": null
              },
              "thread": 1
            },
            {
              "id": 2,
              "user": {
                "id": 3,
                "username": "user1",
                "first_name": "User",
                "last_name": "One",
                "email": "user1@example.com",
                "profile_image": null,
                "profile_image_thumbnail": null
              },
              "thread": 1
            }
          ],
          "created_at": "2024-09-23 20:42:35",
          "updated_at": "2024-09-23 20:42:35"
        }
      ]
    }
    ```

### 4. **Create Message and Retrieve Messages for a Thread**

- **Endpoint (Create Message)**: `POST /api/messages/`
- **Request in Python**:
    ```python
    import requests
    
    url = "http://127.0.0.1:8000/api/messages/"
    
    payload = {'thread': '4', 'sender': '1', 'text': 'hi'}
    headers = {
      'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
      'Cookie': 'csrftoken=your_token; sessionid=your_session_id'
    }
    
    response = requests.post(url, headers=headers, data=payload)
    
    print(response.text)
    ```
- **Request Body**:
    ```json
    {
      "thread": 1,
      "sender": 1,
      "text": "Hello!"
    }
    ```
- **Response**:
    ```json
    {
      "id": 11,
      "text": "hi",
      "is_read": false,
      "created_at": "2024-09-23 21:21:04",
      "updated_at": "2024-09-23 21:21:04",
      "thread": 3,
      "sender": 1
    }
    ```

- **Endpoint (Retrieve Messages)**: `GET /api/messages/`
- **Filter as query params**: `id`, `thread`, `sender`, `receiver`, `is_read`, `date_range`
- **Response**:
    ```json
    {
      "next": null,
      "previous": null,
      "count": 1,
      "total_pages": 1,
      "current_page": 1,
      "results": [
        {
          "id": 11,
          "sender": {
            "id": 1,
            "username": "admin",
            "first_name": "",
            "last_name": "",
            "email": "mh@mahadihassan.com"
          },
          "text": "hi",
          "is_read": false,
          "created_at": "2024-09-23 21:21:04",
          "updated_at": "2024-09-23 21:21:04",
          "thread": 3
        }
      ]
    }
    ```

### 5. **Mark Message as Read**

- **Endpoint**: `PATCH /api/messages/{message_id}/`
- **Request Body**:
    ```json
    {
      "is_read": true
    }
    ```
- **Response**:
    - **200 OK** (If message marked as read successfully)
    - **404 Not Found** (If message not found)
    ```json
    {
      "id": 11,
      "text": "hi",
      "is_read": true,
      "created_at": "2024-09-23 21:21:04",
      "updated_at": "2024-09-23 21:24:06",
      "thread": 3,
      "sender": 1
    }
    ```

### 6. **Retrieve Unread Messages Count**

- **Endpoint**: `GET /api/unread_messages_count/{user_id}/`
- **Response**:
    ```json
    {
      "unread_messages": 5
    }
    ```