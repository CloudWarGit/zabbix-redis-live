#!/bin/bash
python redis_live_daemon.py &
python redis_monitor_daemon.py &

while true;
do
  echo hello world;
  sleep 1
done
