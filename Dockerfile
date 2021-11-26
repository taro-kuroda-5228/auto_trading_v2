FROM python:3.8
# NOTE: This image's web page link
# https://hub.docker.com/layers/python/library/python/3.8/images/sha256-febc7f300ce1e609eae193af7a77616c170333ab3c2a9efa3b80f314d0e2ff4b?context=explore

RUN apt-get update -y \
    && apt-get upgrade -y

RUN curl -sL https://deb.nodesource.com/setup_12.x \
    | bash - \
    && apt-get install -y --no-install-recommends \
    wget \
    git \
    vim \
    curl \
    make \
    cmake \
    nodejs \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /var/cache/apt/* \
        /usr/local/src/* \
        /tmp/*

# install python library
COPY requirements.txt .
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt \
    && rm -rf ~/.cache/pip

# install jupyterlab & extentions
RUN pip3 install --upgrade --no-cache-dir \
    'jupyterlab~=3.0' \
    jupyterlab_code_formatter \
    black \
    isort \
    && rm -rf ~/.cache/pip \
    && jupyter labextension install \
      @hokyjack/jupyterlab-monokai-plus \
      @ryantam626/jupyterlab_code_formatter \
      @jupyterlab/toc \
    && jupyter serverextension enable --py jupyterlab_code_formatter

# make directory
RUN mkdir -p /root/.jupyter/lab/user-settings/@ryantam626/jupyterlab_code_formatter/ \
    && mkdir -p /root/.jupyter/lab/user-settings/@jupyterlab/notebook-extension/ \
    && mkdir -p /root/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/
    
# copy setting files
COPY envs/settings.jupyterlab-settings /root/.jupyter/lab/user-settings/@ryantam626/jupyterlab_code_formatter/
COPY envs/tracker.jupyterlab-settings /root/.jupyter/lab/user-settings/@jupyterlab/notebook-extension/
COPY envs/themes.jupyterlab-settings /root/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/

WORKDIR /home/work/
