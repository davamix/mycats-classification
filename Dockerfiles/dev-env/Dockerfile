FROM tensorflow/tensorflow:2.0.0b1-gpu-py3-jupyter

RUN apt update && apt install -y \
    libgtk2.0-dev libsm6 libxext6 libxrender1 libxrender-dev libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install Keras scikit-learn opencv-python tqdm Pillow pandas seaborn

RUN mkdir -p /home/work

WORKDIR /home/work

ENTRYPOINT ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--allow-root", "--no-browser", "."]
