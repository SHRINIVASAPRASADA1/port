# Use the official Python image as a base
FROM python

WORKDIR /app

COPY app.py .
COPY portfolioshrinivasaprasada-firebase-adminsdk-qlcxs-77577b3327.json .
COPY . .

RUN pip install Flask
RUN pip install Flask Flask-SocketIO
RUN pip install Flask firebase_admin

CMD ["python3", "app.py"]