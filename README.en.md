# YooKassa API Python Client Library

[![Build Status](https://travis-ci.org/yoomoney/yookassa-sdk-python.svg?branch=master)](https://travis-ci.org/yoomoney/yookassa-sdk-python)
[![Latest Stable Version](https://img.shields.io/pypi/v/yookassa.svg)](https://pypi.org/project/yookassa/)
[![Total Downloads](https://img.shields.io/pypi/dm/yookassa.svg)](https://pypi.org/project/yookassa/)
[![License](https://img.shields.io/pypi/l/yookassa.svg)](https://git.yoomoney.ru/projects/SDK/repos/yookassa-sdk-python)

[Russian](README.md) | English

This product is used for managing payments under [The YooKassa API](https://yookassa.ru/en/developers/api)
For usage by those who implemented YooKassa using the API method.

## Features

* Version 3.x supports Python >=3.7. To work on earlier versions of Python, use versions of yookassa 2.x
* Changing the directory/file structure affected some package imports. When switching from the version of yookassa 2.x, check the imports in your project:
  * `yookassa.domain.models.airline` → `yookassa.domain.models.payment_data.request.airline`
  * `yookassa.domain.models.authorization_details` → `yookassa.domain.models.payment_data.response.authorization_details`
  * `yookassa.domain.models.receipt_customer` → `yookassa.domain.models.receipt_data.receipt_customer`
  * `yookassa.domain.models.receipt_item` → `yookassa.domain.models.receipt_data.receipt_item`
  * `yookassa.domain.models.receipt_item_supplier` → `yookassa.domain.models.receipt_data.receipt_item_supplier`
  * `yookassa.domain.models.recipient` → `yookassa.domain.models.payment_data.recipient`
  * `yookassa.domain.models.refund_source` → `yookassa.domain.models.refund_data.refund_source`
* `Settings.get_account_settings()` now returns the `Me` object. To support compatibility, object fields can be accessed as an array - `me.account_id = me['account_id']`
* The `me.fiscalization_enabled` field is deprecated, but it is still supported. The `me.fiscalization` object has been added instead..

## Requirements
1. Python >=3.7
2. pip

## Installation
### Under console using pip

1. Install pip.
2. In the console, run the following command:
```bash
pip install --upgrade yookassa
```

### Under console using easy_install
1. Install easy_install.
2. In the console, run the following command:
```bash
easy_install --upgrade yookassa
```

## Commencing work

1. Import module
```python
import yookassa
```

2. Configure a Client
```python
from yookassa import Configuration

Configuration.configure('<Account Id>', '<Secret Key>')
```

or

```python
from yookassa import Configuration

Configuration.account_id = '<Account Id>'
Configuration.secret_key = '<Secret Key>'
```

or via oauth

```python
from yookassa import Configuration

Configuration.configure_auth_token('<Oauth Token>')
```

If you agree to participate in the development of the SDK, you can submit data about your framework, cms or module:

```python
from yookassa import Configuration
from yookassa.domain.common.user_agent import Version

Configuration.configure('<Account Id>', '<Secret Key>')
Configuration.configure_user_agent(
    framework=Version('Django', '2.2.3'),
    cms=Version('Wagtail', '2.6.2'),
    module=Version('Y.CMS', '0.0.1')
)
```

3. Call the required API method. [More details in our documentation for the YooKassa API](https://yookassa.ru/en/developers/api)

## Examples of using the API SDK

#### [YooKassa SDK Settings](./docs/examples/01-configuration.md)
* [Authentication](./docs/examples/01-configuration.md#Аутентификация)
* [Statistics about the environment used](./docs/examples/01-configuration.md#Статистические-данные-об-используемом-окружении)
* [Getting information about the store](./docs/examples/01-configuration.md#Получение-информации-о-магазине)
* [Working with Webhook](./docs/examples/01-configuration.md#Работа-с-Webhook)
* [Notifications](./docs/examples/01-configuration.md#Входящие-уведомления)

#### [Working with payments](./docs/examples/02-payments.md)
* [Request to create a payment](./docs/examples/02-payments.md#Запрос-на-создание-платежа)
* [Request to create a payment via the builder](./docs/examples/02-payments.md#Запрос-на-создание-платежа-через-билдер)
* [Request for partial payment confirmation](./docs/examples/02-payments.md#Запрос-на-частичное-подтверждение-платежа)
* [Request to cancel an incomplete payment](./docs/examples/02-payments.md#Запрос-на-отмену-незавершенного-платежа)
* [Get payment information](./docs/examples/02-payments.md#Получить-информацию-о-платеже)
* [Get a list of payments with filtering](./docs/examples/02-payments.md#Получить-список-платежей-с-фильтрацией)

#### [Working with refunds](./docs/examples/03-refunds.md)
* [Request to create a refund](./docs/examples/03-refunds.md#Запрос-на-создание-возврата)
* [Request to create a refund via the builder](./docs/examples/03-refunds.md#Запрос-на-создание-возврата-через-билдер)
* [Get refund information](./docs/examples/03-refunds.md#Получить-информацию-о-возврате)
* [Get a list of returns with filtering](./docs/examples/03-refunds.md#Получить-список-возвратов-с-фильтрацией)

#### [Working with receipts](./docs/examples/04-receipts.md)
* [Request to create a receipt](./docs/examples/04-receipts.md#Запрос-на-создание-чека)
* [Request to create a receipt via the builder](./docs/examples/04-receipts.md#Запрос-на-создание-чека-через-билдер)
* [Get information about the receipt](./docs/examples/04-receipts.md#Получить-информацию-о-чеке)
* [Get a list of receipts with filtering](./docs/examples/04-receipts.md#Получить-список-чеков-с-фильтрацией)

#### [Working with safe deals](./docs/examples/05-deals.md)
* [Request to create a deal](./docs/examples/05-deals.md#Запрос-на-создание-сделки)
* [Request to create a deal via the builder](./docs/examples/05-deals.md#Запрос-на-создание-сделки-через-билдер)
* [Request to create a payment with info about deal](./docs/examples/05-deals.md#Запрос-на-создание-платежа-с-привязкой-к-сделке)
* [Get deal information](./docs/examples/05-deals.md#Получить-информацию-о-сделке)
* [Get a list of deals with filtering](./docs/examples/05-deals.md#Получить-список-сделок-с-фильтрацией)

#### [Working with payouts](./docs/examples/06-payouts.md)
* [Request to create a payout](./docs/examples/06-payouts.md#Запрос-на-выплату-продавцу)
  * [Payouts to bank card](./docs/examples/06-payouts.md#Проведение-выплаты-на-банковскую-карту)
  * [Payouts to YooMoney wallets](./docs/examples/06-payouts.md#Проведение-выплаты-в-кошелек-юmoney)
  * [Payouts via Fast Payment Service](./docs/examples/06-payouts.md#Проведение-выплаты-через-сбп)
  * [Payouts to self-employed](./docs/examples/06-payouts.md#Выплаты-самозанятым)
  * [Payouts by safe deal](./docs/examples/06-payouts.md#Проведение-выплаты-по-безопасной-сделке)
* [Get payout information](./docs/examples/06-payouts.md#Получить-информацию-о-выплате)

#### [Working with self-employed](./docs/examples/07-self-employed.md)
* [Creation of self-employed](./docs/examples/07-self-employed.md#Запрос-на-создание-самозанятого)
* [Get information about self-employed](./docs/examples/07-self-employed.md#Получить-информацию-о-самозанятом)

#### [Working with personal data](./docs/examples/08-personal-data.md)
* [Creation of personal data](./docs/examples/08-personal-data.md#Создание-персональных-данных)
* [Get information about personal data](./docs/examples/08-personal-data.md#Получить-информацию-о-персональных-данных)

#### [Working with the list of Fast Payment Service participants](./docs/examples/09-sbp-banks.md)
* [Get a list of Fast Payment Service participants](./docs/examples/09-sbp-banks.md#Получить-список-участников-СБП)

#### [Working with invoices](./docs/examples/10-invoices.md)
* [Request to create an invoice](./docs/examples/10-invoices.md#Запрос-на-создание-счета)
* [Request to create an invoice via the builder](./docs/examples/10-invoices.md#Запрос-на-создание-счета-через-билдер)
* [Get information about the invoice](./docs/examples/10-invoices.md#Получить-информацию-о-счете)

#### [Working with payment methods](./docs/examples/11-payment-methods.md)
* [Request to create payment method](./docs/examples/11-payment-methods.md#Запрос-на-создание-способа-оплаты)
* [Request to create payment method via the builder](./docs/examples/11-payment-methods.md#Запрос-на-создание-способа-оплаты-через-билдер)
* [Get information about the payment method](./docs/examples/11-payment-methods.md#Получить-информацию-о-способе-оплаты)
