# container images nvidia pytorch 21.02
FROM c-adas-dldi-baseimages-docker-v.eu.artifactory.conti.de/nvidia/pytorch:21.02-py3-continental.v1

ARG https_proxy=http://sia-proxy-basic.geo.conti.de:3128
ARG http_proxy=http://sia-proxy-basic.geo.conti.de:3128
 
RUN printf 'Acquire::http::Proxy "%s";' ${http_proxy} > /etc/apt/apt.conf && \
  printf 'Acquire::https::Proxy "%s";' ${https_proxy} >> /etc/apt/apt.conf
 
ARG CERT_PATH=/usr/local/share/ca-certificates/ContinentalCorporateITSecurity-ContinentalAG.crt
ARG PIP_REPO=https://eu.artifactory.conti.de/artifactory/api/pypi/c_adas_cip_pypi_v/simple

# Install torch and torchvision
# RUN pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 --extra-index-url https://download.pytorch.org/whl/torch_stable.html

RUN apt-get update -y && apt-get install -y libgl1-mesa-glx

# pip upgrade
RUN pip install --no-cache-dir         --upgrade pip

# Install python packages
RUN pip install --no-cache-dir         pytorch-warmup==0.1.0 \
                                       opencv-python==4.2.0.32 \
                                       PyQt5==5.15.6 \
                                       PyQt5-Qt5==5.15.2 \
                                       PyQt5-sip==12.10.1 \
                                       yapf==0.32.0 \
                                       einops==0.4.1\
									   addict\
									   timm\
                     thop\
									   open3d==0.15.2
COPY entrypoint.sh /entrypoint
RUN chmod o+rx /entrypoint
 
WORKDIR /app
COPY . .
RUN chmod -R o+rwx /app
 
CMD ["/entypoint"]
