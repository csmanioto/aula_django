# SLIM: Arround 120MB use debian base, better for compatibility   
# ALPINE: Arroung 5MB
FROM python:3.12-slim 

RUN pip install --upgrade pip
RUN pip install pipenv

#Security - working with no root user.
RUN useradd -ms /bin/bash user_app
USER user_app

WORKDIR /home/user_app/app


ENV PIPENV_VENV_IN_PROJECT=1

# Mantem a conexão com o container ativa.
CMD [ "tail", "-f", "/dev/null" ]

# COPY Pipfile.lock /home/user_app/app
# RUN pipenv install --system

# pip install --pre django
