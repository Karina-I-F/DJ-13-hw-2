import datetime
import os
from django.shortcuts import render
from django.conf import settings


def file_list(request, date=None):
    template_name = 'index.html'

    files = os.listdir(settings.FILES_PATH)

    files_data = []
    for file_name in files:
        full_file_name = os.path.join(settings.FILES_PATH, file_name)
        stat_info = os.stat(full_file_name)
        ctime = datetime.datetime.fromtimestamp(stat_info.st_ctime)

        if date and date.date() != ctime.date():
            continue

        files_data.append({
            'name': file_name,
            'ctime': ctime,
            'mtime': datetime.datetime.fromtimestamp(stat_info.st_mtime),
        })
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': files_data,
        'date': date.date() if date else None,
    }

    return render(request, template_name, context)


def file_content(request, name):
    full_file_path = os.path.join(settings.FILES_PATH, name)
    with open(full_file_path) as f:
        file_content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )
