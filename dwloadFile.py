
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

url = 'https://raw.githubusercontent.com/globaldothealth/monkeypox/main/latest.csv'
filename = 'C:\Python\Projects\DownloadFiles\Monkeypox\latest.csv'
req = requests.get(url)
file = open(filename, 'wb')

for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
