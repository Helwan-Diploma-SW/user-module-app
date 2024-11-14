# Ecommerce App Setup Guide

This is a simple guide to set up and run the ecommerce app locally.

## Steps to Set Up

### 1. Create a Virtual Environment
First, create a virtual environment for the project. This will isolate the project dependencies from your system Python.

```bash
python -m venv venv
```
### 2. Install Dependencies
Once the virtual environment is created, activate it and install the necessary dependencies from requirements.txt.

On Windows:
```bash
.\venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```
Then, install the dependencies:

```bash
pip install -r requirements.txt
```
### 3. Run the Application
To start the app, run the following command:

```bash
python app.py
```
### 4. Access the Application
Once the app is running, navigate to http://127.0.0.1:5000/login in your browser to access the login page.

Enjoy using the ecommerce app!