# Технологии программирования

Лабораторные работы по дисциплине **«Технологии программирования»**.

**Язык:** Python 3  
**Репозиторий:** [Erikqwerty1/programming-technologies](https://github.com/Erikqwerty1/programming-technologies)

## Лабораторные работы

| № | Тема | Материалы |
|:--:|---|---|
| 01 | Объектно-ориентированное программирование | [Lab01](Lab01/) · [Отчёт](Lab01/report.pdf) |
| 02 | ООП и проектирование классов | [Lab02](Lab02/) · [Код](Lab02/main.py) · [Отчёт](Lab02/report.pdf) |
| 03 | Порождающие паттерны проектирования | [Lab03](Lab03/) |
| 04 | Поведенческие паттерны проектирования | [Lab04](Lab04/) |

## Паттерны проектирования

### Лабораторная №3 — порождающие

| Паттерн | Реализация |
|---|---|
| Singleton | [singleton.py](Lab03/singleton.py) |
| Factory Method | [factory_method.py](Lab03/factory_method.py) |
| Abstract Factory | [abstract_factory.py](Lab03/abstract_factory.py) |
| Builder | [builder.py](Lab03/builder.py) |

### Лабораторная №4 — поведенческие

| Паттерн | Реализация |
|---|---|
| Strategy | [strategy.py](Lab04/strategy.py) |
| Chain of Responsibility | [chain_of_responsibility.py](Lab04/chain_of_responsibility.py) |
| Iterator | [iterator.py](Lab04/iterator.py) |

## Запуск

Установите **Python 3** и клонируйте репозиторий:

```bash
git clone https://github.com/Erikqwerty1/programming-technologies.git
cd programming-technologies
```

Запуск примеров из корня репозитория:

```bash
python Lab02/main.py
python Lab03/singleton.py
python Lab03/factory_method.py
python Lab03/abstract_factory.py
python Lab03/builder.py
python Lab04/strategy.py
python Lab04/chain_of_responsibility.py
python Lab04/iterator.py
```

Для этих примеров сторонние зависимости не требуются.

## Структура

```text
programming-technologies/
├── Lab01/
│   ├── README.md
│   └── report.pdf
├── Lab02/
│   ├── README.md
│   ├── main.py
│   └── report.pdf
├── Lab03/
│   ├── README.md
│   ├── singleton.py
│   ├── factory_method.py
│   ├── abstract_factory.py
│   └── builder.py
├── Lab04/
│   ├── README.md
│   ├── strategy.py
│   ├── chain_of_responsibility.py
│   └── iterator.py
├── .gitattributes
├── .gitignore
└── README.md
```

## Автор

[Erikqwerty1](https://github.com/Erikqwerty1)
