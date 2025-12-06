## Работа с выплатами

Выплата — это сумма денег, которую вы переводите физическому лицу или самозанятому. С помощью API вы можете создать выплату и получить о ней актуальную информацию.

Выплаты используются в следующих платежных решениях ЮKassa:

* Выплаты — вы как компания переводите деньги физическим лицам и самозанятым (например, выплачиваете кэшбэк пользователям).
* Безопасная сделка — ваша платформа в рамках созданной сделки переводит оплату от одного физического лица другому.

SDK позволяет проводить выплаты, а также получать информацию о них.

Объект выплаты `PayoutResponse` содержит всю информацию о выплате, актуальную на текущий момент времени. Объект формируется при создании выплаты и приходит в ответ на любой запрос, связанный с выплатами.

Набор возвращаемых параметров зависит от статуса объекта (значение параметра status) и того, какие параметры вы передали в запросе на создание выплаты.

* [Запрос на выплату продавцу](#Запрос-на-выплату-продавцу)
  * [Проведение выплаты на банковскую карту](#Проведение-выплаты-на-банковскую-карту)
  * [Проведение выплаты в кошелек ЮMoney](#Проведение-выплаты-в-кошелек-юmoney)
  * [Проведение выплаты через СБП](#Проведение-выплаты-через-сбп)
  * [Выплаты самозанятым](#Выплаты-самозанятым)
  * [Проведение выплаты по безопасной сделке](#Проведение-выплаты-по-безопасной-сделке)
* [Запрос на создание выплаты через билдер](#Запрос-на-создание-выплаты-через-билдер)
* [Получить информацию о выплате](#Получить-информацию-о-выплате)

---

### Запрос на выплату продавцу <a name="Запрос-на-выплату-продавцу"></a>

[Выплата продавцу в документации](https://yookassa.ru/developers/api?lang=php#create_payout)

Запрос позволяет перечислить продавцу оплату за выполненную услугу или проданный товар в рамках «Безопасной сделки». Выплату можно сделать на банковскую карту или в кошелек ЮMoney.

В ответ на запрос придет объект выплаты — `PayoutResponse` — в актуальном статусе.

[Подробнее о проведении выплат](https://yookassa.ru/developers/solutions-for-platforms/safe-deal/integration/payouts)

#### Проведение выплаты на банковскую карту <a name="Проведение-выплаты-на-банковскую-карту"></a>

```python
import uuid
import var_dump as var_dump
from yookassa import Payout
from yookassa.domain.models.currency import Currency

idempotency_key = uuid.uuid4()
res = Payout.create({
    'amount': {
        'value': '280.00',
        'currency': Currency.RUB,
    },
    'payout_destination_data': {
        'type': 'bank_card',
        'card': {
            'number': '5555555555554477',
        },
    },
    'description': 'Выплата по заказу №37',
    'metadata': {
        'order_id': '37',
    },
}, idempotency_key)

var_dump.var_dump(res)
```

#### Проведение выплаты в кошелек ЮMoney <a name="Проведение-выплаты-в-кошелек-юmoney"></a>

```python
import var_dump as var_dump
from yookassa import Payout
from yookassa.domain.models.currency import Currency

res = Payout.create({
    'amount': {
        'value': '280.00',
        'currency': Currency.RUB,
    },
    'payout_destination_data': {
        'type': 'yoo_money',
        'account_number': '4100116075156746',
    },
    'description': 'Выплата по заказу №37',
    'metadata': {
        'order_id': '37',
    },
})

var_dump.var_dump(res)
```

#### Проведение выплаты через СБП <a name="Проведение-выплаты-через-сбп"></a>

```python
import var_dump as var_dump
from yookassa import Payout
from yookassa.domain.models.currency import Currency

res = Payout.create({
    'amount': {
        'value': '280.00',
        'currency': Currency.RUB,
    },
    'payout_destination_data': {
        'type': 'sbp',
        'phone': '79000000000',
        'bank_id': '100000000111',
    },
    'description': 'Выплата по заказу №37',
    'metadata': {
        'order_id': '37',
    },
})

var_dump.var_dump(res)
```

#### Выплаты самозанятым <a name="Выплаты-самозанятым"></a>

```python
import var_dump as var_dump
from yookassa import Payout
from yookassa.domain.models.currency import Currency

res = Payout.create({
    'amount': {
        'value': '280.00',
        'currency': Currency.RUB,
    },
    'payout_token': '<Синоним банковской карты>',
    'self_employed': {
        'id': 'se-d6b9b3fa-0cb8-4aa8-b3c0-254bf0358d4c',
    },
    'receipt_data': {
        'service_name': 'Доставка документов'
    },
    'description': 'Выплата по заказу №37',
    'metadata': {
        'order_id': '37',
        'courier_id': '001',
    },
})

var_dump.var_dump(res)
```

#### Проведение выплаты по безопасной сделке <a name="Проведение-выплаты-по-безопасной-сделке"></a>

```python
import var_dump as var_dump
from yookassa import Payout
from yookassa.domain.models.currency import Currency

res = Payout.create({
    "amount": {"value": 800.0, "currency": Currency.RUB},
    "payout_token": '<Синоним банковской карты>',
    "description": "Выплата по заказу №37",
    "metadata": {
        "order_id": "37"
    },
    "deal": {
        "id": "dl-285e5ee7-0022-5000-8000-01516a44b147"
    }
})

var_dump.var_dump(res)
```
---

### Запрос на создание выплаты через билдер <a name="Запрос-на-создание-выплаты-через-билдер"></a>

[Создание выплаты в документации](https://yookassa.ru/developers/api?lang=python#create_payout)

Билдер позволяет создать объект выплаты — `PayoutRequest` программным способом, через объекты.

```python
import var_dump as var_dump
from yookassa import Payout
from yookassa.domain.models.currency import Currency
from yookassa.domain.request import PayoutRequestBuilder

builder = PayoutRequestBuilder()
builder.set_amount({'value': 800.0, 'currency': Currency.RUB}) \
    .set_description('Выплата по заказу №77') \
    .set_payout_token('<Синоним банковской карты>') \
    .set_metadata({'order_id': '77'}) \
    .set_deal({
        'id': 'dl-285e5ee7-0022-5000-8000-01516a44b147'
    })
    
request = builder.build()
# Можно что-то поменять, если нужно
request.description = 'Выплата по заказу №77'
res = Payout.create(request)

var_dump.var_dump(res)
```
---

### Получить информацию о выплате <a name="Получить-информацию-о-выплате"></a>

[Информация о выплате в документации](https://yookassa.ru/developers/api?lang=php#get_payout)

Запрос позволяет получить информацию о текущем состоянии выплаты по ее уникальному идентификатору.

[Данные для аутентификации запросов](https://yookassa.ru/developers/using-api/interaction-format#auth) зависят от того, какое платежное решение вы используете — [обычные выплаты](https://yookassa.ru/developers/payouts/overview) или выплаты в рамках «[Безопасной сделки](https://yookassa.ru/developers/solutions-for-platforms/safe-deal/basics)».

В ответ на запрос придет объект выплаты — `PayoutResponse` — в актуальном статусе.

```python
import var_dump as var_dump
from yookassa import Payout

res = Payout.find_one('po-21b23b5b-000f-5061-a000-0674e49a8c10')

var_dump.var_dump(res)
```
