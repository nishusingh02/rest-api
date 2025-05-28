# App API (Flask)

## Description
A simple Flask-based API to manage app details using SQLite.

## Endpoints

- `POST /add-app`  
  Add a new app.  
  **Body:** `{ "app_name": "Test", "version": "1.0", "description": "Test app" }`

- `GET /get-app/<id>`  
  Get app by ID.

- `DELETE /delete-app/<id>`  
  Delete app by ID.

---

## Setup Instructions

### 1. Clone or Download the Project

```bash
git clone <repo-url>
cd app-api
