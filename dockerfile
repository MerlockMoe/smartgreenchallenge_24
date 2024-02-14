FROM nvcr.io/nvidia/l4t-pytorch:r35.2.1-pth2.0-py3
COPY requirements.txt .
RUN pip install -r requirements.txt