# News API Usage Guide

This API allows users to manage news articles, including creating, retrieving, updating, and deleting them. It also provides endpoints to manage associated tags.

---

## Features
- List all news articles with optional filters
- Create, update, and delete news articles (requires authentication)
- Manage tags for categorizing articles

---

## News Endpoints

### 1. **List All News Articles**
Retrieve a paginated list of news articles.

**Endpoint:**
```
GET /api/news/
```

**Query Parameters:**
- `page`: Page number (default: 1)
- `page_size`: Number of articles per page (default: 10, max: 100)
- `author`: Filter articles by author (username or ID)
- `search`: Search for articles by title or content

**Example Requests:**
```
GET /api/news/
GET /api/news/?page=2&page_size=20
GET /api/news/?author=johndoe
GET /api/news/?author=5
GET /api/news/?search=technology
```

**Response Example:**
```json
[
  {
    "id": 1,
    "title": "Breaking News",
    "summary": "Brief summary of the article",
    "author": {
      "id": 1,
      "username": "johndoe"
    },
    "tags": [
      { "id": 1, "name": "Technology" },
      { "id": 2, "name": "Science" }
    ],
    "created_at": "2024-12-07T10:00:00Z"
  }
]
```

---

### 2. **Create a New News Article**
Create a new news article (requires authentication).

**Endpoint:**
```
POST /api/news/
```

**Request Body:**
```json
{
  "title": "Breaking News Title",
  "content": "Full article content",
  "summary": "Optional brief summary",
  "tags": [1, 2]
}
```

**Response Example:**
```json
{
  "id": 2,
  "title": "Breaking News Title",
  "content": "Full article content",
  "summary": "Optional brief summary",
  "tags": [
    { "id": 1, "name": "Technology" },
    { "id": 2, "name": "Science" }
  ],
  "author": {
    "id": 1,
    "username": "admin"
  },
  "created_at": "2024-12-07T10:30:00Z"
}
```

---

### 3. **Retrieve a Specific News Article**
Get detailed information about a specific article.

**Endpoint:**
```
GET /api/news/{id}/
```

**Response Example:**
```json
{
  "id": 2,
  "title": "Breaking News Title",
  "content": "Full article content",
  "summary": "Optional brief summary",
  "tags": [
    { "id": 1, "name": "Technology" },
    { "id": 2, "name": "Science" }
  ],
  "author": {
    "id": 1,
    "username": "admin"
  },
  "created_at": "2024-12-07T10:30:00Z",
  "updated_at": "2024-12-07T11:00:00Z"
}
```

---

### 4. **Update a News Article**
Update an existing news article (requires authentication).

**Endpoint:**
```
PUT /api/news/{id}/
```

**Request Body Example:**
```json
{
  "title": "Updated News Title",
  "tags": [1, 3]
}
```

**Response Example:**
```json
{
  "id": 2,
  "title": "Updated News Title",
  "content": "Full article content",
  "summary": "Optional brief summary",
  "tags": [
    { "id": 1, "name": "Technology" },
    { "id": 3, "name": "Business" }
  ],
  "author": {
    "id": 1,
    "username": "admin"
  },
  "created_at": "2024-12-07T10:30:00Z",
  "updated_at": "2024-12-07T12:00:00Z"
}
```

---

### 5. **Delete a News Article**
Delete a specific article (requires authentication).

**Endpoint:**
```
DELETE /api/news/{id}/
```

**Response:**
```
204 No Content
```

---

## Tags Endpoints

### 1. **List All Tags**
Retrieve a list of all available tags.

**Endpoint:**
```
GET /api/tags/
```

**Response Example:**
```json
[
  { "id": 1, "name": "Technology", "description": "Tech-related news articles" },
  { "id": 2, "name": "Science", "description": "Science-related news articles" }
]
```

---

### 2. **Create a New Tag**
Create a new tag (requires authentication).

**Endpoint:**
```
POST /api/tags/
```

**Request Body:**
```json
{
  "name": "Technology",
  "description": "Tech-related news articles"
}
```

**Response Example:**
```json
{
  "id": 3,
  "name": "Technology",
  "description": "Tech-related news articles"
}
```

---

### 3. **Retrieve a Specific Tag**
Retrieve details about a specific tag.

**Endpoint:**
```
GET /api/tags/{id}/
```

**Response Example:**
```json
{
  "id": 1,
  "name": "Technology",
  "description": "Tech-related news articles"
}
```

---

### 4. **Update a Tag**
Update details of a specific tag (requires authentication).

**Endpoint:**
```
PUT/PATCH /api/tags/{id}/
```

**Request Body Example:**
```json
{
  "description": "Updated description for the tag"
}
```

---

### 5. **Delete a Tag**
Delete a specific tag (requires authentication).

**Endpoint:**
```
DELETE /api/tags/{id}/
```

**Response:**
```
204 No Content
```

---

## Authentication
All `POST`, `PUT`, `PATCH`, and `DELETE` endpoints require authentication. Ensure users can only modify resources they own.
