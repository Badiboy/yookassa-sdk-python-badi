## Работа со счетами

С помощью SDK можно выставлять счета на оплату. Счет — это страница ЮKassa, на которой пользователь увидит описание заказа и сможет заплатить в любой удобный момент в течение заданного вами срока. [Выставление счетов](https://yookassa.ru/developers/payment-acceptance/scenario-extensions/invoices/basics)

* [Запрос на создание счета](#Запрос-на-создание-счета)
* [Запрос на создание счета через билдер](#Запрос-на-создание-счета-через-билдер)
* [Получить информацию о счете](#Получить-информацию-о-счете)

---

### Запрос на создание счета <a name="Запрос-на-создание-счета"></a>

[Создание счета в документации](https://yookassa.ru/developers/api?codeLang=php#create_invoice)

Используйте этот запрос, чтобы создать в ЮKassa [объект счета](https://yookassa.ru/developers/api?codeLang=bash#invoice_object). В запросе необходимо передать данные о заказе, которые отобразятся на странице счета, и данные для проведения платежа.

В ответ на запрос придет объект счета — `InvoiceResponse` — в актуальном статусе.

```python
import uuid
import var_dump as var_dump
from yookassa import Invoice

idempotence_key = str(uuid.uuid4())
invoice = Invoice.create({
    "payment_data": {
        "amount": {
            "value": "10.00",
            "currency": "RUB"
        },
        "capture": True,
        "description": "Заказ №137",
        "metadata": {
            "order_id": "137"
        }
    },
    "cart": [
        {
            "description": "Товар арт. 12345",
            "price": {
                "value": "9.00",
                "currency": "RUB"
            },
            "discount_price": {
                "value": "7.00",
                "currency": "RUB"
            },
            "quantity": 1.000
        },
        {
            "description": "Товар арт. 67890",
            "price": {
                "value": "1.00",
                "currency": "RUB"
            },
            "quantity": 3.000
        }
    ],
    "delivery_method_data": {
        "type": "self"
    },
    "locale": "ru_RU",
    "expires_at": "2024-11-18T10:51:18.139Z",
    "description": "Счет на оплату заказа номер 137",
    "metadata": {
        "order_id": "137"
    }
}, idempotence_key)

var_dump.var_dump(dict(invoice))
```

---

### Запрос на создание счета через билдер <a name="Запрос-на-создание-счета-через-билдер"></a>

[Информация о создании счета в документации](https://yookassa.ru/developers/api?codeLang=php#create_invoice)

Билдер позволяет создать объект счета — `CreateInvoiceRequest` — программным способом, через объекты.

```python
import uuid
import var_dump as var_dump
from yookassa import Invoice
from yookassa.domain.models.invoice_data.request.delivery_method_self import DeliveryMethodSelf
from yookassa.domain.request import InvoiceRequestBuilder

idempotence_key = str(uuid.uuid4())
builder = InvoiceRequestBuilder()
builder.set_payment_data({
        "amount": {
            "value": "10.00",
            "currency": "RUB"
        },
        "capture": True,
        "description": "Заказ №137",
        "metadata": {
            "order_id": "137"
        }
    }) \
    .set_cart([
        {
            "description": "Товар арт. 12345",
            "price": {
                "value": "9.00",
                "currency": "RUB"
            },
            "discount_price": {
                "value": "7.00",
                "currency": "RUB"
            },
            "quantity": 1.000
        },
        {
            "description": "Товар арт. 67890",
            "price": {
                "value": "1.00",
                "currency": "RUB"
            },
            "quantity": 3.000
        }
    ]) \
    .set_delivery_method_data(DeliveryMethodSelf()) \
    .set_locale("ru_RU") \
    .set_expires_at("2024-11-18T10:51:18.139Z") \
    .set_description("Заказ №137") \
    .set_metadata({"order_id": "137"}) \

request = builder.build()
# Можно что-то поменять, если нужно
request.description = "Счет на оплату заказа номер 137"
res = Invoice.create(request)

var_dump.var_dump(dict(res))
```

---

### Получить информацию о счете <a name="Получить-информацию-о-счете"></a>

[Информация о счете в документации](https://yookassa.ru/developers/api?codeLang=php#get_invoice)

Запрос позволяет получить информацию о текущем состоянии счета по его уникальному идентификатору.

В ответ на запрос придет объект счета — `InvoiceResponse` — в актуальном статусе.

```python
import var_dump as var_dump
from yookassa import Invoice
from yookassa import Payment

invoiceId = "in-2eab0a2f-0000-0050-e893-63eee8efee81"
invoice = Invoice.find_one(invoiceId)
var_dump.var_dump(dict(invoice))
if invoice.payment_details is not None:
    payment = Payment.find_one(invoice.payment_details.id)
    var_dump.var_dump(dict(payment))
```
