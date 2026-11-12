FROM python:3.12.2-bookworm

RUN apt-get update && apt-get install -y \
    python3-dev \
    libgdal-dev \
    graphviz \
    graphviz-dev

WORKDIR /usr/src/app

RUN pip install --upgrade pip setuptools

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY start.sh /start.sh

RUN chmod +x /start.sh

EXPOSE 8000

CMD ["/start.sh"]