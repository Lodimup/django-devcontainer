FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY app /app/

EXPOSE 8000

ENTRYPOINT ["hypercorn", "app.asgi:application"]
CMD ["--bind", "0.0.0.0:8000", "--workers", "4"]
