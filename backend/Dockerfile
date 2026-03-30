FROM python:3.11-slim
WORKDIR /app
RUN useradd -m -u 1000 appuser
COPY app.py .
RUN chown appuser:appuser app.py
USER appuser
EXPOSE 8080
CMD ["python", "app.py"]
