FROM ubuntu:22.04

# install app dependencies
COPY pyproject.toml pyproject.toml
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install uv ruff mypy
RUN uv sync