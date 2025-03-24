# RabbitMQ Fanout Exchange Example

This project demonstrates the use of RabbitMQ's fanout exchange using Python and the pika library. In a fanout exchange, messages sent to an exchange are broadcast to all queues bound to it.

## Running RabbitMQ

To quickly set up RabbitMQ, you can use the official Docker RabbitMQ image with the management plugin enabled:

```
docker run -d -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management
```

* The RabbitMQ server will be accessible at localhost:5672 for messaging and localhost:15672 for management (default username: guest, password: guest).

## Installing the Required Library

Install the pika library to communicate with RabbitMQ:

```
pip install pika
```

## Running the Example

Navigate to the fanout-exchange directory:

```
cd fanout-exchange
```

## Sending and Receiving Messages

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

## Code Explanation

### Producer (emit_log.py)
* Establishes a connection to the RabbitMQ server.
* Declares a fanout exchange named logs.
* Sends a message to the exchange.

### Consumer (receive_logs.py)
* Connects to the RabbitMQ server and declares the same fanout exchange.
* Creates a temporary, exclusive queue bound to the exchange.
* Listens for and prints incoming messages.