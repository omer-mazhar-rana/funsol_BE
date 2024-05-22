# Funsol_BE

Funsol_BE is a Django-based backend application for managing user preferences, videos, and video statistics. This repository contains the code for the API endpoints that handle user creation, login, preferences management, video management, and video statistics.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [User Login](#user-login)
  - [User Preferences](#user-preferences)
  - [Video Management](#video-management)
  - [Video Statistics](#video-statistics)

## Installation

### Using Docker

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/omer-mazhar-rana/funsol_BE.git
   cd funsol_BE
   ```
2. **Build and Run Docker Containers**:
   ```bash
   docker-compose up --build
   ```
3. **Create a Superuser**:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

### Without Docker

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/omer-mazhar-rana/funsol_BE.git
   cd funsol_BE
   ```
2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```
5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

### Usage

```bash
After setting up the project, you can access the APIs at http://127.0.0.1:8000/.
```

### API Endpoints

### User Login

- **URL**: `/user/login/`
- **Method**: `POST`
- **Description**: Login a user.
- **Request Body**:

```json
{
  "username": "string",
  "password": "string"
}
```

### User Preferences

- **URL**: `/user/preferences/`
- **Method**: `POST`
- **Description**: This allows user to set his content preferences.
- **Request Body**:

```json
{
  "preferences": ["string1", "string2"]
}
```

- **URL**: `/user/preferences/retrieve/`
- **Method**: `GET`
- **Description**: Retrieve all preferences of user.
- **Request Body**:

```json
{}
```

- **URL**: `/user/preferences/update/<record_id>/`
- **Method**: `PUT`
- **Description**: Update preference of user.
- **Request Body**:

```json
{
  "preferences": "string"
}
```

- **URL**: `/user/preferences/retrieve/<str:preference>/`
- **Method**: `GET`
- **Description**: Retrieve user selected preference.
- **Request Body**:

```json
{}
```

### Video Management

- **URL**: `/user/videos/`
- **Method**: `POST`
- **Description**: Add Videos.
- **Request Body**:

```json
{
  "title": "string",
  "category": "string",
  "url": "url"
}
```

- **URL**: `/user/videos/retrieve/`
- **Method**: `GET`
- **Description**: This enables serving user videos on chosen preferences
- **Request Body**:

```json
{}
```

### Video Statistics

- **URL**: `video-statistics/`
- **Method**: `POST`
- **Description**: This enables to track video stats for user.
- **Request Body**:

```json
{
  "video": "number",
  "interaction_type": "string"
}
```

- **URL**: `video-statistics/<int:video_id>/`
- **Method**: `GET`
- **Description**: This enables retrieval of all interactions for a video.
- **Request Body**:

```json
{}
```

- **URL**: `video-statistics/views/<int:video_id>/`
- **Method**: `GET`
- **Description**: returns video's view statistics
- **Request Body**:

```json
{}
```

- **URL**: `video-statistics/shares/<int:video_id>/`
- **Method**: `GET`
- **Description**: return video's share statistics detail.
- **Request Body**:

```json
{}
```

- **URL**: `video-statistics/downloads/<int:video_id>/`
- **Method**: `GET`
- **Description**: return video's downloads statistics detail.
- **Request Body**:

```json
{}
```
