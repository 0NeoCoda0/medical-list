# У каждого пациента есть номер_ID и состояние здоровья.

patients: list[int] = []
conditions_key_names = {0: "Тяжело болен", 1: "Болен",
                     2: "Слегка болен", 3: "Готов к выписке"}


def get_current_pacient_condition(id):
    return conditions_key_names[patients[id - 1]]


def init(number_patients: int = 200):
    global patients
    # Изначально Статус ВСЕХ пациентов - "Болен"
    patients = [1] * number_patients


def get_pacient_condition(id_patient: int) -> tuple[int, str]:
    """Получение статуса пациента."""
    if 0 < id_patient <= len(patients):
        return (
            patients[id_patient - 1],
            f'Статус пациента: "{conditions_key_names[patients[id_patient - 1]]}"',
        )
    else:
        return -1, "Ошибка. В больнице нет пациента с таким ID"


def improve_pacient_health(id_patient: int) -> tuple[bool, str] | tuple[bool, None]:
    """Повысить статус пациента."""

    if 0 < id_patient <= len(patients):  # № пациента корректный
        patients[id_patient - 1] += 1  # повышаем статус
        return True, f'Новый статус пациента: "{conditions_key_names[patients[id_patient - 1]]}"'
    return False, None


def deriorate_pacient_health(id_patient: int) -> tuple[bool, str]:
    """Понизить статус пациента."""
    if 0 < id_patient <= len(patients):  # № пациента корректный
        if patients[id_patient - 1] == 0:  # понижение статуса невозможно
            return (
                False,
                "Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)",
            )
        patients[id_patient - 1] -= 1  # понижаем статус
        return True, f'Новый статус пациента: "{conditions_key_names[patients[id_patient - 1]]}"'
    else:
        return False, "Ошибка. В больнице нет пациента с таким ID"


def discharge_pacient(id_patient: int) -> tuple[bool, str]:
    """Выписать пациента."""
    if 0 < id_patient < len(patients):  # № пациента корректный
        del patients[id_patient - 1]  # Удаляем пациента из списка
        return True, "Пациент выписан из больницы"
    else:
        return False, "Ошибка. В больнице нет пациента с таким ID"


def calculate_statistics() -> str:
    """Рассчитать статистику."""
    statistic_list = f"В больнице на данный момент находится {len(patients)} человек, из них:\n"
    if len(patients) <= 0:
        return "В больнице нет пациентов\n"

    # Перебор всех возможных состояний пациентов
    # получаем ключ и значение из словаря 'conditions_key_names'
    for condition_key, condition_name in conditions_key_names.items():
        # Подсчёт количества пациентов с определённым состоянием
        count = patients.count(condition_key)
        if count > 0:  # Если пациенты с состоянием condition_key есть в больнице, то добавляем к отчёту
            statistic_list += f'\t- в статусе "{condition_name}": {count} чел.\n'
    return statistic_list


# Ввод номера пациента
# и формирование информации об ошибке, если она есть
# возвращаем номер пациента и сообщение для отображения на экране
def input_patient_id() -> tuple[int, str] | tuple[int, None]:
    try:
        id_patient = int(input("Введите ID пациента: "))
    except (Exception,):  # перехват ошибки ввода не числа
        id_patient = -1

    if id_patient < 1:  # если ввели не целое, положительное число
        return -1, "Ошибка. ID пациента должно быть числом (целым, положительным)"
    else:
        return id_patient, None


# Вопрос про выписку клиента из больницы
# возвращаем True, если ввели 'да' или 'yes'
def input_yes_no() -> bool:
    return input("Желаете этого клиента выписать? (да/нет): ").strip().lower() in [
        "да",
        "yes",
    ]


# Основная функция обработки команд, вводимых в консоли
def main():
    is_program_working = True
    while is_program_working:
        cmd = input("Введите команду: ").strip().lower()

        if cmd in ["узнать статус пациента", "get conditions_key_names"]:
            pacient_id, info = input_patient_id()
            if pacient_id > 0:  # № пациента корректный
                _, info = get_pacient_condition(pacient_id)

        elif cmd in ["повысить статус пациента", "conditions_key_names up"]:
            pacient_id, info = input_patient_id()
            if pacient_id > 0:  # № пациента корректный
                stat, info = get_pacient_condition(pacient_id)
                if stat >= 3:  # статус максимальный
                    if input_yes_no():
                        _, info = discharge_pacient(pacient_id)
                    else:
                        info = 'Пациент остался в статусе "Готов к выписке"'
                else:
                    _, info = improve_pacient_health(pacient_id)

        elif cmd in ["понизить статус пациента", "conditions_key_names down"]:
            pacient_id, info = input_patient_id()
            if pacient_id > 0:
                _, info = deriorate_pacient_health(pacient_id)

        elif cmd in ["выписать пациента", "discharge_pacient"]:
            pacient_id, info = input_patient_id()
            if pacient_id > 0:
                _, info = discharge_pacient(pacient_id)

        elif cmd in ["рассчитать статистику", "calculate statistics"]:
            info = calculate_statistics()

        elif cmd in ["стоп", "stop"]:
            info = "Сеанс завершён."
            is_program_working = False

        else:
            info = "Неизвестная команда! Попробуйте ещё раз"

        print(info)


if __name__ == "__main__":
    init()
    main()
