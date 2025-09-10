# Django Backend for Interactive Resume

This project is a **backend in Python with Django REST Framework** that serves my CV data on demand, allowing my web CV to dynamically consume the information in JSON format.

# Main Goals:

- Display work experience, education, and skills from a **REST API**.
- Deploy the backend for free on Render (free plan), showcasing skills in  
  Python, Django, APIs, and Cloud Deployment.


## Public API URL

The API is live at:

```
https://cv-backend-ttra.onrender.com/api/experiences/
```


## Usage in the frontend

To load the data into the CV website:

```javascript
fetch("https://cv-backend-ttra.onrender.com/api/experiences/")
  .then(res => res.json())
  .then(data => console.log(data));
```


## Repository structure

```
cv-backend/
├── portfolio/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── cvapi/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── manage.py
```

- `portfolio/`: the app defining the model, serializer, views, and API routes.
- `cvapi/`: general Django configuration.
- API available at `/api/experiences/`.

---

## How to work with this project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/cv-backend.git
   cd cv-backend
   ```

2. Set up the virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   # .\venv\Scripts\activate  # Windows PowerShell

   pip install -r requirements.txt
   ```

3. Apply migrations and create a superuser:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Run locally:

   ```bash
   python manage.py runserver
   ```

5. Access the admin panel at `http://127.0.0.1:8000/admin/` to add "Experiences" and check the API at `http://127.0.0.1:8000/api/experiences/`.

---

### Conclusion

This backend allows my interactive CV to be **always up-to-date without touching the frontend**, simply by managing data through the Admin or API.  
It is a clear demonstration of skills in backend development, APIs, cloud deployment, and dynamic frontend consumption.

---