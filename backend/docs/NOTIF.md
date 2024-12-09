# Notification API Usage Guide

A simple notification system implemented in Django Rest Framework (DRF). This API allows users to send, retrieve, and manage notifications.

## Features
- Create notifications
- Retrieve all notifications for the authenticated user
- Mark notifications as read
- Support for system and user-generated notifications

---

## API Endpoints

### 1. **Get All Notifications**
Retrieve all notifications for the authenticated user.

**Endpoint:**
```
GET /api/notifications/
```

**Response Example:**
```json
[
  {
    "id": 1,
    "sender": "System",
    "recipient": "john_doe",
    "content": "Welcome to the platform!",
    "type": "info",
    "is_read": false,
    "created_at": "2024-12-07T10:00:00Z"
  },
  {
    "id": 2,
    "sender": "alice",
    "recipient": "john_doe",
    "content": "You have a new message.",
    "type": "message",
    "is_read": false,
    "created_at": "2024-12-07T10:15:00Z"
  }
]
```

---

### 2. **Create a Notification**
Create a new notification for a user.

**Endpoint:**
```
POST /api/notifications/
```

**Request Example:**
```json
{
  "recipient": 2,
  "content": "You have a new alert!",
  "type": "alert"
}
```

**Response Example:**
```json
{
  "id": 3,
  "sender": "admin_user",
  "recipient": "jane_doe",
  "content": "You have a new alert!",
  "type": "alert",
  "is_read": false,
  "created_at": "2024-12-07T10:30:00Z"
}
```

> **Note:** The `sender` is automatically set to the authenticated user.

---

### 3. **Mark a Notification as Read**
Update a notification's `is_read` status to `true`.

**Endpoint:**
```
PATCH /api/notifications/<id>/
```

**Request Example:**
```json
{
  "is_read": true
}
```

**Response Example:**
```json
{
  "id": 1,
  "sender": "System",
  "recipient": "john_doe",
  "content": "Welcome to the platform!",
  "type": "info",
  "is_read": true,
  "created_at": "2024-12-07T10:00:00Z"
}
```

---

### 4. **Delete a Notification**
Delete a notification by ID.

**Endpoint:**
```
DELETE /api/notifications/<id>/
```

**Response:**
```
204 No Content
```

---

## Real-Time Notifications
For real-time notifications, integrate WebSocket or push notification services to notify users when new notifications are created.

---

## Authentication
All endpoints require authentication using a token or session. Ensure users can only access their notifications.

---

## Models Overview
- **Sender:** User who sent the notification (optional for system notifications).
- **Recipient:** User who receives the notification.
- **Content:** The main message of the notification.
- **Type:** The category of notification (`info`, `alert`, or `message`).
- **Read Status:** Indicates if the notification has been read.
- **Timestamps:** Auto-generated timestamps for creation.



