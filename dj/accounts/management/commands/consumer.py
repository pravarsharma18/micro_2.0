import json
import pika
from django.core.management.base import BaseCommand
from accounts.models import User

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', "5672", heartbeat=600, blocked_connection_timeout=300))
queue_name = "users"
exchange = "flask_exchange"
bindingKey = "add.user"

class Command(BaseCommand):
    def callback(self, ch, method, properties, body):
        print("Received in users...")
        data = json.loads(body)
        print(data)
        User.objects.create(**data)
        print("User created.....")

    def setup(self):
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='topic')
        # This method creates or checks a queue
        channel.queue_declare(queue=queue_name)
        # Binds the queue to the specified exchang
        channel.queue_bind(queue=queue_name, exchange=exchange, routing_key=bindingKey)
        channel.basic_consume(queue=queue_name, on_message_callback=self.callback, auto_ack=True)
        print(' [*] Waiting for data for ' + queue_name + '. To exit press CTRL+C')
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()

    def handle(self, *args, **options):
        self.setup()
