# My test task:

The task is to launch a mini-site with support for Google AMP and Yandex.Turbo.
1. Take a template - https://github.com/1vank1n/django-project-template
2. Create a Page model in the `main` application, which inherits Common, Seo. The Page model should have the fields title (Title), slug (url-name), content (Content, django-ckeditor subkeys for this field).
3. Add Page display in admin panel
4. Add view and url. The page should open at the address `/ url-name-which-set-in-the-model /`
5. Add a template that displays the page. Don't waste much time, but make the display of all fields.
6. Connect support for Google AMP and Yandex.Turbo for these pages.
7. Put everything on any free host (heroku for example) and in the repository.
____

# Моя тестовая задача:

Задача — запустить мини-сайт с поддержкой Google AMP и Яндекс.Турбо.
1. Взять шаблон — https://github.com/1vank1n/django-project-template
2. Создать в приложении `main` модель Page (Страница), которая наследует Common, Seo. У модели Page должны быть поля title (Название), slug (url-имя), content (Контент, подключи django-ckeditor для этого поля).
3. Добавить отображение Page в админке
4. Добавить view и url. Страница должна открываться по адресу `/url-имя-которое-задал-в-модели/`
5. Добавить шаблон который выводит страницу. Сильно время не трать, но сделай отображение всех полей.
6. Подключи поддержку Google AMP  и Яндекс.Турбо у этих страниц.
7. Всё выложи на любой бесплатный хост (heroku например) и в репозиторий.
