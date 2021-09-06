from __future__ import annotations

from typing import Union


class Pix(object):
    def __init__(
        self,
        pixkey: str,
        amount: float,
        *,
        merchant_name: str = '*',
        description: str = '',
        merchant_city: str = '*',
        country_code: str = "BR",
        txid: str = '*',
    ):
        """
        Define objects of type Pix.
        https://www.bcb.gov.br/content/estabilidadefinanceira/spb_docs/ManualBRCode.pdf
        """
        self._ID_PAYLOAD_FORMAT_INDICATOR = "00"
        self._ID_MERCHANT_ACCOUNT_INFORMATION = "26"
        self._ID_MERCHANT_ACCOUNT_INFORMATION_GUI = "00"
        self._ID_MERCHANT_ACCOUNT_INFORMATION_KEY = "01"
        self._ID_MERCHANT_ACCOUNT_INFORMATION_DESCRIPTION = "02"
        self._ID_MERCHANT_CATEGORY_CODE = "52"
        self._ID_TRANSACTION_CURRENCY = "53"
        self._ID_TRANSACTION_AMOUNT = "54"
        self._ID_COUNTRY_CODE = "58"
        self._ID_MERCHANT_NAME = "59"
        self._ID_MERCHANT_CITY = "60"
        self._ID_ADDITIONAL_DATA_FIELD_TEMPLATE = "62"
        self._ID_ADDITIONAL_DATA_FIELD_TEMPLATE_TXID = "05"
        self._ID_CRC16 = "63"

        self.pixkey = pixkey
        self.amount = amount

        self.description = self.to_string(description)
        self.merchant_name = self.to_string(merchant_name)
        self.merchant_city = self.to_string(merchant_city)
        self.txid = self.to_string(txid)
        self.country_code = "BR"

    @property
    def pixkey(self):
        return self._pixkey

    @pixkey.setter
    def pixkey(self, value):
        self._pixkey = self.to_string(value)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = "{:.2f}".format(float(self.to_string(value)))

    def _pix_factory(self):
        payload = "{}{}{}{}{}{}{}{}{}".format(
            self.get_value(self._ID_PAYLOAD_FORMAT_INDICATOR, "01"),
            self.get_merchant_account_information(),
            self.get_value(self._ID_MERCHANT_CATEGORY_CODE, "0000"),
            self.get_value(self._ID_TRANSACTION_CURRENCY, "986"),
            self.get_value(self._ID_TRANSACTION_AMOUNT, self.amount),
            self.get_value(self._ID_COUNTRY_CODE, self.country_code),
            self.get_value(self._ID_MERCHANT_NAME, self.merchant_name),
            self.get_value(self._ID_MERCHANT_CITY, self.merchant_city),
            self.get_additional_data_field_template(),
        )
        return "{}{}".format(payload, self.get_crc16(payload))

    def get_value(self, identify: str, value: str):
        """Concatenates the identifier and the value"""
        return "{}{}{}".format(identify, str(len(value)).zfill(2), value)

    def get_merchant_account_information(self):
        gui = self.get_value(
            self._ID_MERCHANT_ACCOUNT_INFORMATION_GUI, "br.gov.bcb.pix"
        )
        key = self.get_value(
            self._ID_MERCHANT_ACCOUNT_INFORMATION_KEY, self.pixkey)
        description = (
            self.get_value(
                self._ID_MERCHANT_ACCOUNT_INFORMATION_DESCRIPTION,
                self.description
            )
            if self.description
            else ""
        )

        return self.get_value(
            self._ID_MERCHANT_ACCOUNT_INFORMATION,
            "{}{}{}".format(gui, key, description),
        )

    def get_additional_data_field_template(self):
        txid = self.get_value(
            self._ID_ADDITIONAL_DATA_FIELD_TEMPLATE_TXID, self.txid)
        return self.get_value(self._ID_ADDITIONAL_DATA_FIELD_TEMPLATE, txid)

    def toHex(self, dec: float):
        digits = "0123456789ABCDEF"
        x = dec % 16
        rest = dec // 16
        if rest == 0:
            return digits[x]
        return self.toHex(rest) + digits[x]

    def get_crc16(self, payload: str):
        payload = "{}{}04".format(payload, self._ID_CRC16)
        crc = 0xFFFF
        for i in range(len(payload)):
            crc ^= ord(payload[i]) << 8
            for j in range(8):
                if (crc & 0x8000) > 0:
                    crc = (crc << 1) ^ 0x1021
                else:
                    crc = crc << 1
        return "{}{}{}".format(
            self._ID_CRC16, "04", self.toHex(crc & 0xFFFF).upper())

    #######################################################################

    def to_float(self, value):
        try:
            value = float(value)
        except Exception:
            TypeError(
                "Not able to convert {} to float type".format(
                    type(value)
                )
            )
        else:
            return value

    def to_string(self, value):
        try:
            value = str(value)
        except Exception:
            TypeError(
                "Not able to convert {} to string type".format(
                    type(value)
                )
            )
        else:
            return value

    def __add__(
            self,
            other: Union['Pix', list['Pix'], float, list[float]]) -> 'Pix':
        amount_parsed = self.to_float(self.amount)

        if not isinstance(other, list):
            other = list(other)

        if isinstance(other, list):
            for o in other:
                if hasattr(o, 'amount'):
                    amount_parsed += self.to_float(o.amount)
                else:
                    amount_parsed += self.to_float(o)

        self.amount = self.to_string(amount_parsed)
        return self

    def __sub__(
            self,
            other: Union['Pix', list['Pix'], float, list[float]]) -> 'Pix':
        amount_parsed = self.to_float(self.amount)

        if not isinstance(other, list):
            other = list(other)

        if isinstance(other, list):
            for o in other:
                if hasattr(o, 'amount'):
                    amount_parsed -= self.to_float(o.amount)
                else:
                    amount_parsed -= self.to_float(o)

        self.amount = self.to_string(amount_parsed)
        return self

    def __iadd__(self, other):
        return self.__add__(self, other)

    def __isub__(self, other):
        return self.__sub__(self, other)

    def __repr__(self):
        return self._pix_factory()
