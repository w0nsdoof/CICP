# Authentication API Usage Guide

This API provides endpoints for user authentication, including login, registration, password reset, and error handling.

---

## Features
- User login with access and refresh tokens
- New user registration
- Password recovery and reset options
- Comprehensive error handling for authentication workflows

---

## Authentication Endpoints

### 1. **User Login**
Authenticate a user and retrieve access and refresh tokens.

**Endpoint:**
```
POST /auth/login/
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

**Response Example:**
```json
{
  "refresh": "long_refresh_token_string",
  "access": "long_access_token_string"
}
```

---

### 2. **User Registration**
Register a new user with email, password, and username.

**Endpoint:**
```
POST /auth/register/
```

**Request Body:**
```json
{
  "email": "new_example@example.com",
  "password": "strongpassword",
  "username": "example"
}
```

**Response Example:**
```json
{
  "message": "User registered successfully!",
  "user": {
    "username": "example",
    "email": "new_example@example.com"
  }
}
```

---

### 3. **Forgot Password**
Send a password reset email to the user.

**Endpoint:**
```
POST /auth/forgot_password/
```

**Request Body:**
```json
{
  "email": "user@example.com"
}
```

**Response Example:**
```json
{
  "message": "URL for password reset sent via email."
}
```

---

### 4. **Reset Password**
Reset the user's password using a unique URL token.

**Endpoint:**
```
POST /auth/reset_password/{uid}/{token}/
```

**Request Body Options:**
1. **Set a New Password:**
   ```json
   {
     "password": "newpassword"
   }
   ```

2. **Generate a Random Password (sent via email):**
   ```json
   {
     "password": "GENERATE_RANDOM"
   }
   ```

**Response Example:**
```json
{
  "message": "Password reset successful."
}
```

---

## Error Handling

Authentication endpoints return appropriate error codes and messages for common scenarios:

- **400 Bad Request:** Invalid input data.
- **404 Not Found:** User not found.
- **401 Unauthorized:** Authentication failed (e.g., incorrect password, expired token).

---

## Token Management
- **Access Token:** Short-lived token for API access.
- **Refresh Token:** Long-lived token used to request new access tokens. 