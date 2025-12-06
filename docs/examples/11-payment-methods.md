## Работа со способами оплаты

> Только для тех, кто использует [привязку на нулевую сумму](https://yookassa.ru/developers/payment-acceptance/scenario-extensions/recurring-payments/save-payment-method/save-without-payment) для сохранения банковских карт.

Способ оплаты — данные платежного средства пользователя. Например, данные банковской карты.

С помощью SDK вы можете создать способ оплаты — сохранить платежные данные в ЮKassa с привязкой к вашему магазину. Также через SDK вы можете получить актуальную информацию о созданном способе оплаты.

* [Запрос на создание способа оплаты](#Запрос-на-создание-способа-оплаты)
* [Запрос на создание способа оплаты через билдер](#Запрос-на-создание-способа-оплаты-через-билдер)
* [Получить информацию о способе оплаты](#Получить-информацию-о-способе-оплаты)

### Запрос на создание способа оплаты <a name="Запрос-на-создание-способа-оплаты"></a>

[Создание способа оплаты в документации](https://yookassa.ru/developers/api#create_payment_method)

Объект способа оплаты `PaymentMethod` содержит всю информацию о платежном средстве пользователя, актуальную на текущий момент времени. Он формируется при создании способа оплаты и приходит в ответ на любой запрос, связанный со способами оплаты.

Набор возвращаемых параметров зависит от статуса объекта (значение параметра `status`) и того, какие параметры вы передали в запросе на создание способа оплаты.

В ответ на запрос придет объект способа оплаты - `PaymentMethod` в актуальном статусе.

```python
import var_dump as var_dump
from yookassa import PaymentMethod

res = PaymentMethod.create({
    "type": "bank_card",
    "id": "22d6d597-000f-5000-9000-145f6df21d6f",
    "saved": False,
    "holder": {
        "gateway_id": "100700"
    },
    "confirmation": {
        "type": "redirect",
        "confirmation_url": "https://merchant-site.ru/return_url"
    }
})

var_dump.var_dump(res)
```
---

### Запрос на создание способа оплаты через билдер <a name="Запрос-на-создание-способа-оплаты-через-билдер"></a>

[Создание способа оплаты в документации](https://yookassa.ru/developers/api#create_payment_method)

Билдер позволяет создать объект способа оплаты — `PaymentMethod` программным способом, через объекты.

```python
import var_dump as var_dump
from yookassa import PaymentMethod
from yookassa.domain.request import PaymentMethodRequestBuilder
from yookassa.domain.common import ConfirmationType, PaymentMethodType

payment_method = PaymentMethodRequestBuilder()
payment_method.set_type(PaymentMethodType.BANK_CARD) \
    .set_client_ip('1.2.3.4') \
    .set_confirmation({
        "type": ConfirmationType.REDIRECT, 
        "return_url": "https://merchant-site.ru/return_url"
    }) \
    .set_holder({'gateway_id': '77780044'})

request = payment_method.build()
# Можно что-то поменять, если нужно
request.client_ip = "127.0.0.1"

res = PaymentMethod.create(request)

var_dump.var_dump(res)
```
---

### Получить информацию о способе оплаты <a name="Получить-информацию-о-способе-оплаты"></a>

[Информация о способе оплаты в документации](https://yookassa.ru/developers/api#get_payment_method)

Запрос позволяет получить информацию о текущем состоянии способа оплаты по его уникальному идентификатору.

В ответ на запрос придет объект способа оплаты — `PaymentMethodResponse` — в актуальном статусе.

```python
import var_dump as var_dump
from yookassa import PaymentMethod

paymentMethod = PaymentMethod.find_one('3006bf62-0037-5000-8000-091792232ce7')

var_dump.var_dump(paymentMethod)
```
