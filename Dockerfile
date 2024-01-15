FROM python:3.8
WORKDIR /home/notebooks
RUN pip install streamlit pandas seaborn

COPY src/app.py /app/
COPY csv/employees.csv /app/csv/employees.csv

WORKDIR /app

ENTRYPOINT ["streamlit", "run", "app.py","--server.port=8501", "--server.address=0.0.0.0"]