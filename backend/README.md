# .env file

```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password # not your regular password, remove this comment on .env
DEFAULT_FROM_EMAIL=book_store@gmail.com

DB_NAME=book_store_db
DB_USER=dev_user
DB_PASSWORD=adminadminadmin
DB_HOST=localhost
DB_PORT=5432

CELERY_BROKER="redis://localhost:6379/0"
```

## Running the app (Things to do)

1. Make sure celery is up and running
Be sure that redis is running on your system

```bash
celery -A book_store worker -l info & celery -A book_store beat -l info
```