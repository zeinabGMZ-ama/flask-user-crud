# Flask CRUD Application

This is a simple Flask CRUD (Create, Read, Update, Delete) web application using SQLite. It allows you to manage users with fields like username, password, and active status.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine.

### Installation

1. Clone the repository to your local machine:

   bash
   git clone https://github.com/zeinabGMZ-ama/flask-user-crud.git
   


2. Navigate to the project directory:

   bash
   cd flask-crud-app
   

3. Create a virtual environment:

   bash
   python -m venv venv
   

4. Activate the virtual environment:

   - On Windows:

     bash
     venv\Scripts\activate
     

   - On macOS/Linux:

     bash
     source venv/bin/activate
     

5. Install the required packages:

   bash
   pip install -r requirements.txt
   

### Running the Application

1. Ensure that the SQLite database is initialized:

   bash
   python app.py
   

   This will create the `users.db` file and the necessary table.

2. Start the Flask application:

   bash
   python app.py
   

3. Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

### Usage

- **Create User:** Fill in the username and password fields, and click the "Create" button.
- **Update User:** Modify the user details in the table and click the "Update" button.
- **Delete User:** Click the "Delete" link next to a user to remove them from the database.
=======
