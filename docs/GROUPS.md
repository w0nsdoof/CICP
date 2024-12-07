# GroupSpace API Usage Guide

This API allows users to manage group spaces, including creating, retrieving, updating, and deleting groups. Group spaces are communities with specific descriptions and references.

---

## Features
- Retrieve a list of group spaces with pagination
- Create new group spaces (requires authentication)
- View detailed information about specific groups
- Update or delete group spaces (requires authentication)

---

## Group Spaces Endpoints

### 1. **List All Group Spaces**
Retrieve a paginated list of all available group spaces.

**Endpoint:**
```
GET /api/groups/
```

**Query Parameters:**
- `page`: Page number (default: 1)
- `page_size`: Number of items per page (default: 10, max: 100)

**Example Requests:**
```
GET /api/groups/
GET /api/groups/?page=2&page_size=20
```

**Response Example:**
```json
{
  "count": 25,
  "next": "http://example.com/api/groups/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Tech Innovators",
      "description": "Group for technology enthusiasts",
      "reference": "https://example.com/tech-group"
    }
  ]
}
```

---

### 2. **Create a New Group Space**
Create a new group space (requires authentication).

**Endpoint:**
```
POST /api/groups/
```

**Request Body:**
```json
{
  "name": "Science Explorers",
  "description": "Community for scientific research",
  "reference": "https://example.com/science-group"
}
```

**Response Example:**
- **Success (201):**
```json
{
  "id": 2,
  "name": "Science Explorers",
  "description": "Community for scientific research",
  "reference": "https://example.com/science-group"
}
```

- **Existing Group (200):**
```json
{
  "id": 1,
  "name": "Tech Innovators",
  "description": "Group for technology enthusiasts",
  "reference": "https://example.com/tech-group"
}
```

---

### 3. **Retrieve a Specific Group Space**
Get detailed information about a specific group space.

**Endpoint:**
```
GET /api/groups/{id}/
```

**Response Example:**
```json
{
  "id": 1,
  "name": "Tech Innovators",
  "description": "Group for technology enthusiasts",
  "reference": "https://example.com/tech-group"
}
```

---

### 4. **Update a Group Space**
Update an existing group space (requires authentication).

**Endpoint:**
```
PUT/PATCH /api/groups/{id}/
```

**Request Body:**
```json
{
  "description": "Updated group description"
}
```

**Response Example:**
```json
{
  "id": 1,
  "name": "Tech Innovators",
  "description": "Updated group description",
  "reference": "https://example.com/tech-group"
}
```

---

### 5. **Delete a Group Space**
Delete a specific group space (requires authentication).

**Endpoint:**
```
DELETE /api/groups/{id}/
```

**Response:**
```
204 No Content
```

---

## Authentication
- **Create, update, and delete:** Requires authentication.
- **Retrieve and list:** Public access.
