

# from typing import Any, Callable, Union
#
# from pydantic import BaseModel
#
# # TODO: create, read, update and delete
#
#
# class KeyboardModel(BaseModel):
#     format: list[str]  # formato do teclado [row:str]
#     row_width: int = 3
#
#     resize: bool = True  # redimensiona altura padrão do teclado
#     force_reply: bool = True  # obriga o user a responder
#     once: bool = True  # desaparece após o click
#     shufle: bool = False  # embaralhar?
#
#     filter_keyboard: Callable = None  # lambda k,v: v.startswith('A')
#
#     class Config:
#         orm_mode = True
#
#
# # outcoming / incoming
#
# class MessageModel(BaseModel):
#     text: list[str]  # mensagens do bot
#     reply_markup: KeyboardModel = None
#
#     media: dict[str:Any] = None  # files, images, pdf, location
#     pined: bool = False  # pinned?
#     schedule: int = None  # Agendado?
#
#     shufle: bool = False  # embaralhar?
#     sample_size: int = 0
#     # NOTE: diversificador de mensagens utils > sorted_sample_list
#     probability: float = 1  # aparece randomicamente
#     filter_message: Callable = None  # lambda k,v: v.startswith('A')
#
#     class Config:
#         orm_mode = True
#
#
# class StateModel(BaseModel):
#     name: str  # nome do state
#     id: int  # id do state [final 0]
#     messages: list[Union[MessageModel, list[MessageModel]]
#                    ] = None  # markups do state
#
#     # type content handles permitidos
#     permissions: list[Union[str, list[str]]] = None
#     conditions: dict['StateModel':bool] = None  # states exigidos
#
#     probability: float = 1  # aparece randomicamente
#     required: bool = True  # obrigatório?
#     done: bool = False  # concluído?
#
#     sub_states: dict[int:'StateModel'] = None  # states associados
#     filter_states: Callable = None  # lambda k,v: v.startswith('A')
#
#     class Config:  # representação da instância do modelo
#         orm_mode = True
#
#
# class AddressModel(BaseModel):
#     cep: str
#     bairro: str
#     cidade: str
#     logradouro: str
#     uf: str
#     complemento: str
#
#     lat: float
#     long: float
#
#
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
#     obj_user = None
#     obj_userfull = None
#
#     class Config:  # representação da instância do modelo
#         orm_mode = True
