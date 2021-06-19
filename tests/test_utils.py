from unittest.mock import MagicMock, patch, Mock
import pytest
from parking_manager.src import utils


@patch("parking_manager.src.utils.print")
def test_print_parking_created(print_mock):
    num_slots = 2
    utils.print_parking_created(num_slots)

    assert print_mock.call_args[0][0] == "Created parking of 2 slots"


@patch("parking_manager.src.utils.print")
def test_print_park_vehicle_slot_minus_one(print_mock):
    slot = -1
    regno = "XYZ"
    utils.print_park_vehicle(slot, regno)

    assert print_mock.call_args[0][0] == "Parking is full, no space for new vehicles"


@patch("parking_manager.src.utils.print")
def test_print_park_vehicle_slot_minus_two(print_mock):
    slot = -2
    regno = "XYZ"
    utils.print_park_vehicle(slot, regno)

    assert print_mock.call_args[0][0] == "Car with this registration number is already parked."


@patch("parking_manager.src.utils.print")
def test_print_park_vehicle_slot_minus_two(print_mock):
    slot = 2
    regno = "XYZ"
    utils.print_park_vehicle(slot, regno)

    assert print_mock.call_args[0][0] == "Car with vehicle registration number \"XYZ\" has been parked at slot number 2"


@patch("parking_manager.src.utils.print")
def test_print_slot_nums_or_regno_type_not_tuple(print_mock):
    content_list = []
    
    try:
        utils.print_slot_nums_or_regno(content_list)
    except Exception as e:
        assert e.args[0] == "Expected a tuple to print, but got <class 'list'>"



@patch("parking_manager.src.utils.print")
def test_print_slot_nums_or_regno_len_zero(print_mock):
    content_list = ()

    utils.print_slot_nums_or_regno(content_list)

    assert print_mock.call_args[0][0] == "No parked car matches the query"


@patch("parking_manager.src.utils.print")
def test_print_slot_nums_or_regno_valid_input(print_mock):
    content_list = (1,2)

    utils.print_slot_nums_or_regno(content_list)

    assert print_mock.call_args[0][0] == "1,2"


@patch("parking_manager.src.utils.print")
def test_print_vehicle_leave_type_not_tuple(print_mock):
    content_list = []
    
    try:
        utils.print_vehicle_leave(content_list)
    except Exception as e:
        assert e.args[0] == "Expected a tuple to print, but got <class 'list'>"


@patch("parking_manager.src.utils.print")
def test_print_vehicle_leave_len_zero(print_mock):
    content_list = ()

    utils.print_vehicle_leave(content_list)

    assert print_mock.call_args[0][0] == "Slot already vacant"


@patch("parking_manager.src.utils.print")
def test_print_vehicle_leave_valid_input(print_mock):
    content_list = (1, "KA-01-HH-1234", "22")

    utils.print_vehicle_leave(content_list)

    assert print_mock.call_args[0][0] == "Slot number 1 vacated, the car with vehicle registration "\
            "number \"KA-01-HH-1234\" left the space, the driver of the car was "\
            "of age 22"