import json

class Library:
    def __init__(self, db_file='library_db.json'):
        """
        Инициализация объекта библиотеки.
        """
        self.db_file = db_file
        self.books = self.load_books()

    def load_books(self):
        """
        Загрузка списка книг из файла.
        """
        try:
            with open(self.db_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_books(self):
        """
        Сохранение списка книг в файл.
        """
        with open(self.db_file, 'w') as file:
            json.dump(self.books, file, indent=2)

    def add_book(self, title, author, description, genre):
        """
        Добавление новой книги в библиотеку.
        """
        new_book = {'title': title, 'author': author, 'description': description, 'genre': genre}
        self.books.append(new_book)
        self.save_books()
        print(f'Книга "{title}" успешно добавлена.')

    def display_books(self):
        """
        Вывод списка книг на экран.
        """
        print("\nСписок книг:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book['title']} - {book['author']}")

    def view_book_details(self, index):
        """
        Просмотр подробной информации о книге.
        """
        if 0 <= index < len(self.books):
            book = self.books[index]
            print("\nПодробная информация:")
            print(f"Название: {book['title']}")
            print(f"Автор: {book['author']}")
            print(f"Описание: {book['description']}")
            print(f"Жанр: {book['genre']}")
        else:
            print("Неверный номер книги.")

    def filter_books_by_genre(self, genre):
        """
        Вывод книг по заданному жанру.
        """
        filtered_books = [book for book in self.books if book['genre'] == genre]
        if filtered_books:
            print(f"\nКниги жанра '{genre}':")
            for i, book in enumerate(filtered_books, 1):
                print(f"{i}. {book['title']} - {book['author']}")
        else:
            print(f"Нет книг жанра '{genre}'.")

    def search_books(self, keyword):
        """
        Поиск книги по названию или автору.
        """
        results = [book for book in self.books if keyword.lower() in (book['title'].lower(), book['author'].lower())]
        if results:
            print(f"\nРезультаты поиска для '{keyword}':")
            for i, book in enumerate(results, 1):
                print(f"{i}. {book['title']} - {book['author']}")
        else:
            print(f"По запросу '{keyword}' ничего не найдено.")

    def remove_book(self, index):
        """
        Удаление книги из библиотеки.
        """
        if 0 <= index < len(self.books):
            removed_book = self.books.pop(index)
            self.save_books()
            print(f'Книга "{removed_book["title"]}" успешно удалена.')
        else:
            print("Неверный номер книги.")


def main():
    """
    Основная функция для взаимодействия с библиотекой.
    """
    library = Library()

    while True:
        print("\n===== Библиотека =====")
        print("1. Добавить новую книгу")
        print("2. Просмотреть список книг")
        print("3. Просмотреть подробности о книге")
        print("4. Вывести книги по жанру")
        print("5. Поиск книги по названию или автору")
        print("6. Удалить книгу")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            description = input("Введите описание книги: ")
            genre = input("Введите жанр книги: ")
            library.add_book(title, author, description, genre)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            try:
                index = int(input("Введите номер книги для просмотра подробной информации: ")) - 1
                library.view_book_details(index)
            except ValueError:
                print("Неверный ввод. Введите число.")

        elif choice == '4':
            genre = input("Введите жанр для фильтрации: ")
            library.filter_books_by_genre(genre)

        elif choice == '5':
            keyword = input("Введите ключевое слово для поиска: ")
            library.search_books(keyword)

        elif choice == '6':
            try:
                index = int(input("Введите номер книги для удаления: ")) - 1
                library.remove_book(index)
            except ValueError:
                print("Неверный ввод. Введите число.")

        elif choice == '0':
            break

        else:
            print("Неверный выбор. Пожалуйста, введите корректное значение.")


if __name__ == "__main__":
    main()

#Если я с этой фигнёй которую я писал не пройду то я четвертую проверяющего(конечно же в игре и в шутку, не баньте)
#Я старался писать грамотно. Даже коментарии в своём роде как у Экс-Герцога