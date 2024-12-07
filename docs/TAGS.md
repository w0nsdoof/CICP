# Tags API Usage Guide

## Tags Endpoints

### 1. List All Tags

```
GET /api/tags/
```

- Returns a list of all available tags
- No authentication required

#### Example Requests:

```
# Get all tags
GET /api/tags/

# Paginated tags (if implemented)
GET /api/tags/?page=1&page_size=10
```

### 2. Create a New Tag

```
POST /api/tags/
```

- Requires admin privileges
- Request Body:

```json
{
  "name": "Technology",
  "description": "Tech-related news articles"
}
```

#### Validation Rules:

- `name` is required and must be unique
- `description` is optional

### 3. Retrieve a Specific Tag

```
GET /api/tags/{id}/
```

- Returns detailed information about a specific tag

#### Example:

```
GET /api/tags/1/
```

### 4. Update a Tag

```
PUT /api/tags/{id}/
```

- Can update name or description

```json
{
  "name": "Updated Technology",
  "description": "Updated description of tech tags"
}
```

### 5. Partial Update of a Tag

```
PATCH /api/tags/{id}/
```

- Update only specific fields

```json
{
  "description": "New description without changing the name"
}
```

### 6. Delete a Tag

```
DELETE /api/tags/{id}/
```

- Removes the tag from the system
- May have cascading effects on associated news articles

## Example Scenarios

### Creating Multiple Tags

```bash
# Create first tag
POST /api/tags/
{
    "name": "Technology",
    "description": "Tech industry news"
}

# Create second tag
POST /api/tags/
{
    "name": "Politics",
    "description": "Political news and analysis"
}
```

### Using Tags with News

When creating a news article, you can associate these tags:

```json
POST /api/news/
{
    "title": "AI Breakthrough",
    "content": "Latest developments in AI technology",
    "tags": [1]  // ID of the "Technology" tag
}
```

## Error Responses

### Duplicate Tag Creation

```json
{
  "message": "Tag already exists",
  "tag": {
    "id": 1,
    "name": "Technology",
    "description": "Existing description"
  }
}
```

### Validation Errors

```json
{
  "name": ["This field is required"],
  "description": ["Maximum length is 200 characters"]
}
```

## Response Format

```json
{
  "id": 1,
  "name": "Technology",
  "description": "Tech-related news articles"
}
```
