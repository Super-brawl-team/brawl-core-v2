# FindMessage.py

from Admins.Converter.Messaging.Client.ClientHelloMessage import ClientHelloMessage

find_messages = {
    10100: ClientHelloMessage
}

class FindMessage:
    def convert(m_type):
        if m_type in find_messages:
            return find_messages[m_type]()
        return None