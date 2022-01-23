from client import Client

username = 'dasha'
password = '12345'
client = Client(username, password)

print("\t1- Получение списка задач;")
print("\t2- Добавление задачи;")
print("\t3- Обновление задач;")
print("\t4- Удаление задачи;")
print("\t5- Загрузка файла;")
print("\t6- Отображение списка файлов;")
print("\t7- Скачать файл;")
print("\t8- Удалить файл;")
print("\t0- Выход.\n")

cmd = input("Введите команду: ")
while cmd != "0":
    if cmd == "1":
        client.task_view()
    elif cmd == "2":
        task = input("\tДобавьте новую задачу: ")
        client.create_task(task)
    elif cmd == "3":
        task_id = input("\tВведите id задачи, которую вы хотели бы изменить: ")
        task = input("\tИзмените выбранную задачу: ")
        client.update_task(task, task_id)
    elif cmd == "4":
        task_id = input("\tВведите id задачи, которую вы хотели бы удалить: ")
        client.deleting_task(task_id)
    elif cmd == "5":
        filename = input("\tВведите название файла, который нужно загрузить: ")
        client.file_upload(filename)
    elif cmd == "6":
        client.file_browsing()
    elif cmd == "7":
        filename = input("\tВведите название файла, который нужно скачать: ")
        client.download_file(filename)
    elif cmd == "8":
        filename = input("\tВведите название файла, который нужно удалить: ")
        client.delete_file(filename)
    else:
        print("Введенная команда не существует!")
    cmd = input("Введите команду: ")
