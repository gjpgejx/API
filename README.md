# API
Эта программа выполняет следующие действия:



Импортирует необходимые модули openmeteo_requests, requests_cache, pandas и retry_requests.

Создает кешированную сессию cache_session с использованием requests_cache для запросов к API сроком действ

Создает сессию с повторными запросами retry_session с использованием retry_requests, с параметрами повторов 5 раз и коэффициентом задержки 0.2.

Создает клиент OpenMeteo и делает запрос к API Open-Meteo для получения прогноза погоды.

Извлекает информацию о координатах, высоте, часовом поясе и разнице с GMT+0 из полученного ответа.

Извлекает данные почасовой температуры из ответа и создает DataFrame с этими данными, используя библиотеку pandas.

Выводит полученный DataFrame с данными почасовой температуры.

Создает файл requirements.txt и записывает в него необходимые зависимости.

Создает файл .gitignore и записывает в него список файлов и директорий, которые будут игнорироваться Git.


Эта программа использует API Open-Meteo для получения прогноза погоды
