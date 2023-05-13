FROM python:3.11.3-slim-bullseye

# Extra packages
RUN apt-get update && \
	apt-get install -y --no-install-recommends \
	libssl1.1 \
	openssl \
	mime-support \
	make \
	gcc \
	python3-dev \
	mime-support \
	libffi-dev \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install -U pip

RUN pip install -r requirements.txt

EXPOSE 9000

CMD ["uwsgi", "--ini", "uwsgi.ini"]
