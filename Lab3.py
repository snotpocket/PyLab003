from lab_chat import join_group


def get_username():
   username = input("Enter your username: ")
   return username.strip().upper()
def get_group():
    group = input("Enter group name: ")
    return group.strip().upper()
def get_message():
    message = input("Enter message: ")
    return message.strip()

import lab_chat as lc

def initialize_chat():
    user_name = get_username()
    group_name = get_group()
    node = lc.get_peer_node(user_name)
    lc.join_group(node, group_name)
    return lc.get_channel(node, group_name)

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")
start_chat()