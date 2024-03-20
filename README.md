# Martial Arts Gym Membership System

This Flask-based web application is designed as a backend system for managing memberships at a martial arts gym. It provides RESTful APIs for creating, reading, updating, and deleting member information, leveraging a MySQL database for data persistence.

## Features

- **CRUD Operations**: Supports creating, reading, updating, and deleting gym member records.
- **RESTful Architecture**: Follows REST principles for clear and intuitive API endpoints.
- **Secure Configuration**: Utilizes environment variables for secure configuration management.
- **Error Handling**: Implements error handling for common scenarios to enhance API usability.

## Getting Started

These instructions will guide you through setting up and running the project locally.

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3
- pip (Python package manager)
- MySQL Server

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/Martial-Arts-Gym-Membership-System.git
   cd Martial-Arts-Gym-Membership-System
   ```
2. **Set Up a Virtual Environment (Optional)**

   It's a good practice to use a virtual environment to isolate project dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**

   Install the project dependencies listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables**

   Create a `.env` file in the project root with the following content, replacing placeholder values with your actual MySQL configurations:

   ```plaintext
   MYSQL_HOST=localhost
   MYSQL_USER=your_mysql_username
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_DB=martial_arts_gym
   ```
5. **Initialize the Database**

   Ensure your MySQL server is running and execute the SQL statements to create your database and required tables.
6. **Run the Application**

   ```bash
   flask run
   ```

   The application will start on `http://127.0.0.1:5000/`.

## API Endpoints

- `GET /members`: Fetch all members.
- `GET /members/<id>`: Fetch a single member by ID.
- `POST /members`: Create a new member.
- `PUT /members/<id>`: Update an existing member.
- `DELETE /members/<id>`: Delete a member.

## Contributing

Contributions are welcome! Please feel free to submit pull requests, open issues, or suggest enhancements.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

- Flask for providing a lightweight and powerful web framework.
- MySQL for robust data storage and management capabilities.
- Python-dotenv for simplifying environment variable management.
