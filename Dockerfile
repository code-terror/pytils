FROM fuzzers/atheris:1.0.3-python3.8
WORKDIR /
COPY . /
RUN chmod +x fuzz-numeral.py
