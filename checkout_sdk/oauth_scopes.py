from __future__ import absolute_import

from enum import Enum


class OAuthScopes(str, Enum):
    VAULT = 'vault'
    VAULT_INSTRUMENTS = 'vault:instruments'
    VAULT_TOKENIZATION = 'vault:tokenization'
    GATEWAY = 'gateway'
    GATEWAY_PAYMENT = 'gateway:payment'
    GATEWAY_PAYMENT_DETAILS = 'gateway:payment-details'
    GATEWAY_PAYMENT_AUTHORIZATION = 'gateway:payment-authorizations'
    GATEWAY_PAYMENT_VOIDS = 'gateway:payment-voids'
    GATEWAY_PAYMENT_CAPTURES = 'gateway:payment-captures'
    GATEWAY_PAYMENT_REFUNDS = 'gateway:payment-refunds'
    FX = 'fx'
    PAYOUTS_BANK_DETAILS = 'payouts:bank-details'
    SESSIONS_APP = 'sessions:app'
    SESSIONS_BROWSER = 'sessions:browser'
    DISPUTES = 'disputes'
    DISPUTES_VIEW = 'disputes:view'
    DISPUTES_PROVIDE_EVIDENCE = 'disputes:provide-evidence'
    DISPUTES_ACCEPT = 'disputes:accept'
    MARKETPLACE = 'marketplace'
    ACCOUNTS = 'accounts'
    FLOW = 'flow'
    FLOW_WORKFLOWS = 'flow:workflows'
    FLOW_EVENTS = 'flow:events'
    FILES = 'files'
    FILES_RETRIEVE = 'files:retrieve'
    FILES_UPLOAD = 'files:upload'
    FILES_DOWNLOAD = 'files:download'
    TRANSFERS = 'transfers'
    TRANSFERS_CREATE = 'transfers:create'
    TRANSFERS_VIEW = 'transfers:view'
    BALANCES = 'balances'
    BALANCES_VIEW = 'balances:view'

    MIDDLEWARE = 'middleware'
    MIDDLEWARE_MERCHANTS_SECRET = 'middleware:merchants-secret'
    MIDDLEWARE_MERCHANTS_PUBLIC = 'middleware:merchants-public'
