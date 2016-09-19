#from __future__ import absolute_import
from multiprocessing import Process
import importlib
import argparse,json
mod = importlib.import_module("scrapy_cluster.kafka-monitor.kafka_monitor")
from models import PageDocument

from celery import task

def feed(json_req):
    KafkaMonitor=mod.KafkaMonitor
    
    #KAFKA_HOSTS = 'kafka.1.svc:9092'
    kafka_monitor = KafkaMonitor('localsettings.py')
    
    kafka_monitor.setup(level='INFO', log_file='INFO',
                        json='INFO')
    try:
        parsed = json.loads(json_req)
    except ValueError:
        kafka_monitor.logger.info("JSON failed to parse")

    #data={}
    #data['url'] = json_req['url']
    #data['title'] = json_req['title']
    #data['raw_content'] = json_req['raw_content']
    #data['extract_content'] = json_req['extract_content']

    #serializer = PageSerializer(data=data)
    #if serializer.is_valid():
    #    serializer.save()
    
    return kafka_monitor.feed(parsed)


@task()
def crawl(json_req):
    p = Process(target=feed, args=(json_req))
    p.start()
    p.join()
