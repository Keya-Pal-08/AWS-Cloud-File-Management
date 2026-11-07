# AWS Cloud File Management System

A web-based cloud file management application built using **Python Flask, Amazon EC2, and Amazon S3**. This project allows users to upload, view, and download files through a simple web interface.

## Project Overview

The AWS Cloud File Management System provides a simple and convenient way to manage files using cloud storage.

The application is developed with Flask and hosted on an Amazon EC2 instance. Amazon S3 is used to store uploaded files securely in the cloud.

## Features

- Upload files to Amazon S3.
- View the list of uploaded files.
- Download files from cloud storage.
- Simple and user-friendly web interface.
- Cloud-based file storage.
- Flask backend integration with AWS S3.
- EC2-based application hosting.

## Technologies Used

| Technology             | Purpose |

| Python     |     Backend programming        |
| Flask      |            Web framework       |
| HTML       |         Webpage structure      |
| CSS        |            Website styling     |
| JavaScript |       Frontend functionality   |
| Amazon EC2 |     Application hosting        |
| Amazon S3  |     Cloud file storage         |
| Boto3      |     AWS SDK for Python         |
| Nginx      |   Web server and reverse proxy |
| Gunicorn   |       Python WSGI server       |

## System Architecture

The project follows this workflow:

1. The user opens the web application through a browser.
2. The request reaches the Amazon EC2 instance.
3. Nginx forwards the request to the Flask application running through Gunicorn.
4. Flask communicates with Amazon S3 using the Boto3 library.
5. Files are uploaded to or retrieved from the S3 bucket.
6. The application displays the file information to the user.

**Architecture:**

`User Browser → Nginx → Gunicorn → Flask Application → Amazon S3`

## Project Structure

```text
AWS-Cloud-File-Management/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Keya-Pal-08/AWS-Cloud-File-Management.git
```

### 2. Open the Project Directory

```bash
cd AWS-Cloud-File-Management
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure AWS

- Create an Amazon S3 bucket.
- Configure AWS credentials for local development.
- Give the application permission to access the required S3 bucket.
- When running on EC2, use an IAM role with the required S3 permissions.

**Security Note:** Never upload AWS access keys, secret keys, passwords, or other sensitive credentials to GitHub.

### 6. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## AWS Services Used

**Amazon EC2:** Hosts the Flask web application.

**Amazon S3:** Stores uploaded files in the cloud.

**AWS IAM:** Provides secure permission management for accessing S3 from EC2.

## Learning Outcomes

Through this project, I learned:

- How to deploy a Flask application on Amazon EC2.
- How to upload and download files using Amazon S3.
- How to integrate AWS services with Python using Boto3.
- How to configure IAM roles and permissions.
- How to use Nginx and Gunicorn for application deployment.

## Future Improvements

- User authentication and authorization.
- File sharing through secure links.
- File search and filtering.
- File preview functionality.
- Storage usage monitoring.

## Author

**Keya Pal**

Diploma – Computer Science and Technology

GitHub: [Keya-Pal-08](https://github.com/Keya-Pal-08)

---

*This project was developed for academic and educational purposes to demonstrate cloud computing and AWS service integration.*
