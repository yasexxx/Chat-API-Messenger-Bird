import json
from typing_extensions import final
import messagebird

class SMSClient:
    def __init__(self,api_key, id) -> None:
        super(SMSClient,self)
        self.client = messagebird.Client(api_key)
        self.id = id
        self.balance = self.client.balance()

    def get_balance(self):
        amount = self.balance.amount
        payment = self.balance.payment
        print(f'Your amount balanced: {amount} || Payment: {payment}')
        return amount, payment

    def create_message(self, originator, receipient, message: str, reference:str):
        try:
            message = self.client.message_create(
                originator=originator,recipients=receipient,
                body=message, params={ 'reference': reference}
            )
        except messagebird.client.ErrorException as e:
            print('An error occured while requesting a Message object:')
            for error in e.errors:
                print('  code        : %d' % error.code)
                print('  description : %s' % error.description)
                print('  parameter   : %s\n' % error.parameter)
        finally:
            return message

    def read_message(self,id):
        try:
            message = self.client.conversation_read_message(message_id=id)
        except messagebird.client.ErrorException as e:
            print('An error occured while requesting a Message object:')
            for error in e.errors:
                print('  code        : %d' % error.code)
                print('  description : %s' % error.description)
                print('  parameter   : %s\n' % error.parameter)
            message = None
        finally: return message

    def create_conversation_msg(self, conversation_id, channel_id, msg_type, msg_body ):
        try:
            msg = self.client.conversation_create_message(
                conversation_id,
                { 'channelId': channel_id, 
                    'type': msg_type,
                    'content': {'text': msg_body}
                })
        except messagebird.client.ErrorException as e:
            print('An error occured while requesting a Message object:')
            for error in e.errors:
                print('  code        : %d' % error.code)
                print('  description : %s' % error.description)
                print('  parameter   : %s\n' % error.parameter)
            msg = None
        finally:
            return msg
