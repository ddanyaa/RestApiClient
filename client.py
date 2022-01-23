import requests
import json


class Client:
    url = 'http://165.22.247.10'

    def __init__(self, username, password):
        user = {'username': f'{username}', 'password': f'{password}'}
        rsp = requests.post(Client.url + '/login', data=user)
        if rsp.status_code == 200:
            js = json.loads(rsp.text)
            self.header = {'x-access-tokens': f"{js['token']}"}
            print("вы успешно вошли в аккаунт")
        else:
            print("Ошибка", rsp.status_code)

    def task_view(self):
        rsp = requests.get(Client.url + '/todo', headers=self.header)
        if rsp.status_code == 200:
            print(json.loads(rsp.text))
        else:
            print("Ошибка", rsp.status_code)

    def create_task(self, task):
        new_task = {'task': f'{task}'}
        rsp = requests.post(Client.url + '/todo', data=new_task, headers=self.header)
        if rsp.status_code == 200:
            print("\tЗадача добавлена")
        else:
            print("Ошибка", rsp.status_code)

    def update_task(self, task, task_id):
        updated_task = {'task': f'{task}'}
        rsp = requests.put(Client.url + f'/todo/{task_id}', data=updated_task, headers=self.header)
        if rsp.status_code == 200:
            print("\tЗадача изменена")
        else:
            print("Ошибка", rsp.status_code)

    def deleting_task(self, task_id):
        rsp = requests.delete(Client.url + f'/todo/{task_id}', headers=self.header)
        if rsp.status_code == 200:
            print("\tЗадача удалена")
        else:
            print("Ошибка", rsp.status_code)

    def file_upload(self, filename):
        file = {'file': open(filename, 'rb')}
        rsp = requests.post(Client.url + '/files', files=file, headers=self.header)
        if rsp.status_code == 200:
            print("\tФайл добавлен!")
        else:
            print("Ошибка", rsp.status_code)

    def file_browsing(self):
        rsp = requests.get(Client.url + '/files', headers=self.header)
        if rsp.status_code == 200:
            print(json.loads(rsp.text))
        else:
            print("Ошибка", rsp.status_code)

    def download_file(self, filename):
        rsp = requests.get(Client.url + f'/files/{filename}', headers=self.header)
        if rsp.status_code == 200:
            f = open(f'./{filename}', 'wb')
            f.write(rsp.content)
            f.close()
            print("\tФайл скачан")
        else:
            print("Ошибка", rsp.status_code)

    def delete_file(self, filename):
        rsp = requests.delete(Client.url + f'/files/{filename}', headers=self.header)
        if rsp.status_code == 200:
            print("\tФайл удален!")
        else:
            print("Ошибка", rsp.status_code)