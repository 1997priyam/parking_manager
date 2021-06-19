from unittest.mock import MagicMock, patch, mock_open
import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from parking_manager import main

@patch("parking_manager.main.open", new_callable=mock_open, read_data="some_data 12\n")
def test_get_commands_from_file_file_mock_data(mock_file):

    output = main.get_commands_from_file("input.txt")

    assert type(output) == list
    assert type(output[0]) == list
    assert len(output) == 2
    assert output[0] == ["some_data", "12"]

@patch("parking_manager.main.open", side_effect=[FileNotFoundError])
def test_get_commands_from_file_file_not_found(mock_file):

    try:
        output = main.get_commands_from_file("input.txt")
    except Exception as e:
        assert e.args[0] == "Invalid Filename, Exiting."


@patch("parking_manager.main.print")
@patch("parking_manager.main.get_commands_from_file")
@patch("parking_manager.main.input")
def test_main_file_not_found(input_mock, get_commands_mock, print_mock):
    input_mock.return_value = "xyz.txt"
    get_commands_mock.side_effect = [FileNotFoundError]

    output = main.main()
    assert print_mock.call_count == 2

    assert output is None

@patch("parking_manager.main.utils")
@patch("parking_manager.main.SlotsManager")
@patch("parking_manager.main.print")
@patch("parking_manager.main.get_commands_from_file")
@patch("parking_manager.main.input")
def test_main_command_type_create_parking_lot(input_mock, get_commands_mock, print_mock, slots_manager_mock, utils_mock):
    input_mock.return_value = "xyz.txt"
    get_commands_mock.return_value = [["Create_parking_lot", "11"]]
    
    output = main.main()

    assert output is None
    assert slots_manager_mock.call_count == 1
    assert utils_mock.print_parking_created.call_count == 1


@patch("parking_manager.main.utils")
@patch("parking_manager.main.SlotsManager")
@patch("parking_manager.main.print")
@patch("parking_manager.main.get_commands_from_file")
@patch("parking_manager.main.input")
def test_main_command_type_park(input_mock, get_commands_mock, print_mock, slots_manager_mock, utils_mock):
    input_mock.return_value = "xyz.txt"
    get_commands_mock.return_value = [["Create_parking_lot", "11"], ["Park", "KA-01-HH-1234", "driver_age", "21"]]
    slots_manager_obj = MagicMock()
    slots_manager_mock.return_value = slots_manager_obj

    output = main.main()

    assert output is None
    assert slots_manager_mock.call_count == 1
    assert slots_manager_obj.park_vehicle.call_count == 1
    assert utils_mock.print_parking_created.call_count == 1
    assert utils_mock.print_park_vehicle.call_count == 1


@patch("parking_manager.main.utils")
@patch("parking_manager.main.SlotsManager")
@patch("parking_manager.main.print")
@patch("parking_manager.main.get_commands_from_file")
@patch("parking_manager.main.input")
def test_main_command_type_get_slots_from_driver_age(input_mock, get_commands_mock, print_mock, slots_manager_mock, utils_mock):
    input_mock.return_value = "xyz.txt"
    get_commands_mock.return_value = [["Create_parking_lot", "11"], ["Slot_numbers_for_driver_of_age", "21"]]
    slots_manager_obj = MagicMock()
    slots_manager_mock.return_value = slots_manager_obj

    output = main.main()

    assert output is None
    assert slots_manager_mock.call_count == 1
    assert slots_manager_obj.get_slot_numbers_from_driver_age.call_count == 1
    assert utils_mock.print_parking_created.call_count == 1
    assert utils_mock.print_slot_nums_or_regno.call_count == 1


@patch("parking_manager.main.utils")
@patch("parking_manager.main.SlotsManager")
@patch("parking_manager.main.print")
@patch("parking_manager.main.get_commands_from_file")
@patch("parking_manager.main.input")
def test_main_command_type_get_slots_from_regno(input_mock, get_commands_mock, print_mock, slots_manager_mock, utils_mock):
    input_mock.return_value = "xyz.txt"
    get_commands_mock.return_value = [["Create_parking_lot", "11"], ["Slot_number_for_car_with_number", "KA-01-HH-1234"]]
    slots_manager_obj = MagicMock()
    slots_manager_mock.return_value = slots_manager_obj

    output = main.main()

    assert output is None
    assert slots_manager_mock.call_count == 1
    assert slots_manager_obj.get_slot_number_from_regno.call_count == 1
    assert utils_mock.print_parking_created.call_count == 1
    assert utils_mock.print_slot_nums_or_regno.call_count == 1


@patch("parking_manager.main.utils")
@patch("parking_manager.main.SlotsManager")
@patch("parking_manager.main.print")
@patch("parking_manager.main.get_commands_from_file")
@patch("parking_manager.main.input")
def test_main_command_type_get_regno_from_driver_age(input_mock, get_commands_mock, print_mock, slots_manager_mock, utils_mock):
    input_mock.return_value = "xyz.txt"
    get_commands_mock.return_value = [["Create_parking_lot", "11"], ["Vehicle_registration_number_for_driver_of_age", "11"]]
    slots_manager_obj = MagicMock()
    slots_manager_mock.return_value = slots_manager_obj

    output = main.main()

    assert output is None
    assert slots_manager_mock.call_count == 1
    assert slots_manager_obj.get_regno_from_driver_age.call_count == 1
    assert utils_mock.print_parking_created.call_count == 1
    assert utils_mock.print_slot_nums_or_regno.call_count == 1


@patch("parking_manager.main.utils")
@patch("parking_manager.main.SlotsManager")
@patch("parking_manager.main.print")
@patch("parking_manager.main.get_commands_from_file")
@patch("parking_manager.main.input")
def test_main_command_type_leave_vehicle(input_mock, get_commands_mock, print_mock, slots_manager_mock, utils_mock):
    input_mock.return_value = "xyz.txt"
    get_commands_mock.return_value = [["Create_parking_lot", "11"], ["Leave", "11"]]
    slots_manager_obj = MagicMock()
    slots_manager_mock.return_value = slots_manager_obj

    output = main.main()

    assert output is None
    assert slots_manager_mock.call_count == 1
    assert slots_manager_obj.leave_vehicle.call_count == 1
    assert utils_mock.print_parking_created.call_count == 1
    assert utils_mock.print_vehicle_leave.call_count == 1
