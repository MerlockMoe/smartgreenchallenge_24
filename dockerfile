FROM nvcr.io/nvidia/pytorch:23.04-py3
COPY requirements.txt .
RUN pip uninstall opencv-python
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y libgl1