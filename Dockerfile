FROM pypy:3.9-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip install --upgrade pip && \
    pip install online-judge-tools

COPY ./src /app

# 環境変数を設定
ENV PYPY_GC_L2=262144
ENV PYPY_GC_L3=8388608