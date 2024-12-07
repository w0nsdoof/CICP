# Authentication API Usage Guide

## 1. User Login

```
POST /auth/login/
```

### Request Body

```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

### Response

```json
{
  "refresh": "long_refresh_token_string",
  "access": "long_access_token_string"
}
```

## 2. User Registration

```
POST /auth/register/
```

### Request Body

```json
{
  "email": "newuser@example.com",
  "password": "strongpassword",
  "username": "optional_username"
  // other required user fields
}
```

### Response

```json
{
  "message": "User registered successfully!",
  "user": {
    "email": "newuser@example.com"
    // other user details
  }
}
```

## 3. Forgot Password

```
POST /auth/forgot_password/
```

### Request Body

```json
{
  "email": "user@example.com"
}
```

### Response

```json
{
  "message": "Password reset email sent."
}
```

## 4. Reset Password

```
POST /auth/reset_password/{uid}/{token}/
```

### Request Body

```json
{
  "password": "newpassword"
}
```

Or use "GENERATE_RANDOM" to auto-generate a password that would be sent to email

### Response

```json
{
  "message": "Password reset successful."
}
```

## Error Handling

- 400: Invalid input
- 404: User not found
- 401: Authentication failed
