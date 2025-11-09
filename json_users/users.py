import json

def create_json(filename):
    users = []
    n = int(input("Введите количество пользователей: "))

    for i in range(n):
        user = input("Введите имя пользователя: ")
        login = input("Введите логин: ")
        last_enter = input("Введите время последнего входа: ")
        len_of_stay = int(input("Введите время пребывания на сайте (мин): "))

        all_inf = {
            "user" : user,
            "login" : login,
            "last enter time" : last_enter,
            "length of stay" : len_of_stay
        }
        
        users.append(all_inf)

    data = {"users" : users}

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)
    print(f"Файл '{filename}' создан")

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except:
        print("Ошибка чтения файла")
        return

    print("Информация о пользователях\n")
    
    for user in data.get("users"):
        print(f"Имя: {user['user']} \n")
        print(f"Логин: {user['login']} \n")
        print(f"Время последнего захода: {user['last enter time']} \n")
        print(f"Время пребывания на сайте (мин): {user['length of stay']} \n")
        print("-" * 45)
          
def main():
    while(True):
        print("Выберите действие")
        print("1 - создать JSON файл с информацией o пользователях\n")
        print("2 - прочитать JSON файл с информацией o пользователях\n")
        print("3 - выход из программы\n")

        choice = input("Введите цифру: ")

        if choice == "1":
            filename = input("Введите имя файла для создания (например users.json): ")
            create_json(filename)
        elif choice == "2":
            filename = input("Введите имя файла для прочтения (например users.json): ")
            read_file(filename)
        elif choice == "3":
            print("Выход из программы")
            break
        else:
            print("Введён некорректный номер действия")
            
if __name__ == "__main__":
    main()
