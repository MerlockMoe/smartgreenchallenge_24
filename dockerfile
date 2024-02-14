FROM nvcr.io/nvidia/pytorch:22.02-py3
COPY requirements.txt .
COPY model_unet_resnet34_dil0_bilin1_retrained.pt .
RUN pip uninstall opencv-python
RUN pip install -r requirements.txt