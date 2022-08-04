from __future__ import absolute_import

from checkout_sdk.common.common import Address
from checkout_sdk.common.enums import PaymentSourceType
from checkout_sdk.payments.payments import PaymentRequestSource


class RequestIdealSource(PaymentRequestSource):
    bic: str
    description: str
    language: str

    def __init__(self):
        super().__init__(PaymentSourceType.IDEAL)


class RequestSofortSource(PaymentRequestSource):

    def __init__(self):
        super().__init__(PaymentSourceType.SOFORT)


class RequestTamaraSource(PaymentRequestSource):
    billing_address: Address

    def __init__(self):
        super().__init__(PaymentSourceType.TAMARA)


class RequestPayPalSource(PaymentRequestSource):

    def __init__(self):
        super().__init__(PaymentSourceType.PAYPAL)


class PaymentRequestWeChatPaySource(PaymentRequestSource):
    billing_address: Address

    def __init__(self):
        super().__init__(PaymentSourceType.WECHATPAY)


class RequestAlipayPlusSource(PaymentRequestSource):

    def __init__(self, source_type: PaymentSourceType):
        super().__init__(source_type)

    @staticmethod
    def request_alipay_plus_cn_source():
        return RequestAlipayPlusSource(PaymentSourceType.ALIPAY_CN)

    @staticmethod
    def request_alipay_plus_gcash_source():
        return RequestAlipayPlusSource(PaymentSourceType.GCASH)

    @staticmethod
    def request_alipay_plus_dana_source():
        return RequestAlipayPlusSource(PaymentSourceType.DANA)

    @staticmethod
    def request_alipay_plus_kakao_pay_source():
        return RequestAlipayPlusSource(PaymentSourceType.KAKAOPAY)

    @staticmethod
    def request_alipay_plus_true_money_source():
        return RequestAlipayPlusSource(PaymentSourceType.TRUEMONEY)

    @staticmethod
    def request_alipay_plus_tng_source():
        return RequestAlipayPlusSource(PaymentSourceType.TNG)
