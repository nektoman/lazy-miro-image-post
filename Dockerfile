FROM python:3.11.0b5-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#START
CMD ["python", "./main.py"]
#docker build . -t lazy-miro-image-post
#docker run --name miro_image --rm -d lazy-miro-image-post  