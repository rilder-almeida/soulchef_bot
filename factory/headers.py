from tinysheet.fieldsheet import FieldSheet
from tinysheet.headersheet import HeaderSheet

keyboard_header = HeaderSheet('keyboard_header').add(
    FieldSheet('name').type(str).required(True),
    FieldSheet('header').type(list).default(list()),
    FieldSheet('body').type(list).default(list()),
    FieldSheet('footer').type(list).default(list()),
    FieldSheet('resize').type(bool).default(True),
    FieldSheet('once').type(bool).default(True),
)

message_header = HeaderSheet('message_header').add(
    # content_types=[
    #     'audio', 'photo', 'voice', 'video', 'document', 'text',
    #     'location', 'contact', 'sticker']
    FieldSheet('text').type(list).required(True),
    FieldSheet('content_type').type(str).default('text'),
    FieldSheet('reply_markup').nullable(True).default(None),
    FieldSheet('media').type(str).nullable(True).default(None),
    FieldSheet('latitude').type(float).nullable(True).default(None),
    FieldSheet('longitude').type(float).nullable(True).default(None),
)


plates_header = HeaderSheet('plates_header').add(
    FieldSheet('qtd').type(int).required(True),
    FieldSheet('value').type(int).required(True),
    FieldSheet('description').type(str).required(True)
)

menu_header = HeaderSheet('menu_header').add(
    FieldSheet('name').type(str).required(True),
    FieldSheet('plates').type(dict).required(True),
)

# class UserModel(BaseModel):
#     uid: int  # user_id ou from_id
#     cid: int  # chat_id ou peer_id
#
#     username: str = None  # nome de usuário
#     nickname: str = None  # apelido
#
#     phone: str = None  # NOTE: validar > phone_valid
#     cpf: str = None  # NOTE: validar > cpf_valid
#     email: str = None  # NOTE: validar > email_valid
#
#     location: AddressModel


user_header = HeaderSheet('user_header').add(
    FieldSheet('uid').type(int).required(True),
    FieldSheet('step').type(float).required(True),
    FieldSheet('name').type(str).required(False),
    FieldSheet('unknown').type(bool).required(False),

)

client_header = HeaderSheet('client_header')
