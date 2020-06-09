# Дипломный проект по курсу «Django: создание функциональных веб-приложений»

Разработать сайт интернет-магазина.
Должна быть реализована клиентская часть сервиса и интерфейс администрирования.


## Описание клиентской части

Просмотр товара и добавление в корзину (рядом с каждым товаром должна быть кнопка добавления в корзину).

* Главная страница со статьями о подборке товаров (отсортированы по дате создания статьи)
  и перечислением этих товаров.
* Страница категории товара со списком товаров с пагинацией.
* Страница товара с подробным описанием.
    
Меню:

* Ссылка на главную страницу.
* Ссылки на разделы (разделы могут иметь иерархию).
* Ссылка на корзину.
* Кнопка входа/выхода в зависимости от статуса авторизации.

Корзина со списком выбранных товаров, привязанных к пользователю.
Кнопка заказа должна создавать заказ и очищать корзину.

Для входа использовать аутентификацию по email'у.


## Интерфейс администратора

* Редактирование разделов.
* Редактирование товаров.
* Редактирование статей на главной странице и привязывание к ним товаров,
  которые должны отображаться после нее.
* Просмотр списка заказов пользователей, отсортированных по дате создания,
    с указанием пользователя и количества товаров.
* Страница детализации заказа с просмотром списка заказанных товаров.

## Дизайн

* [Главная страница](templates/shop/index.html).
* [Страница раздела](templates/shop/categorys.html).
* [Страница незаполненного раздела](templates/shop/empty_section.html).
* [Страница товара](templates/shop/product.html).
* [Страница корзины](templates/shop/cart.html).
* [Страница входа](templates/shop/login.html).

## Требования к организации системы

* Система должна быть реализована на Django версии 2.
* Интерфейс администратора должен быть создан стандартными средствами Django admin.
* В качестве СУБД использовать sqlite.
* Система при работе не должна вызывать исключений и ошибок.

## Что необходимо предоставить по проекту

* Миграции для создания базы данных.
* Инструкции по установке и первому запуску. Файл `README.md` в папке проекта.
* Дамп данных с тестовым наполнением `fixtures.json`,
  с тестовым суперпользователем с именем `admin` и паролем `admin` (команда `manage.py dumpdata` для создания дампа).

## Дополнительные задачи

* Реализовать механизм анонимных отзывов как показано на макете [Страница товара](templates/shop/product.html).
* Реализовать возможность регистрации по почте (без подтверждения почты).

---
Способы предоставить код дипломной работы -
исходный код на [BitBucket](https://bitbucket.org/) или [GitHub](https://github.com/).


### Как правильно задавать вопросы дипломному руководителю?

**Что следует делать, чтобы все получилось:**

* Попробовать найти ответ сначала самому в интернете. Ведь, именно это скилл поиска ответов пригодится тебе на первой работе. И только после этого спрашивать дипломного руководителя
* В одном вопросе должна быть заложена одна проблема 
* По возможности, прикреплять к вопросу скриншоты и стрелочкой показывать где не получается. Программу для этого можно скачать здесь https://app.prntscr.com/ru/
* По возможности, задавать вопросы в комментариях к коду. 
* Начинать работу над дипломом как можно раньше! Чтобы было больше времени на правки. 
* Делать диплом по-частям, а не все сразу. Иначе, есть шанс, что нужно будет все переделывать :)  

**Что следует делать, чтобы ничего не получилось:**

* Писать вопросы вида “Ничего не работает. Не запускается. Всё сломалось.”
* Откладывать диплом на потом. 
* Ждать ответ на свой вопрос моментально. Дипломные руководители - работающие разработчики, которые занимаются, кроме преподавания, своими проектами. Их время ограничено, поэтому постарайтесь задавать правильные вопросы, чтобы получать быстрые ответы! 

