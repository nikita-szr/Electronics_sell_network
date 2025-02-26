# Electronics sell network
Сервис, сети по продаже электроники

## Использование c помощью **Docker**
* В виртуальном окружении загрузите зависимости:
  
```sh
$ pip install -r requirements.txt
```

* Добавьте файл **.env** (по примеру **.env.sample**)
* Запустите терминал и выполните команду:

```sh
$ docker-compose up -d --build
```

## Разработка

Реализовано приложение:
`network` - API представление 

### network:

Модель **NetworkNode**:

* *name* - Название
* *email* - Почта
* *country* - Страна
* *city*  - Город
* *street* - Улица
* house_number* - Номер дома
* supplier* - Поставщик
* debt* - Задолженность
* created_at* - Время создания

Модель **Product**:

* *network_node*
* *name* - Название
* *model* - Модель
* *release_date*  - Дата релиза


#### Контроллеры:

* CRUD для модели поставщика

