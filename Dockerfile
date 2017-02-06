FROM python:2-onbuild
RUN cd src
CMD [ "./redis_monitor.sh" ]
