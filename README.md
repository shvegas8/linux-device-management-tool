EN
# linux-device-management-tool

A simple command-line utility for managing storage devices in Linux. It provides a user-friendly menu to list devices, format, mount/unmount, create mount points, and check available space. All actions are logged for tracking purposes.

## Key Features:

List connected devices
Format devices
Create and manage mount points
Check available space
Log all operations

## Requirements:
Linux OS
Python 3.x
(`sudo`) privileges

## Usage:

Clone the repository.
Run python3 device_management.py.

## Logging
All performed actions are recorded in the device_management.log file.

## Warnings
FORMATTING DELETES ALL DATA ON THE DEVICE.

Most operations require superuser privileges (`sudo`).

RU
# linux-device-management-tool

Программа для управления устройствами хранения данных в системе Linux с помощью командной строки. Позволяет выполнять операции с подключенными устройствами через удобное меню: форматирование, создание точек монтирования, проверка доступного места и многое другое.

## Функционал:

- Список подключенных устройств.
- Проверка смонтированных устройств.
- Форматирование устройства.
- Создание точки монтирования и монтирование устройства.
- Размонтирование устройства.
- Удаление точки монтирования.
- Проверка доступного места на устройствах.

## Требования

- Операционная система: Linux.
- Python версии 3.x.
- Права суперпользователя (`sudo`).

## Установка и запуск
Склонируйте репозиторий
Запустите программу: Run python3 device_management.py.

## Логирование

Все выполненные действия записываются в файл `device_management.log`.

## Предупреждения

1. ФОРМАТИРОВАНИЕ УДАЛЯЕТ ВСЕ ДАННЫЕ НА УСТРОЙСТВЕ.
2. Большинство операций требуют прав суперпользователя (`sudo`).
