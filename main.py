from src.slots_manager import SlotsManager 
from src import utils


def get_commands_from_file(file_name):
    final_commands = []
    try:
        with open(file_name, "r") as command_file:
            file_data = command_file.read()
        commands = file_data.split("\n")
        for eachCommand in commands:
            final_commands.append(eachCommand.split(" "))
    except FileNotFoundError:
        raise Exception("Invalid Filename, Exiting.")
    else:
        return final_commands


def main():
    try:
        print("Enter the file name: ")
        file_name = input()
        # file_name = "input.txt"
        command_list = get_commands_from_file(file_name)
        parking_lot = None

        for eachCommand in command_list:
            commandType = eachCommand[0]

            if commandType == "Create_parking_lot":
                num_slot = int(eachCommand[1])
                parking_lot = SlotsManager(num_slot)
                utils.print_parking_created(num_slot)
            elif commandType == "Park":
                regno = eachCommand[1]
                driver_age = eachCommand[3]
                slot = parking_lot.park_vehicle(regno, driver_age)
                utils.print_park_vehicle(slot, regno)
            elif commandType == "Slot_numbers_for_driver_of_age":
                driver_age = eachCommand[1]
                slot_nums = parking_lot.get_slot_numbers_from_driver_age(driver_age)
                utils.print_slot_nums_or_regno(slot_nums)
            elif commandType == "Slot_number_for_car_with_number":
                regno = eachCommand[1]
                slot_num = parking_lot.get_slot_number_from_regno(regno)
                utils.print_slot_nums_or_regno(slot_num)
            elif commandType == "Vehicle_registration_number_for_driver_of_age":
                driver_age = eachCommand[1]
                regnos = parking_lot.get_regno_from_driver_age(driver_age)
                utils.print_slot_nums_or_regno(regnos)
            elif commandType == "Leave":
                slot = int(eachCommand[1])
                details = parking_lot.leave_vehicle(slot)
                utils.print_vehicle_leave(details)
            elif commandType == "":
                pass
            else:
                raise Exception("Invalid Command. Exiting.")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()