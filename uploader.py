class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        import requests
        import os

        file_name = os.path.basename(file_path)

        url = f"https://cloud-api.yandex.net/v1/disk/resources/upload?path={file_name}"

        headers = {
            "Authorization": f"OAuth {self.token}"
        }
        with open(file_path, "rb") as file:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                upload_url = response.json().get("href")
                if upload_url:
                    upload_response = requests.put(upload_url, files={"file": file})
                    if upload_response.status_code == 201:
                        print(f"Файл {file_name} успешно загружен на Яндекс.Диск")
                    else:
                        print(f"Ошибка загрузки файла {file_name} на Яндекс.Диск")
                else:
                    print("Не удалось получить URL для загрузки файла на Яндекс.Диск")
            else:
                print("Ошибка получения URL для загрузки файла на Яндекс.Диск")


if __name__ == '__main__':
    path_to_file = input("Введите путь до файла на компьютере: ")
    token = input("Введите токен Яндекс.Диска: ")
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
