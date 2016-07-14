#from __future__ import absolute_import
import importlib
import argparse,json
mod = importlib.import_module("scrapy_cluster.kafka-monitor.kafka_monitor")
KafkaMonitor=mod.KafkaMonitor

KAFKA_HOSTS = 'kafka-svc1:9092'
kafka_monitor = KafkaMonitor('localsettings.py')

kafka_monitor.setup(level='INFO', log_file='INFO',
                    json='INFO')
json_req='{"url": "http://istresearch.com", "appid":"testapp", "crawlid":"ABC123"}'
try:
    parsed = json.loads(json_req)
except ValueError:
    kafka_monitor.logger.info("JSON failed to parse")

kafka_monitor.feed(parsed)
