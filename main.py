class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.completed = False

    def __str__(self):
        status = "Виконано" if self.completed else "Не виконано"
        return f"{self.name} - {self.description} - Дедлайн: {self.deadline} - Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Завдання '{task.name}' додано до списку.")

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                print(f"Завдання '{task_name}' видалено.")
                return
        print(f"Завдання '{task_name}' не знайдено.")

    def mark_as_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                print(f"Завдання '{task_name}' відмічено як виконане.")
                return
        print(f"Завдання '{task_name}' не знайдено.")

    def display_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.")
        else:
            print("Список завдань:")
            for task in self.tasks:
                print(task)

if __name__ == "__main__":
    manager = TaskManager()

    task1 = Task("Підготувати звіт", "Написати звіт про результати дослідження", "15.05.2024")
    task2 = Task("Посадити квіти", "Купити квіти та посадити у саду", "20.05.2024")
    manager.add_task(task1)
    manager.add_task(task2)

    manager.display_tasks()

    manager.mark_as_completed("Підготувати звіт")

    manager.display_tasks()

    manager.remove_task("Посадити квіти")

    manager.display_tasks()
