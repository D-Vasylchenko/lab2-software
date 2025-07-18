# Doubly Linked List Application

## Короткий опис застосунку
Цей проєкт реалізує клас двобічно зв'язного списку, в якому елементами є літери (Character). Список підтримує основні операції, такі як додавання, вставка, видалення, пошук, обертання та інші.

## Розрахунок номера варіанту та опис варіанту
- **Номер варіанту**: 6%4=2
- **Опис варіанту**: Реалізація двобічно зв'язного списку, що підтримує всі стандартні операції (додавання, видалення, обертання, пошук, копіювання тощо). Програмне забезпечення реалізує додаткові функції для роботи з літерними елементами списку, забезпечуючи можливість маніпулювати цими елементами за допомогою стандартних методів.

## Інструкція, як зібрати проект та запустити тести

1. **Клонуйте репозиторій**:
   ```bash
   git clone https://github.com/D-Vasylchenko/lab2-software.git
   cd doubly-linked-list
Створіть та активуйте віртуальне середовище:
Для цього можна використати наступні команди:
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
Запустіть юніт тести:
Для запуску тестів використовуйте наступну команду:
python -m unittest discover -s . -p "test_main.py"
Перевірка тестів за допомогою GitHub Actions:
Кожного разу, коли ви пушите зміни до репозиторію, тести автоматично запускаються через CI/CD за допомогою GitHub Actions.
Посилання на коміт, на якому впали тести на CI

Тести впали на CI на коміті #841a4dc5ceb6b30791f3ddbcb01de88f2b653573, коли зміни у коді були внесені, що порушило деякі з юніт тестів.

Висновки

Юніт тести виявились дуже корисними в цьому проєкті. Вони дозволили:

Перевіряти коректність роботи кожної окремої функції класу, що дає змогу швидко знаходити помилки.
Автоматизувати перевірку всіх операцій на кожному етапі розробки, що дає гарантію стабільності коду.
Наявність CI допомогла автоматизувати процес тестування, що робить його зручнішим і ефективнішим.
В цілому, юніт тести значно полегшили розробку та виявлення помилок, і це був корисний інструмент для забезпечення якості коду.
