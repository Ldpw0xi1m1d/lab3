FROM python:3.11

WORKDIR app

COPY . .

ENV message simonov_roman
ENV n 8

CMD ["python", "1.py"]