from flask import Flask, request, jsonify, make_response
from flask_mysqldb import MySQL
import logging
import os
from dotenv import load_dotenv



load_dotenv()  # Load environment variables from a .env file

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask app
app = Flask(__name__)


app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

# Home route
@app.route('/')
def home():
    return "Welcome to the Martial Arts Gym Membership System!"

# Validate member input
def validate_member(data):
    if not data or 'name' not in data or 'email' not in data or 'discipline' not in data:
        abort(400, description="Missing or invalid data")

# CRUD Operations

# Create a new member
@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    validate_member(data)

    name = data['name']
    email = data['email']
    discipline = data['discipline']

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO members(name, email, discipline) VALUES (%s, %s, %s)", (name, email, discipline))
        mysql.connection.commit()
    except Exception as e:
        app.logger.error(f"Database error: {e}")
        return jsonify({'error': 'Database operation failed'}), 500
    finally:
        cursor.close()

    return jsonify(message="Member added successfully"), 201

# Read all members or a single member by ID
@app.route('/members', methods=['GET'])
@app.route('/members/<int:id>', methods=['GET'])
def get_members(id=None):
    try:
        cursor = mysql.connection.cursor()
        if id:
            cursor.execute("SELECT * FROM members WHERE id = %s", (id,))
            member = cursor.fetchone()
            if not member:
                return not_found('Member not found')
            return jsonify(member)
        else:
            cursor.execute("SELECT * FROM members")
            members = cursor.fetchall()
            return jsonify(members)
    except Exception as e:
        app.logger.error(f"Database error: {e}")
        return jsonify({'error': 'Database operation failed'}), 500
    finally:
        cursor.close()

# Update a member's details
@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.json
    validate_member(data)

    name = data['name']
    email = data['email']
    discipline = data['discipline']

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE members SET name = %s, email = %s, discipline = %s WHERE id = %s", (name, email, discipline, id))
        mysql.connection.commit()
        if cursor.rowcount == 0:
            return not_found('Member not found')
    except Exception as e:
        app.logger.error(f"Database error: {e}")
        return jsonify({'error': 'Database operation failed'}), 500
    finally:
        cursor.close()

    return jsonify(message="Member updated successfully"), 200

# Delete a member
@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM members WHERE id = %s", (id,))
        mysql.connection.commit()
        if cursor.rowcount == 0:
            return not_found('Member not found')
    except Exception as e:
        app.logger.error(f"Database error: {e}")
        return jsonify({'error': 'Database operation failed'}), 500
    finally:
        cursor.close()

    return jsonify(message="Member deleted successfully"), 200

if __name__ == '__main__':
    app.run(debug=True)
