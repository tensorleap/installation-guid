FROM --platform=linux/amd64 tensorflow/tensorflow:2.11.0-gpu as base-amd64
FROM --platform=linux/arm64 armswdev/tensorflow-arm-neoverse:r22.12-tf-2.11.0-onednn-acl as base-arm64

ARG TARGETARCH=amd64
FROM base-${TARGETARCH}

USER root
ENV PATH="/root/.local/bin:$PATH"
ENV PATH="$HOME/.local/bin:$PATH"

WORKDIR /app

RUN apt-key del 7fa2af80
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
RUN apt update
RUN apt install -y python3-opencv python3.8-venv

RUN pip install --upgrade pip
RUN curl --retry 3 --retry-delay 2 -sSL https://install.python-poetry.org | python -

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN poetry export -f requirements.txt --output requirements.txt --dev --without-hashes
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY dnn_checks dnn_checks

CMD ["python", "-m", "dnn_checks.tf_gpu_check"]