FROM python:3.10.0-alpine3.15
ADD . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5004
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
     CMD curl -f http://localhost:5004/health || exit 1
ENTRYPOINT [ "python","./main.py" ]