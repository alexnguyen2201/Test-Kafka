
from confluent_kafka import Consumer, KafkaException
import sys
import json
import time  # noqa


if __name__ == '__main__':

    broker = 'localhost: 29092'
    group = 'mygroup'
    topics = 'views'
    conf = {
        'bootstrap.servers': broker,
        'group.id': group,
        'session.timeout.ms': 6000,
        'auto.offset.reset': 'earliest'
    }

    c = Consumer(conf)
    c.subscribe([topics])
    try:
        while True:
            msg = c.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:

                msg = msg.value()
                msg = json.loads(msg)
                time.sleep(1)
                print(msg)

    except KeyboardInterrupt:
        sys.stderr.write('%% Aborted by user\n')

    finally:
        c.close()
