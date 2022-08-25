from datetime import datetime
import pickle
from emojis import emojis_icons
from dateutil.parser import parse


# Import the required Libraries


def read_files_android(chat_file):
    with open(chat_file, encoding="utf-8") as chat:
        chat_text = chat.read()

    chat_text = chat_text.strip() + '\n .'
    list_of_chat = []
    new = 0
    for i in range(len(chat_text) - 2):
        if chat_text[i] == '\n' and (chat_text[i + 2] == '.' or chat_text[i + 3] == '.'):
            list_of_chat.append(chat_text[new: i + 1])
            new = i + 1

    if list_of_chat[0] == '\n':
        list_of_chat = list_of_chat[1:]
    if list_of_chat[-1] == '\n':
        list_of_chat = list_of_chat[:-1]

    # print(list_of_chat)
    return list_of_chat


def read_files_ios(chat_file):
    with open(chat_file, encoding="utf-8") as chat:
        chat_text = chat.read()

    chat_text = chat_text.strip() + '\n['
    list_of_chat = []
    new = 0
    chat_text = chat_text.replace("[","")
    chat_text = chat_text.replace("]","")
    print("---Chat Text---")
    print(chat_text)
    for i in range(len(chat_text) - 1):
        if chat_text[i] == '\n':
            list_of_chat.append(chat_text[new: i + 1])
            new = i + 1
    print(new)
    if list_of_chat[0] == '\n':
        list_of_chat = list_of_chat[1:]
    if list_of_chat[-1] == '\n':
        list_of_chat = list_of_chat[:-1]

    print(list_of_chat)
    return list_of_chat


def count_emoji_ios(chat_file, username=None, start_date=None, end_date=None):
    with open('all_emojies_list.pkl', 'rb') as f:
        text_emojis = pickle.load(f)
    all_emojis = text_emojis + emojis_icons()

    text = read_files_ios(chat_file)
    count_of_emojis = 0
    username_count = 0

    if start_date == '':
        start_date = datetime.strptime('31/03/1000', '%d/%m/%Y')
    else:
        start_date = parse(str(start_date))
        start_date = start_date.strftime('%d/%m/%Y')
        start_date = datetime.strptime(start_date, '%d/%m/%Y')
        # start_date = datetime.strptime(start_date, '%d/%m/%Y')

    if end_date == '':
        end_date = datetime.strptime('31/03/9999', '%d/%m/%Y')
    else:
        end_date = parse(str(start_date))
        end_date = end_date.strftime('%d/%m/%Y')
        end_date = datetime.strptime(end_date, '%d/%m/%Y')
        # end_date = datetime.strptime(end_date, '%d/%m/%Y')
    count = 0
    for message in text:
        message = message.replace('\u200e', '')
        index = message.find(',')
        split = message.split(',')
        # start = message.find('[')
        # end = message.find(']')
        # date = message[start + 1: end].replace(',', '')
        date = split[0]
        try:
            message_date = date
            message_date = parse(str(message_date))
            message_date = message_date.strftime('%d/%m/%Y')
            message_date = datetime.strptime(message_date, '%d/%m/%Y')
        except ValueError:
            pass
        if message_date.hour < 10:
            # print(message_date)
            username_end_index = 19 + message[19:].find(":")
            username_start_index = 19 + message[19:].find(" ")
            message_username = message[username_start_index: username_end_index]
        else:
            # print(message_date)
            username_index = 21 + message[18:].find(":")
            message_username = message[23: username_index]

        message_content = message[username_end_index + 1:]
        message_username = message_username.replace('\u202a', '')
        message_username = message_username.replace('\u202c', '')
        message_username = message_username.replace('\xa0', '')
        message_username = message_username.replace('‑', '-')
        message_username = message_username.strip()
        # print(username)
        # print(message_username)
        if username == '' or username.lower() == 'all':
            if (start_date <= message_date) and (end_date >= message_date):
                username_count += 1
                for emoji_ in all_emojis:
                    count_of_emojis += message_content.count(emoji_)
        elif (message_username == username) and (start_date <= message_date) and (end_date >= message_date):
            username_count += 1
            for emoji_ in all_emojis:
                count_of_emojis += message_content.count(emoji_)
            # for word in data:
            #         if any(char in emoji.UNICODE_EMOJI['en'] for char in word):
            #             count_of_emojis += 1
    return count_of_emojis, username_count


def count_emoji_android(chat_file, username=None, start_date=None, end_date=None):
    with open('all_emojies_list.pkl', 'rb') as f:
        text_emojis = pickle.load(f)
    all_emojis = text_emojis + emojis_icons()

    text = read_files_android(chat_file)
    count_of_emojis = 0
    username_count = 0

    if start_date == '':
        start_date = datetime.strptime('31/03/1000', '%d/%m/%Y')
    else:
        start_date = parse(str(start_date))
        start_date = start_date.strftime('%d/%m/%Y')
        start_date = datetime.strptime(start_date, '%d/%m/%Y')

    if end_date == '':
        end_date = datetime.strptime('31/03/9999', '%d/%m/%Y')
    else:
        end_date = parse(str(end_date))
        end_date = end_date.strftime('%d/%m/%Y')
        end_date = datetime.strptime(end_date, '%d/%m/%Y')
    count = 0
    for message in text:
        message = message.replace('\u200e', '')
        end = message.find('-') - 1
        date = message[0: end].replace(',', '')
        start_username = end + 3
        end_username = start_username + message[start_username:].find(":")

        try:
            message_date = date
            message_date = parse(str(message_date))
            message_date = message_date.strftime('%d/%m/%Y')
            message_date = datetime.strptime(message_date, '%d/%m/%Y')
        except ValueError:
            pass
        message_username = message[start_username: end_username]
        message_content = message[end_username + 2:]
        message_username = message_username.replace('\u202a', '')
        message_username = message_username.replace('\u202c', '')
        message_username = message_username.replace('\xa0', ' ')
        message_username = message_username.replace('‑', '-')
        if username == '' or username.lower() == 'all':
            if (start_date <= message_date) and (end_date >= message_date):
                username_count += 1
                for emoji_ in all_emojis:
                    count_of_emojis += message_content.count(emoji_)
        elif (message_username == username) and (start_date <= message_date) and (end_date >= message_date):
            username_count += 1
            for emoji_ in all_emojis:
                count_of_emojis += message_content.count(emoji_)
            # for word in data:
            #         if any(char in emoji.UNICODE_EMOJI['en'] for char in word):
            #             count_of_emojis += 1
    return count_of_emojis, username_count
