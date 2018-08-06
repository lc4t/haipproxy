#!/bin/bash
nohup python crawler_booter.py --usage crawler common ajax > crawler.log 2>&1 &
nohup python scheduler_booter.py --usage crawler common ajax > crawler_scheduler.log 2>&1 &
nohup python crawler_booter.py --usage validator init bili > init_validator.log 2>&1 &
nohup python scheduler_booter.py --usage validator bili > validator_scheduler.log 2>&1 &
#nohup python squid_update.py --usage bili --interval 3 > squid.log 2>&1 &
#rm -rf /var/run/squid.pid
#squid -N -d1
