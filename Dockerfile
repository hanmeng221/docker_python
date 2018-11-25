FROM python:3.5.2

MAINTAINER hanmeng hanmeng@bupt.edu.cn

RUN mkdir -p /usr/src \
	&& mkdir -p /usr/goal
COPY ./execution_exe.py  /usr/src

WORKDIR /usr/src

