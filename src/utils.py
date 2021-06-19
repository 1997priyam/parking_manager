def print_parking_created(num_slot):
    print("Created parking of {} slots".format(num_slot))


def print_park_vehicle(slot, regno):
    if slot == -1:
        print("Parking is full, no space for new vehicles")
    elif slot == -2:
        print("Car with this registration number is already parked.")
    else:
        print("Car with vehicle registration number \"{}\" has been parked "
            "at slot number {}".format(regno, slot))


def print_slot_nums_or_regno(content_list):
    if type(content_list) != tuple:
        raise Exception("Expected a tuple to print, but got {}".format(type(content_list)))
    if len(content_list) == 0:
        print("No parked car matches the query")
    else:
        print_string = ""
        for eachSlot in content_list:
            print_string = print_string + "{},".format(eachSlot)
        print_string = print_string[:-1]
        print(print_string)


def print_vehicle_leave(details):
    if type(details) != tuple:
        raise Exception("Expected a tuple to print, but got {}".format(type(details)))
    if len(details) == 0:
        print("Slot already vacant")
    else:
        slot, regno, driver_age = details
        print("Slot number {} vacated, the car with vehicle registration "
            "number \"{}\" left the space, the driver of the car was "
            "of age {}".format(slot, regno, driver_age))
