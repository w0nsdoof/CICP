# GroupSpace API Usage Guide

## 1. List Group Spaces
```
GET /api/groups/
```
- Paginated list of group spaces
- Optional query parameters:
  - `page`: Page number
  - `page_size`: Items per page (max 100)

### Response
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

## 2. Create a Group Space
```
POST /api/groups/
```
### Request Body
```json
{
    "name": "Science Explorers",
    "description": "Community for scientific research",
    "reference": "https://example.com/science-group"
}
```

### Responses
- Success (201): New group created
- Existing Group (200): Returns existing group details

## 3. Retrieve a Specific Group Space
```
GET /api/groups/{id}/
```
### Response
```json
{
    "id": 1,
    "name": "Tech Innovators",
    "description": "Group for technology enthusiasts",
    "reference": "https://example.com/tech-group"
}
```

## 4. Update a Group Space
```
PUT/PATCH /api/groups/{id}/
```
### Request Body
```json
{
    "description": "Updated group description"
}
```

## 5. Delete a Group Space
```
DELETE /api/groups/{id}/
```

## Authentication
- Authenticated users can create/modify
- Read access is public
```