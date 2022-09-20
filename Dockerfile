FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s
ENV DATABASE_URL=sqlite:///db/oc-lettings-site.sqlite3
ENV SQLITE_URL=sqlite:///db/oc-lettings-site.sqlite3

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]