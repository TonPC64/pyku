import logging
import os
import time
import json
from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """
    CustomJsonFormatter
    append necessary fields for iu kibana
    """

    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(
            log_record, record, message_dict)

        now = round(time.time() * 1000)
        log_record['timestamp'] = now
        log_record['log_level'] = record.levelname.lower()
        log_record['type'] = 'app_log'
        log_record['msg'] = record.message
        del log_record['message']


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log_level = os.getenv("LOG_LEVEL")
if log_level:
    log.setLevel(log_level.upper())

logHandler = logging.StreamHandler()
formatter = CustomJsonFormatter()
logHandler.setFormatter(formatter)
log.propagate = False
log.addHandler(logHandler)
