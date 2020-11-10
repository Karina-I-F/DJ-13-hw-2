from django.urls import path, register_converter
from file_server.app.converters import DateConverter
from file_server.app.views import file_list, file_content

register_converter(DateConverter, 'dtc')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),
    path('<dtc:date>/', file_list, name='file_list'),  # задайте необязательный параметр "date"
    # для детальной информации смотрите HTML-шаблоны в директории templates
    path('<str:name>/', file_content, name='file_content'),
]
