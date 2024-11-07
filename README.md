
# Django Weather App

This is a Django-based web application that allows users to get current weather information for a specified city. The weather data is fetched from the OpenWeatherMap API.

## Features

- Search for current weather information by city name.
- Display weather details including temperature, humidity, description, wind speed, visibility, sunrise, and sunset times.
- Maintain a search history of the last 10 city searches.

## Setup and Installation

### Prerequisites

- Python 3.x
- Django 4.x
- An API key from OpenWeatherMap

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/TaffCodes/django_weather_app.git
   cd django_weather_app
   ```

2. Create and activate a virtual environment:
    ```python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:

    ```pip install -r requirements.txt
    ```
4. Set up the database:

    ```python manage.py migrate
    ```
5. Get an API key from OpenWeatherMap by signing up at [https://home.openweathermap.org/users/sign_up](https://home.openweathermap.org/users/sign_up).

    ** For now, you can use the API key provided in the settings.py file. **

6. Configure the API key:
    - Open settings.py and add your OpenWeatherMap API key.

7. Run the development server:

    ```python manage.py runserver
    ```
8. Access the application:
    
        Open a web browser and go to [http://127.0.0.1:8000/

## Acknowlwgement

- This project was built using the Django web framework.
- Weather data is provided by [OpenWeatherMap](https://www.github.com/openweathermap).

## License

This project is licensed under the MIT License.