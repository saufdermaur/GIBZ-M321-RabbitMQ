# RabbitMQ

## Running RabbitMQ

Community docker image

```
docker run -d -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management
```

Python pika

```
pip install pika
```

### Run example

```
cd fanout-exchange
```

`emit_log.py` will send a "Hello World!" message to the queue each time it is executed. `receive_logs.py` will get all the messages from the queue as soon as they arrive.

```
python receive_logs.py
```

```
python emit_log.py
```
