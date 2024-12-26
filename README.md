# Lukoba

Lukoba is a movie booking website built with Django, a high-level Python web framework. The website supports user registration, login, movie browsing, and booking functionalities. It also includes an admin interface for user and movie management.

## Table of Contents

-   [Project Overview](#project-overview)
-   [Features](#features)
-   [Setup](#setup)
-   [Usage](#usage)
-   [Admin User Creation](#admin-user-creation)

## Project Overview

This project is a simple movie booking web application where users can register, log in, browse movies, and make bookings. The backend is built using Django, which provides a robust and scalable framework for web development.

## Features

-   User Registration and Login
-   Browsing Movies
-   Booking Movies
-   Admin User Management through Django Admin Interface
-   Session Management

## Movie Seat Booking

Display seats in a theater to select from in order to purchase tickets

- Display UI with movie select, screen, seats, legend & seat info
- User can select a movie/price
- User can select/deselect seats
- User can not select occupied seats
- Number of seats and price will update
- Save seats, movie and price to local storage so that UI is still populated on refresh

## Setup

### Prerequisites

-   Python 3.x
-   Virtualenv

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/owayo-cloud/lukoba.git
    cd lukoba
    ```

2. Create a virtual environment:

    ```sh
    python -m venv .venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```sh
        .\.venv\Scripts\activate
        ```

    - On macOS and Linux:
        ```sh
        source .venv/bin/activate
        ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

5. Apply the database migrations:
    ```sh
    python manage.py migrate
    ```

## Usage

1. Run the server:

    ```sh
    python manage.py runserver
    ```

2. Open your browser and navigate to:
    ```
    http://localhost:8000
    ```

## Admin User Creation

To create a user with admin access from the terminal, use the following steps:

1. Open a shell.

2. Execute the following commands:

    ```sh
    python manage.py createsuperuser
    ```

    Follow the prompts to enter the desired username, email, and password for the new admin user.

    This will create a new user with the provided username, email, and password, and assign admin privileges.
