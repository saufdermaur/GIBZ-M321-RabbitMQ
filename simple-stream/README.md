# RabbitMQ

## Running RabbitMQ

Community docker image

```
docker run -it --rm --name rabbitmq -p 5552:5552 -p 15672:15672 -p 5672:5672 -e RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS='-rabbitmq_stream advertised_host localhost' rabbitmq:4-management
```

Python 

```
pip install rstream
```

## Simple stream

### Run example

```
cd simple-stream
```

`send.py` will send a "Hello World!" message to the stream each time it is executed. `receive.py` will get all the messages from the stream.

```
python receive.py
```

```
python send.py
```

We see, that the producers message is received by the receiver. To demonstrate the differences between the queue and the stream we can do the following:

Consumer 1:

```
python receive.py
```

Producer:
```
python send.py
```

```
python send.py
```

```
python send.py
```

Now a total of three "Hello, World!"-messages will be received by the consumer. As streams don't have acknowledgements, all consumers will get all published messages, to show that, we need another consumer:

Consumer 2:

```
python receive.py
```

Now we see, that the new consumer also receives all sent messages. In contrast, the queue wouldn't have done that, because the first consumer acknowleged the messages and thus removed them from the queue.