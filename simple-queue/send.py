import pika
import sys
import os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='hello')
    
    try:
        while True:
            message = input("Enter message (Ctrl+C to exit): ")
            channel.basic_publish(exchange='',
                                  routing_key='hello',
                                  body=message)
            print(f" [x] Sent '{message}'")
    except KeyboardInterrupt:
        print('\nInterrupted')
        connection.close()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == '__main__':
    main()
