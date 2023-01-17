class PatientList():

    def __init__(self, number_of_patients):
        self.conditions_key_names = {0: "Тяжело болен", 1: "Болен",
                                     2: "Слегка болен", 3: "Готов к выписке"}

        self.default_condition = 1
        self.persons_status_dict = {}
        for person_id in range(number_of_patients):
            zero_compensation = 1
            real_id = person_id + zero_compensation
            self.persons_status_dict[real_id] = self.default_condition

    def is_id_in_patient_list(self, patient_id):
        return patient_id in self.persons_status_dict

    def is_patient_ready_for_discharge(self, patient_id):
        completely_healthy = 3
        return self.persons_status_dict[patient_id] == completely_healthy

    def is_patient_dying(self, patient_id):
        at_death = 0
        return self.persons_status_dict[patient_id] == at_death

    def get_current_patient_condition(self, patient_id):
        return self.persons_status_dict[patient_id]

    def get_id_condition_key_name(self, patient_id):
        condition_key = self.persons_status_dict[patient_id]
        return self.conditions_key_names[condition_key]

    def increase_health_condition(self, patient_id):
        self.persons_status_dict[patient_id] += 1

    def decrease_health_condition(self, patient_id):
        self.persons_status_dict[patient_id] -= 1

    def improve_patient_health_condition(self, patient_id):
        if self.is_id_in_patient_list(patient_id):
            if self.is_patient_ready_for_discharge(patient_id):
                print(f"Пациент {patient_id} готов к выписке")
            else:
                self.increase_health_condition(patient_id)
                print(
                    f'Статус пациента {patient_id} - {self.get_id_condition_key_name(patient_id)}')
        else:
            print("Такого пациента нет в природе")

    def deriorate_patient_health_condition(self, patient_id):
        if self.is_id_in_patient_list(patient_id):
            if self.is_patient_dying(patient_id):
                print(f"Пациент {patient_id} - уже при смерти")
            else:
                self.decrease_health_condition(patient_id)
                print(
                    f'Статус пациента {patient_id} - {self.get_id_condition_key_name(patient_id)}')
        else:
            print("Такого пациента нет в природе")

    def discharge_patient(self, patient_id):
        self.persons_status_dict.pop(patient_id)
        print(F"Пациент {patient_id} благополучно отправлен домой.")

    def show_statistics(self):
        number_of_patients = len(self.persons_status_dict)
        ready_for_discharge_3 = 0
        slightly_sick_2 = 0
        sick_1 = 0
        very_sick_0 = 0
        print(
            f"В больнице на данный момент находится {number_of_patients} человек, из них:")
        for id, condition in self.persons_status_dict.items():
            if condition == 0:
                very_sick_0 += 1
            elif condition == 1:
                sick_1 += 1
            elif condition == 2:
                slightly_sick_2 += 1
            elif condition == 3:
                ready_for_discharge_3 += 1

        print(f"""\t{ready_for_discharge_3} - готовы к выписке
\t{slightly_sick_2} - слегка больны
\t{sick_1} - больны
\t{very_sick_0} - серьезно больны"""
              )


def input_patient_id():
    try:
        id = int(input("\nВведите ID пациента:"))
    except ValueError:
        print("Ошибка: Значение должно быть числом.")
        id = input_patient_id()
    return id


def main():
    enter_message = """- Повысить статус пациента
- Понизить статус пациента
- Выписать пациента
- Статистика
- Выйти"""

    number_of_pacients = 200
    patients = PatientList(number_of_pacients)
    print(enter_message)
    while True:
        command = input("\n>>>").lower()
        if command in "повысить статус пациента":
            id = input_patient_id()
            patients.improve_patient_health_condition(id)
        elif command == "понизить статус пациента":
            id = input_patient_id()
            patients.deriorate_patient_health_condition(id)
        elif command == "выписать пациента":
            id = input_patient_id()
            patients.discharge_patient(id)
        elif command == "статистика":
            patients.show_statistics()
        elif command == "выйти":
            break
        else:
            print("Такой команды нет.")


if __name__ == "__main__":
    main()
