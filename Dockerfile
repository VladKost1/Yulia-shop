FROM python:3.10

RUN apt update

RUN mkdir /Yulia_shop

WORKDIR /Yulia_shop

COPY ./src ./src
COPY commands ./commands

COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

ENTRYPOINT ["/bin/bash", "./commands/start_server.sh"]
CMD ["bash"]


