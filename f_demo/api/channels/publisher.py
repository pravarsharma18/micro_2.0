from conf.database import Config
import pika

class Publisher:
    def create_connection(self):
        param = pika.ConnectionParameters(host=Config.RABBIT_HOST, port=Config.RABBIT_PORT)
        return pika.BlockingConnection(param)

    def publish(self, routing_key, message):
        connection = self.create_connection()
        # Create a new channel with the next available channel number or pass in a channel number to use
        channel = connection.channel()
        # Creates an exchange if it does not already exist, and if the exchange exists,
        # verifies that it is of the correct and expected class.
        channel.exchange_declare(exchange=Config.RABBIT_EXCHANGE, exchange_type='topic')
        # Publishes message to the exchange with the given routing key
        channel.basic_publish(exchange=Config.RABBIT_EXCHANGE, routing_key=routing_key, body=message)
        print(' [x] Sent message %r for %r' % (message, routing_key))
