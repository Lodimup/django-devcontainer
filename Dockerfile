FROM python:3.11-slim

ARG SKIP_ENV_CHECK=True

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY app /app/
RUN python manage.py collectstatic --noinput

EXPOSE 8000

ENTRYPOINT ["hypercorn", "app.asgi:application"]
CMD ["--bind", "0.0.0.0:8000", "--workers", "4"]
