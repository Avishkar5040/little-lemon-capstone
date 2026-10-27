========================================================================
Little Lemon Restaurant Web Application API - Capstone Project
========================================================================

DESCRIPTION:
This project implements the back-end API for Little Lemon restaurant using
Django REST Framework and a MySQL database. It supports table bookings,
menu management, user authentication, and unit testing.

BASE URL:
http://127.0.0.1:8000/

STATIC HTML CONTENT:
GET  /                      -> Little Lemon home page (serves static HTML & CSS)

USER REGISTRATION & AUTHENTICATION ENDPOINTS (Djoser):
POST /auth/users/           -> Register a new user (params: username, password)
POST /auth/token/login/     -> Generate authentication token
POST /auth/token/logout/    -> Invalidate authentication token
POST /api-token-auth/       -> Alternative DRF token generation

MENU ITEM ENDPOINTS:
GET  /api/menu-items/       -> List all menu items (public / authenticated)
POST /api/menu-items/       -> Create a new menu item (admin / authenticated)
GET  /api/menu-items/<id>/  -> Retrieve a single menu item
PUT  /api/menu-items/<id>/  -> Update a single menu item
DELETE /api/menu-items/<id>/-> Delete a single menu item

TABLE BOOKING ENDPOINTS:
GET  /api/booking/tables/   -> List all table reservations (Token required)
POST /api/booking/tables/   -> Create a table booking (Token required)
GET  /api/booking/tables/<id>/ -> Retrieve single reservation
PUT  /api/booking/tables/<id>/ -> Update single reservation
DELETE /api/booking/tables/<id>/ -> Delete reservation

UNIT TESTS:
Run all test cases using:
python manage.py test

TESTING WITH INSOMNIA / POSTMAN:
Add header for protected booking endpoints:
Authorization: Token <YOUR_AUTH_TOKEN>
========================================================================
