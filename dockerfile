FROM nvcr.io/nvidia/pytorch:24.01-py3
COPY requirements.txt .
RUN pip uninstall python-opencv
RUN pip install -r requirements.txt