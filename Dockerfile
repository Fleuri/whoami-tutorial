FROM python:3.5-alpine
WORKDIR /app
COPY . .
RUN pip install flask
RUN apk add fortune
ENV FLASK_APP "app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True
CMD ["python", "app.py"]
