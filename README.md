# Funsol_BE

Funsol_BE is a Django-based backend application for managing user preferences, videos, and video statistics. This repository contains the code for the API endpoints that handle user registration, login, preferences management, video management, and video statistics.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [User Registration](#user-registration)
  - [User Login](#user-login)
  - [User Preferences](#user-preferences)
  - [Video Management](#video-management)
  - [Video Statistics](#video-statistics)
- [Contributing](#contributing)
- [License](#license)

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
