import re

from pycep_correios import WebService, exceptions, get_address_from_cep


def consulta_cep(cep: str) -> dict:

    address = {}

    if bool(re.match("^[0-9]{5}\-?[0-9]{3}$", cep)):  # noqa
        try:
            address = (
                get_address_from_cep(cep, webservice=WebService.APICEP)
                or get_address_from_cep(cep, webservice=WebService.VIACEP)
                or get_address_from_cep(cep, webservice=WebService.CORREIOS)
            )

        except exceptions.InvalidCEP as eic:
            print(eic)

        except exceptions.CEPNotFound as ecnf:
            print(ecnf)

        except exceptions.ConnectionError as errc:
            print(errc)

        except exceptions.Timeout as errt:
            print(errt)

        except exceptions.HTTPError as errh:
            print(errh)

        except exceptions.BaseException as e:
            print(e)

    return address
