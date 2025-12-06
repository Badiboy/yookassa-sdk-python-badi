## Работа со сделками

SDK позволяет создавать безопасные сделки, проводить по ним платежи и выплаты, а также получать о них информацию.

Объект сделки `DealResponse` содержит всю информацию о сделке, актуальную на текущий момент времени. Объект формируется при создании сделки и приходит в ответ на любой запрос, связанный со сделками.

* [Запрос на создание сделки](#Запрос-на-создание-сделки)
* [Запрос на создание сделки через билдер](#Запрос-на-создание-сделки-через-билдер)
* [Запрос на создание платежа с привязкой к сделке](#Запрос-на-создание-платежа-с-привязкой-к-сделке)
* [Запрос на выплату продавцу](#Запрос-на-выплату-продавцу)
* [Получить информацию о сделке](#Получить-информацию-о-сделке)
* [Получить список сделок с фильтрацией](#Получить-список-сделок-с-фильтрацией)

---

### Запрос на создание сделки <a name="Запрос-на-создание-сделки"></a>

[Создание сделки в документации](https://yookassa.ru/developers/api?lang=python#create_deal)

Чтобы создать сделку, необходимо создать объект сделки — `DealRequest`. Он позволяет создать сделку, в рамках которой 
необходимо принять оплату от покупателя и перечислить ее продавцу.

В ответ на запрос придет объект сделки - `DealResponse` в актуальном статусе.

```python
import var_dump as var_dump
from yookassa import Deal

res = Deal.create({
    "type": "safe_deal",
    "fee_moment": "payment_succeeded",
    "metadata": {
        "order_id": "88"
    },
    "description": "SAFE_DEAL PYTHON 123554642-2432FF344R"
})

var_dump.var_dump(res)
```
---

### Запрос на создание сделки через билдер <a name="Запрос-на-создание-сделки-через-билдер"></a>

[Создание сделки в документации](https://yookassa.ru/developers/api?lang=python#create_deal)

Билдер позволяет создать объект сделки — `DealRequest` программным способом, через объекты.

```python
import var_dump as var_dump
from yookassa import Deal
from yookassa.domain.models.deal import DealType, FeeMoment
from yookassa.domain.request import DealRequestBuilder

builder = DealRequestBuilder() \
    .set_type(DealType.SAFE_DEAL) \
    .set_fee_moment(FeeMoment.PAYMENT_SUCCEEDED) \
    .set_description('SAFE_DEAL 123554642-2432FF344R') \
    .set_metadata({'order_id': '37'})

request = builder.build()
# Можно что-то поменять, если нужно
request.description = 'SAFE_DEAL PYTHON 123554642-2432FF344R'
res = Deal.create(request)

var_dump.var_dump(res)
```
---

### Запрос на создание платежа с привязкой к сделке <a name="Запрос-на-создание-платежа-с-привязкой-к-сделке"></a>

[Создание платежа в документации](https://yookassa.ru/developers/api?lang=python#create_payment)

Чтобы принять оплату от покупателя, отправьте ЮKassa запрос на создание платежа, передайте в нём данные, которые нужны для оплаты, в зависимости от выбранного сценария интеграции, и следующие данные для проведения платежа в рамках сделки:
* Объект `amount` с общей суммой платежа за сделку (сумма вознаграждения продавца и вознаграждения вашей платформы). Эту сумму ЮKassa спишет с покупателя. Комиссия ЮKassa за проведение платежа рассчитывается из этой суммы, а взимается из вашего вознаграждения. Сумма платежа должна соответствовать ограничениям на минимальный и максимальный размер платежа. [Подробнее о лимитах платежей](https://yookassa.ru/docs/support/payments/limits)
* Объект `deal` с данными о сделке: идентификатор сделки и массив settlements с данными о том, какую сумму нужно выплатить продавцу. Разница между суммой платежа и суммой выплаты должна быть больше эквайринговой комиссии ЮKassa. Сумма выплаты должна соответствовать ограничениям на минимальный и максимальный размер выплаты. [Подробнее о лимитах выплат](https://yookassa.ru/developers/solutions-for-platforms/safe-deal/integration/payouts#specifics)

В ответ на запрос придет объект платежа — `PaymentResponse` — в актуальном статусе.

```python
import var_dump as var_dump
from yookassa import Payment

res = Payment.create({
    'amount': {
        'value': '200.00',
        'currency': 'RUB',
    },
    'confirmation': {
        'type': 'redirect',
        'locale': 'ru_RU',
        'return_url': 'https://testna5.ru/',
    },
    'description': 'Оплата заказа на сумму 100 руб',
    'metadata': {
        'order_id': '37'
    },
    'capture': True,
    'deal': {
        'id': 'dl-2909e77d-0022-5000-8000-0c37205b3208',
        'settlements': [
            {
                'type': 'payout',
                'amount': {
                    'value': '100.00',
                    'currency': 'RUB',
                },
            },
        ],
    },
    'merchant_customer_id': 'merchant@shop.com'
})

var_dump.var_dump(res)
```
[Подробнее о приеме оплаты от покупателя](https://yookassa.ru/developers/solutions-for-platforms/safe-deal/integration/payments)

---

### Запрос на выплату продавцу <a name="Запрос-на-выплату-продавцу"></a>

[Выплата продавцу в документации](https://yookassa.ru/developers/api?lang=python#create_payout)

Запрос позволяет перечислить продавцу оплату за выполненную услугу или проданный товар в рамках «Безопасной сделки». Выплату можно сделать на банковскую карту или в кошелек ЮMoney.

В ответ на запрос придет объект выплаты — `PayoutResponse` — в актуальном статусе.
```python
import var_dump as var_dump
from yookassa import Payout

res = Payout.create({
    'amount': {
        'value': '80.00',
        'currency': 'RUB',
    },
    'payout_destination_data': {
        'type': "yoo_money",
        'account_number': '4100116075156746',
    },
    'description': 'Выплата по заказу №37',
    'metadata': {
        'order_id': '37'
    },
    'deal': {
        'id': 'dl-2909e77d-0022-5000-8000-0c37205b3208',
    },
})

var_dump.var_dump(res)
```
[Подробнее о проведении выплат](https://yookassa.ru/developers/solutions-for-platforms/safe-deal/integration/payouts)

---

### Получить информацию о сделке <a name="Получить-информацию-о-сделке"></a>

[Информация о сделке в документации](https://yookassa.ru/developers/api?lang=python)

Запрос позволяет получить информацию о текущем состоянии сделки по его уникальному идентификатору.

В ответ на запрос придет объект сделки - `DealResponse` в актуальном статусе.

```python
import var_dump as var_dump
from yookassa import Deal

res = Deal.find_one('dl-285e5ee7-0022-5000-8000-01516a44b147')

var_dump.var_dump(res)
```
---

### Получить список сделок с фильтрацией <a name="Получить-список-сделок-с-фильтрацией"></a>

[Список сделок в документации](https://yookassa.ru/developers/api?lang=python#get_deals_list)

Запрос позволяет получить список сделок, отфильтрованный по заданным критериям.

В ответ на запрос вернется список сделок с учетом переданных параметров. В списке будет информация о сделках, 
созданных за последние 3 года. Список будет отсортирован по времени создания сделок в порядке убывания.

Если результатов больше, чем задано в `limit`, список будет выводиться фрагментами. В этом случае в ответе на запрос 
вернется фрагмент списка и параметр `next_cursor` с указателем на следующий фрагмент.

```python
import var_dump as var_dump
from yookassa import Deal

cursor = None
data = {
    "limit": 10,                                   # Ограничиваем размер выборки
    "status": "closed",                            # Выбираем только открытые сделки
    "full_text_search": "PYTHON",                  # Фильтр по описанию сделки — параметру description
    "created_at.gte": "2021-08-01T00:00:00.000Z",  # Созданы начиная с 2021-08-01
    "created_at.lt": "2021-11-20T00:00:00.000Z"    # И до 2021-11-20
}

while True:
    params = data
    if cursor:
        params['cursor'] = cursor
    try:
        res = Deal.list(params)
        print(" items: " + str(len(res.items)))    # Количество сделок в выборке
        print("cursor: " + str(res.next_cursor))   # Указательна следующую страницу
        var_dump.var_dump(res)

        if not res.next_cursor:
            break
        else:
            cursor = res.next_cursor
    except Exception as e:
        print(" Error: " + str(e))
        break

```
[Подробнее о работе со списками](https://yookassa.ru/developers/using-api/lists)
