FROM python:3.12

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app
RUN ls -al

COPY devops/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8075

ENTRYPOINT ["/app/entrypoint.sh"]

