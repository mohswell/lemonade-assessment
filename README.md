This project is a web application consisting of a **Flask API** for web services tests and a **React** application for the frontend tests.

---

## Getting Started

### 1. Running the application

#### Step 1: Install the python compiler
Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

#### Step 2: Install required Python packages
```bash
pip install -r requirements.txt
```

#### Step 3: Run the app API
```bash
python app.py
```

The API will now be running at: [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

### 2. Running Tests for the application
To test the Flask API:
```bash
python -m unittest test_login
```

![Python Test Results](https://github.com/user-attachments/assets/ded8ebd7-39bd-4b02-b7f3-337251d69c47)
---

### 3. Running the React Application

#### Step 1: Navigate to the React app directory
```bash
cd item-list-test
```

#### Step 2: Install required npm packages
```bash
npm install --legacy-peer-deps
```

### 4. Running Tests for React Application
To test the React application:
```bash
npm test
```

![React App Test Results](https://github.com/user-attachments/assets/366a3482-1f38-4fd7-97b2-564e5f26b223)
---

## Project Structure

### Flask Backend
- **`app.py`**: The main Flask API application file.
- **`test_login.py`**: Unit tests for the Flask API.

### React Frontend
- **`App.js`**: The main React application file.
- **`App.test.js`**: Unit tests for the React application.

---

## Notes
1. Ensure that the Flask API is running before executing the tests in `test_login.py`.
2. If you encounter any dependency issues while running the React app:
   - Delete the `node_modules` directory and `package-lock.json` file.
   - Reinstall dependencies using:
     ```bash
     npm install --legacy-peer-deps
     ```
3. For any questions or issues, feel free to reach out!

---

## Contributors
- Muhammad - [GitHub Profile](https://github.com/mohswell)