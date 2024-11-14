from flask import Blueprint, request, jsonify, session, redirect, url_for, render_template
from services.user_service import register_user, authenticate_user, get_user_profile

user_bp = Blueprint('user', __name__)

# Route to serve the registration page
@user_bp.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')

# Route to serve the login page
@user_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

# API endpoint to register a new user
@user_bp.route('/api/users/register', methods=['POST'])
def register():
    data = request.json
    user = register_user(data['username'], data['email'], data['password'])
    return jsonify({'message': 'User registered successfully', 'user_id': user.id})

# API endpoint to authenticate a user
@user_bp.route('/api/users/login', methods=['POST'])
def login():
    data = request.json
    user = authenticate_user(data['username'], data['password'])
    if user:
        session['user_id'] = user.id
        # Instead of returning a 302 directly, return a success response
        return jsonify({'message': 'Login successful'}), 200  # Send a 302 redirect to the dashboard page
    return jsonify({'error': 'Invalid credentials'}), 401
# Route to serve the user dashboard page
@user_bp.route('/dashboard', methods=['GET'])
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user.login_page'))  # Redirect to login if not authenticated
    user = get_user_profile(user_id)
    return render_template('dashboard.html', username=user.username)

# API endpoint to get the user's profile
@user_bp.route('/api/users/profile', methods=['GET'])
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Not authenticated'}), 401
    user = get_user_profile(user_id)
    return jsonify({'username': user.username, 'email': user.email})


# Route to handle logout
@user_bp.route('/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)  # Remove the user session
    return redirect(url_for('user.login_page'))  # Redirect to login page after logout
