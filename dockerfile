FROM nvcr.io/nvidia/pytorch
RUN cd data/UAVWeedSegmentation/
COPY requirements.txt .
RUN pip uninstall python-opencv
RUN pip install -r requirements.txt