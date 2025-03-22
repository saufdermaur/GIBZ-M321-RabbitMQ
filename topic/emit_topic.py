import sys
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost"),
)
channel = connection.channel()

channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

print("Enter messages in the format: <routing_key> <message>")
print("Press CTRL+C to exit.")

try:
    while True:
        user_input = input("> ").strip()
        if not user_input:
            continue
        
        parts = user_input.split(" ", 1)
        if len(parts) < 2:
            print("Invalid format. Use: <routing_key> <message>")
            continue
        
        routing_key, message = parts
        channel.basic_publish(
            exchange="topic_logs",
            routing_key=routing_key,
            body=message,
        )
        print(f" [x] Sent {routing_key}:{message}")

except KeyboardInterrupt:
    print("\nExiting...")
    connection.close()
    sys.exit(0)
