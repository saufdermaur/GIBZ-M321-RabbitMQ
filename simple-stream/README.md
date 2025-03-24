# RabbitMQ Stream Example

This project demonstrates the use of RabbitMQ's streams using Python and the rstream library. Unlike traditional queues, streams retain all messages, and multiple consumers can read the same messages independently.

## Running RabbitMQ with Stream Plugin

To quickly set up RabbitMQ with stream capabilities, use the official Docker image:

```
docker run -it --rm --name rabbitmq -p 5552:5552 -p 15672:15672 -p 5672:5672 -e RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS='-rabbitmq_stream advertised_host localhost' rabbitmq:4-management
```

When the server is running, enable the management plugins:

```
docker exec rabbitmq rabbitmq-plugins enable rabbitmq_stream rabbitmq_stream_management 
```

* Ports:
    * 5672: AMQP (default messaging protocol)
    * 5672: Management console (default username: guest, password: guest)
    * 5552: Stream protocol

## Installing the Required Library

Install the rstream library to interact with RabbitMQ streams:

```
pip install rstream
```

## Running the Example

Navigate to the simple-stream directory:

```
cd simple-stream
```

## Sending and Receiving Messages

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

## Demonstrating Stream Characterisitics

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

## Code Explanation

### Producer (send.py)
* Establishes a connection with the RabbitMQ stream server.
* Creates a stream named hello-python-stream.
* Sends a message to the stream.

### Consumer (receive.py)
* Connects to the RabbitMQ stream server and subscribes to the same stream.
* Listens for and prints incoming messages.
* Uses OffsetType.FIRST to start from the beginning of the stream.