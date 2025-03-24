# RabbitMQ

## Running RabbitMQ

Community docker image

```
docker run -it -d --rm --name rabbitmq -p 5552:5552 -p 15672:15672 -p 5672:5672 -e RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS='-rabbitmq_stream advertised_host localhost' rabbitmq:4-management
```

When the server is running, enable the management plugins:

```
docker exec rabbitmq rabbitmq-plugins enable rabbitmq_stream rabbitmq_stream_management 
```

Python pika

```
pip install pika
```

## Simple queue

![Simple queue](doc/queue.png)

### Running the example

```
cd simple-queue
```

`send.py` will send a "Hello World!" message to the queue each time it is executed. `receive.py` will get all the messages from the queue as soon as they arrive.

```
python3 receive.py
```

```
python3 send.py
```

Every message that is sent to a queue needs to go through an *exchange*, instead of setting one up explicitly, one can simply use the default exchange ''.

```python
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
```

## Simple stream

Unlike traditional queues, streams retain all messages, and multiple consumers can read the same messages independently.

When the server is running, enable the management plugins:

```
docker exec rabbitmq rabbitmq-plugins enable rabbitmq_stream rabbitmq_stream_management 
```

* Ports:
    * 5672: AMQP (default messaging protocol)
    * 5672: Management console (default username: guest, password: guest)
    * 5552: Stream protocol

Install the rstream library to interact with RabbitMQ streams:

```
pip install rstream
```

### Running the example

Navigate to the simple-stream directory:

```
cd simple-stream
```

1. Run the consumer (receive.py):

    This will listen for messages from the stream:

    ```
    python receive.py
    ```

2. Run the producer (send.py):

    This will send a message (default: "Hello, World!") to the stream:

    ```
    python send.py
    ```

You should see the message received by the consumer. Streams retain messages, allowing new consumers to access all previous messages.

### Demonstrating Stream Characterisitics

To showcase the stream's message retention, follow these steps:

* Start Consumer 1:

    ```
    python receive.py
    ```

* Send multiple messages:

    ```
    python send.py
    python send.py
    python send.py
    ```

* Consumer 1 will receive all messages. Now, start Consumer 2:

    ```
    python receive.py
    ```

### Code Explanation

#### Producer (send.py)
* Establishes a connection with the RabbitMQ stream server.
* Creates a stream named hello-python-stream.
* Sends a message to the stream.

#### Consumer (receive.py)
* Connects to the RabbitMQ stream server and subscribes to the same stream.
* Listens for and prints incoming messages.
* Uses OffsetType.FIRST to start from the beginning of the stream.

## Fanout exchange

In a fanout exchange, messages sent to an exchange are broadcast to all queues bound to it.

### Running the Example

Navigate to the fanout-exchange directory:

```
cd fanout-exchange
```

### Sending and Receiving Messages

1. Run the consumer (receive_logs.py):

    This will start listening for messages broadcast to the fanout exchange:

    ```
    python receive_logs.py
    ```

2. Run the producer (emit_log.py):

    This will send a message (default: "Hello World!") to all consumers connected to the fanout exchange:

    ```
    python emit_log.py
    ```

### Code Explanation

### Producer (emit_log.py)
* Establishes a connection to the RabbitMQ server.
* Declares a fanout exchange named logs.
* Sends a message to the exchange.

### Consumer (receive_logs.py)
* Connects to the RabbitMQ server and declares the same fanout exchange.
* Creates a temporary, exclusive queue bound to the exchange.
* Listens for and prints incoming messages.

## Topic exchange

In a topic exchange, messages will be routed to queues according to the pattern of their routing key.

### Running the example

```
cd topic
```

### Emitting messages with topics

This will start a client that can send messages with a routing key to a topic exchange.

```bash
python emit_topic.py
```

#### Inputs

The following inputs can be used: 

```bash
error.network Network is down!
```
```bash
error.database Database connection lost!
```
```bash
warning.memory Memory usage is high!
```
```bash
warning.cpu CPU temperature is high!
```
```bash
warning.disk Disk space running low!
```
```bash
info.startup Application has started.
```
```bash
debug.auth User authentication successful.
```

### Receiving messages based on a topic

The topics, or routing keys, can be added as input arguments to the `receive_topic.py` file.

A "#" can be used as a wildcard in a pattern. So for example a consumer with routing key "#" will listen to all topics.

```bash
python receive_topic.py "error.#" "warning.cpu" "warning.memory"
```

```bash
python receive_topic.py "warning.#" "debug.#" "info.#"
```

```bash
python receive_topic.py "#"
```

## Remote Procedure Calls

RabbitMQ also supports remote procedure calls (RPC), where a client can execute some functionality on a remote server.

### Running the example

```
cd rpc
```

In this configuration we have a client and a server. The client will create an exclusive callback queue, where the server can send messages to and the client can receive messages. The client will send a message containing the callback queue, so that the server knows where to send an answer. The server waits for messages in the `rpc_queue` and executes the function as soon as it receives a message. The client will then wait on a response from the callback queue. This way, a synchronous workflow is implemented between distributed systems with an asynchronous messaging system.

First we need to start the RPC server

```
python rpc_server.py
```

Then we can launch a client that will call for a remote execution of a fibonacci number.

```
python rcp_client.py
```