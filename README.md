# Mountains (учебный проект)                                                                                                                                                              
Задача - разработать приложение ("Mountains") для туристов, где они, проходя определенные горные перевалы, могут вносить информацию по разным местам прохождения.   Пользователь устанавливает приложение на своё устройство и регистрируется. На любом этапе пользователь будет иметь возможность создать публикацию с географическими координатами места и его высотой, вносить свои контактные данные, а также загружать фотографии перевала. Admin данного приложения в свою очередь проверяет полученную    информацию о новом объекте и меняет его статус.

Спринт_1
  1. Создаём классы, с помощью которых можно добавить в БД новый перевал и всю информацию о нём.
  2. Реализовываем REST API с учетом задания от заказчика для обмена данными.

Спринт_2
  1. Делаем так, чтобы можно было редактировать отправленные на сервер данные об объекте, если они в статусе new.
  2. Делаем так, чтобы можно было редактировать все поля, кроме тех, что содержат в себе ФИО, адрес почты и номер телефона. Если поле status имеет значение, отличное
от new, делаем редактирование данных об объекте невозможным.
  4. Делаем так, чтобы можно было просматривать статус модерации для объекта.
  5. Делаем так, чтобы можно было просматривать все объекты, когда-либо отправленные на сервер самим пользователем, а также их статусы (Для этого я создал отдельную
страницу со всеми публикациями зарегистрированного пользователя).

Спринт_3
  1. Приводим качество кода в порядок.
  2. Пишем документацию.
