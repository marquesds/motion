FROM python:3.11.3-slim-bullseye
MAINTAINER Lucas Marques <lucasmarquesds@gmail.com>

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

RUN pip install virtualenv
RUN python -m venv .venv
RUN . .venv/bin/activate
RUN pip install -U pip

EXPOSE 9000

CMD ["uwsgi", "--ini", "uwsgi.ini"]
