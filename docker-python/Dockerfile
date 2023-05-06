# Derive a python image
FROM python:3.7-alpine

# Label as a key value pair
LABEL maintainer="ridwan"

# Any working directory can be chosen
WORKDIR /usr/app/src

# copy the python file there
COPY trial.py ./
# this will make the structure look like this /usr/app/src/trial.py

# CMD instruction will run the script in the image
# CMD ["python", "./trial.py"]

CMD ["python", "./trial.py"]
