import os
import logging

# Настройка логирования
logging.basicConfig(filename='device_management.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list_devices():
    print("\nСписок подключенных устройств: \n")
    os.system("lsblk -o NAME, SIZE, TYPE,MOUNTPOINT")
    logging.info("Выведен список подключенных устройств.")

def check_mount():
    print("\nУстройства, смонтированные в систему:\n") 
    os.system("df -h")
    logging.info("Проверены смонтированные устройства.")

def format_device():
    device = input("Введите имя устройства для форматирования (например, /dev/sdX1): ") 
    os.system(f"sudo mkfs.ext4 {device}")
    print(f"Устройство {device} отформатировано.")
    logging.info(f"Устройство {device} отформатировано.")

def create_mount_point():
    mount_point = input("Введите путь для точки монтирования (например, /mnt/new_device): ")
    os.system(f"sudo mkdir -p {mount_point}")
    device = input("Введите имя устройства для монтирования (например, /dev/sdX1): ")
    os.system(f"sudo mount {device} {mount_point}")
    print(f"Устройство {device} смонтировано в {mount_point}.")
    logging.info(f"Устройство {device} смонтировано в {mount_point}.")

def unmount_device():
    device = input("Введите путь точки монтирования (например, /mnt/new_device): ")
    os.system(f"sudo umount {device}")
    print(f"Устройство, смонтированное в {device}, было успешно размонтировано.")
    logging.info(f"Устройство, смонтированное в {device}, было успешно размонтировано.")

def remove_mount_point():
    mount_point = input("Введите путь точки монтирования для удаления (например, /mnt/new_device): ")
    os.system(f"sudo umount {mount_point}")  # Сначала размонтируем устройство
    os.system(f"sudo rmdir {mount_point}")   # Затем удалим точку монтирования
    print(f"Точка монтирования {mount_point} была успешно удалена.")
    logging.info(f"Точка монтирования {mount_point} была успешно удалена.")

def check_available_space():
    print("\nДоступное место на всех устройствах:\n")
    os.system("df -h")
    logging.info("Проверено доступное место на всех устройствах.")

def main_menu():
    while True:
        print("\n=== Меню управления устройствами ===")
        print("1. Список подключенных устройств")
        print("2. Проверить смонтированные устройства")
        print("3. Форматировать устройство")
        print("4. Создать точку монтирования и смонтировать устройство")
        print("5. Размонтировать устройство")
        print("6. Удалить точку монтирования")
        print("7. Проверить доступное место на устройствах")
        print("8. Выход")
        choice = input("Выберите действие (1-8): ")

        if choice == "1":
            list_devices()
        elif choice == "2":
            check_mount()
        elif choice == "3":
            format_device()
        elif choice == "4":
            create_mount_point()
        elif choice == "5":
            unmount_device()
        elif choice == "6":
            remove_mount_point()
        elif choice == "7":
            check_available_space()
        elif choice == "8":
            print("Выход из программы.")
            logging.info("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()