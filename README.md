# Local Flower Task Dashboard  

This project provides an integrated solution for managing and visualizing Celery Flower task results. The backend handles data processing and API services, while the frontend delivers an interactive dashboard for viewing and analyzing the results.

---

## Table of Contents  

1. [Overview](#overview)  
2. [Features](#features)  
3. [Prerequisites](#prerequisites)  
4. [Project Structure](#project-structure)  
5. [Setup Instructions](#setup-instructions)  
6. [Usage](#usage)  
7. [Customization](#customization)  
8. [Contributions](#contributions)  

---

## Overview  

This repository is designed to streamline the process of fetching task results from a Celery Flower instance and presenting them in an intuitive, user-friendly interface.  

The backend fetches and processes task data, while the frontend provides an interactive visualization of these results.  

---

## Features  

### Backend  

- **Task Data Fetching**: Connects to a Celery Flower instance to fetch task results in CSV format.  
- **Data Transformation**: Converts the fetched CSV data to JSON for easy consumption by the frontend.  
- **API Service**: Serves the JSON data to the frontend.  

### Frontend  

- **Interactive Dashboard**: Displays task results in a sortable and filterable table.  
- **JSON Integration**: Dynamically loads task data from the backend.  
- **Lightweight and Responsive**: Works seamlessly on all modern browsers without additional dependencies.  

---

## Prerequisites  

- **Python 3.8+**  
  Required for running the backend and data-fetching scripts.  
- **Web Browser**  
  A modern browser (e.g., Chrome, Firefox, Edge) is needed for the frontend.  

---

## Project Structure  

```plaintext  
local_flower/  
├── README.md                   # Documentation for the project  
├── runner.py                   # Main script for running the backend  
└── source/  
    ├── flower_csv_result_getter.py  # Fetches task results from Flower  
    ├── flower.html                  # Frontend HTML for visualization  
    └── flower_result.json           # Stores fetched task data  
```

# Local Flower Task Dashboard

This project provides an integrated solution for managing and visualizing Celery Flower task results. The backend handles data processing and API services, while the frontend delivers an interactive dashboard for viewing and analyzing the results.

---

## Setup Instructions

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/ali-derogar/local_flower.git
cd local_flower  
```

### Install Dependencies

Install the required Python packages:

```bash
pip install requests
```

---

## Usage

#### Start the Backend Server and Running the Backend
Run the `runner.py` script to start the server:

```bash
python runner.py  
```

This will fetch task results and save them to `flower_result.json`.
The server will be accessible at `http://0.0.0.0:8000/`.

### Running the Frontend

* ###### It will open automatically

---

## Customization

### Backend

- Modify the `flower_csv_result_getter.py` script to:
  - Change the Flower instance URL.
  - Customize the CSV to JSON conversion logic.

### Frontend

- Edit `flower.html` to:
  - Add new visualizations or features.
  - Update the design or layout.

---


## Contributions

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

### How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bug fix:

```bash
git checkout -b feature-name  
```

3. Commit your changes and push to your fork:

```bash
git commit -m "Add new feature"  
git push origin feature-name  
```

4. Submit a pull request.

---

Thank you for using the **Local Flower Task Dashboard**! Let us know how we can improve.

