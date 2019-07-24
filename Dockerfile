# ======================================================================
# @author: Guilherme Vasconcellos <guiyllw@hotmail.com>
# @version: 1.0.0
#
# @description: Dockerfile to build challenge LuizaLabs api
# ======================================================================
FROM python:3.7.4-alpine

WORKDIR /api

# Copy and install only production dependencies
COPY src .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "server.py" ]
