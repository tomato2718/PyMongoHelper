FROM python:3.10.10-slim-bullseye

WORKDIR /usr/src
COPY . ./app/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "-OOm", "app"]
CMD [""]
