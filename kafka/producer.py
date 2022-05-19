from confluent_kafka import Producer
import sys
import json


def producer():
    broker = 'localhost: 29092'
    topic = 'views'

    conf = {'bootstrap.servers': broker}

    p = Producer(**conf)

    def delivery_callback(err, msg):
        if err:
            sys.stderr.write('%% Message failed delivery: %s\n' % err)
        else:
            sys.stderr.write('%% Message delivered to %s [%d] @ %d\n' %
                             (msg.topic(), msg.partition(), msg.offset()))

    for number in range(100):
        data = {'number': number}
        data = json.dumps(data)

        p.produce(topic, data, callback=delivery_callback)
        p.poll(0)

        sys.stderr.write('%% Waiting for %d deliveries\n' % len(p))
        p.flush()


if __name__ == '__main__':
    producer()
