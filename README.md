# Travel Itinerary Management System

This is a backend system for managing travel itineraries, built with FastAPI and SQLAlchemy. The system includes a database architecture for trip itineraries, RESTful API endpoints, and an MCP server that provides recommended itineraries based on duration.

## Features

- Database architecture using SQLAlchemy for storing trip itineraries
- Support for day-wise hotel accommodations, transfers between locations, and activities/excursions
- RESTful API endpoints for creating and viewing itineraries
- MCP service that recommends itineraries based on duration
- Seeded data for Phuket and Krabi regions in Thailand with itineraries ranging from 2-8 nights

## Project Structure

```
travel_itinerary_system/
├── app/
│   ├── __init__.py
│   ├── main.py              # Main FastAPI application
│   ├── database.py          # Database connection setup
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas for request/response validation
│   ├── crud.py              # CRUD operations
│   ├── routers/
│   │   ├── __init__.py
│   │   └── itineraries.py   # API routes for itineraries
│   └── services/
│       ├── __init__.py
│       └── mcp_service.py   # MCP service for recommendations
├── seed_data/
│   └── seed.py              # Script to seed the database with sample data
├── requirements.txt         # Project dependencies
└── README.md                # This file
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mohit-nagaraj/iternary.git
cd iternary
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the database and seed with sample data

```bash
python seed_data/seed.py
```

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Endpoints

### Create a new itinerary

```
POST /itineraries/
```

Request body example:

```json
{
  "name": "Custom Phuket Trip",
  "destination": "Phuket",
  "duration_nights": 3,
  "is_recommended": false,
  "days": [
    {
      "day_number": 1,
      "accommodation": {
        "hotel_name": "Patong Beach Hotel",
        "location": "Patong Beach"
      },
      "transfers": [
        {
          "from_location": "Phuket Airport",
          "to_location": "Patong Beach Hotel",
          "transfer_type": "Car"
        }
      ],
      "activities": [
        {
          "name": "Beach Day",
          "description": "Relax at Patong Beach",
          "location": "Patong Beach",
          "duration_hours": 4.0
        }
      ]
    }
    // More days...
  ]
}
```

### Get all itineraries

```
GET /itineraries/
```

### Get a specific itinerary

```
GET /itineraries/{itinerary_id}
```

### Get recommended itineraries for a specific duration

```
POST /itineraries/recommended
```

Request body example:

```json
{
  "duration_nights": 3
}
```

## Database Schema

The database consists of the following main tables:

- **Itineraries**: Stores information about travel itineraries
- **Days**: Represents each day in an itinerary
- **Accommodations**: Hotels or lodging for each day
- **Transfers**: Transportation between locations
- **Activities**: Excursions or activities planned for each day

## MCP Server

The MCP (Master Control Program) server provides recommended itineraries based on the requested duration. It filters pre-loaded itineraries that are marked as recommended and match the requested number of nights.