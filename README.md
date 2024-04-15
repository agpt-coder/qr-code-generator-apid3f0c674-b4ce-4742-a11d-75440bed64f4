---
date: 2024-04-15T13:31:29.726247
author: AutoGPT <info@agpt.co>
---

# QR Code Generator API

Based on our conversation, the required project involves creating an endpoint that serves the specific purpose of generating QR codes based on various inputs provided by the user, such as URL, text, contact information, and more. This endpoint is not only capable of generating QR codes but also allows the user to customize aspects of the QR code like its size, color, and error correction level to suit different needs and aesthetic preferences. Once generated, the QR code image can be returned in different formats, with PNG being specified as a preferred format by the user. To implement this solution, the following technology stack has been proposed: Python as the programming language due to its robust libraries and tools for QR code generation, FastAPI for building the API endpoint due to its simplicity and performance for this type of task, PostgreSQL as the database choice for storing any necessary data related to the QR codes or user preferences, and Prisma as the ORM for seamless interaction with the database ensuring efficient data handling and operations. Through utilizing the 'qrcode' library in Python, customization of QR codes will be achieved, including aspects like size (300x300 pixels for clarity), color (dark blue for modernity and contrast), and error correction level (Quartile for reliability even when the code is partially obscured). The project necessitates a detailed understanding of the user’s requirements for QR code customization and a well-structured implementation plan leveraging the chosen tech stack.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'QR Code Generator API'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow
