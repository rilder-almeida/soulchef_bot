def message_factory(message: dict, **kwargs):
    msg_args = {}
    if message['content_type'] == 'text':
        msg_args.update({
            'text': message['text'],
            'reply_markup': message['reply_markup'],
        })
    elif message['content_type'] == 'photo':
        msg_args.update({
            'photo': message['media'],
            'caption': message['text'],
            'reply_markup': message['reply_markup'],
        })
    elif message['content_type'] in ['video', 'document']:
        msg_args.update({
            'data': message['media'],
            'caption': message['text'],
            'reply_markup': message['reply_markup'],
        })
    elif message['content_type'] == 'location':
        msg_args.update({
            'latitude': message['latitude'],
            'longitude': message['longitude'],
            'reply_markup': message['reply_markup'],
        })
    else:
        raise Exception('No supported content_type {}'.format(
            message['content_type']))

    msg_args.update({
        'parse_mode': None,
        'disable_notification': None,
        'timeout': None,
        **kwargs,
    })

    return msg_args
