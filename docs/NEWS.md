# News API Usage Guide

## News Endpoints

### 1. List All News Articles

```
GET /api/news/
```

- Returns a paginated list of all news articles
- Optional query parameters:
  - `page`: Page number
  - `page_size`: Number of items per page (max 100)
  - `author`: Filter by author username or ID
  - `search`: Search through title and content

#### Example Requests:

```
GET /api/news/

GET /api/news/?page=2&page_size=20

GET /api/news/?author=johndoe
GET /api/news/?author=5

GET /api/news/?search=technology
```

### 2. Create a New News Article

```
POST /api/news/
```

- Requires authentication
- Request Body:

```json
{
  "title": "Breaking News Title",
  "content": "Full article content",
  "summary": "Optional brief summary", // Optional
  "tags": [1, 2] // Optional 
}
```

### 3. Retrieve a Specific News Article

```
GET /api/news/{id}/
```

- Returns detailed information about a specific news article

### 4. Update a News Article

```
PUT/PATCH /api/news/{id}/
```

- Requires authentication
- Can update title, content, tags, etc.

```json
{
  "title": "Updated Title",
  "tags": [1, 3] // Update tags
}
```

### 5. Delete a News Article

```
DELETE /api/news/{id}/
```

- Requires authentication
- Permanently removes the news article

## Tags Endpoints

### 1. List All Tags

```
GET /api/tags/
```

- Returns a list of all available tags

### 2. Create a New Tag

```
POST /api/tags/
```

```json
{
  "name": "Technology",
  "description": "Tech-related news articles"
}
```

### 3. Retrieve a Specific Tag

```
GET /api/tags/{id}/
```
- Response Format

```json
{
  "id": 1,
  "title": "Article Title",
  "content": "Article content",
  "author": {
    "id": 1,
    "username": "johndoe"
  },
  "tags": [{ "id": 1, "name": "Technology" }],
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-02T14:30:00Z"
}
```

### 4. Update a Tag

```
PUT/PATCH /api/tags/{id}/
```

```json
{
  "description": "Updated tag description"
}
```

### 5. Delete a Tag

```
DELETE /api/tags/{id}/
```
