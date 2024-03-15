import os
import pika
import sys
import json
from json_to_pdf import json_to_pdf


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()
    channel.queue_declare(queue='expense-report')

    def callback(ch, method, properties, body):
        """
        This function deserializes the received message body,
        which is in the form of a serialized tuple.
        It then calls the function to convert a JSON object to a PDF.
        """
        deserialized_tuple = tuple(json.loads(body))
        json_obj, save_path = deserialized_tuple
        # print(f'JSON: {json_obj}; Save path: {save_path}')
        json_to_pdf(json_obj, save_path)

    channel.basic_consume(queue='expense-report',
                          auto_ack=True,
                          on_message_callback=callback)
    print(' [*] Waiting for JSON Object. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)