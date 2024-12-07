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
  "email": "new_example@example.com",
  "password": "strongpassword",
  "username": "example"
}
```

### Response

```json
{
    "message": "User registered successfully!",
    "user": {
        "username": "example",
        "email": "new_example@example.com"
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
  "message": "URL for password reset sent via email."
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

or generate random with password sent to email

```json
{
  "password": "GENERATE_RANDOM"
}

```
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
