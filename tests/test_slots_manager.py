from unittest.mock import MagicMock, patch, Mock
import pytest
from parking_manager.src.slots_manager import SlotsManager


@pytest.fixture(scope="module")
def slot_manager_obj():
    obj = SlotsManager(6)
    yield obj
    del obj

def test_park_vehicle_no_empty_slot(slot_manager_obj):
    slot_manager_obj.available_slots.empty = MagicMock(return_value=True)
    regno = "KA-01-HH-1234"
    driver_age = "21"

    output = slot_manager_obj.park_vehicle(regno, driver_age)

    assert output == -1


def test_park_vehicle_empty_slot_available_driver_age_not_in_lookup(slot_manager_obj):
    slot_manager_obj.available_slots.empty = MagicMock(return_value=False)
    slot_manager_obj.available_slots.get = MagicMock(return_value=1)
    regno = "KA-01-HH-1234"
    driver_age = "21"

    output = slot_manager_obj.park_vehicle(regno, driver_age)

    assert output == 1
    assert regno in slot_manager_obj.regno_lookup
    assert slot_manager_obj.regno_lookup[regno] == 1
    assert 1 in slot_manager_obj.slots_lookup
    assert type(slot_manager_obj.slots_lookup[1]) == list
    assert slot_manager_obj.slots_lookup[1] == ["KA-01-HH-1234", "21"]
    assert driver_age in slot_manager_obj.age_lookup
    assert type(slot_manager_obj.age_lookup[driver_age]) == dict
    assert slot_manager_obj.age_lookup[driver_age] == {1: regno}


def test_park_vehicle_empty_slot_available_driver_age_in_lookup(slot_manager_obj):
    slot_manager_obj.available_slots.empty = MagicMock(return_value=False)
    slot_manager_obj.available_slots.get = MagicMock(return_value=2)
    regno = "KA-01-HH-1235"
    driver_age = "21"

    output = slot_manager_obj.park_vehicle(regno, driver_age)

    assert output == 2
    assert regno in slot_manager_obj.regno_lookup
    assert slot_manager_obj.regno_lookup[regno] == 2
    assert 2 in slot_manager_obj.slots_lookup
    assert type(slot_manager_obj.slots_lookup[2]) == list
    assert slot_manager_obj.slots_lookup[2] == [regno, "21"]
    assert driver_age in slot_manager_obj.age_lookup
    assert type(slot_manager_obj.age_lookup[driver_age]) == dict
    assert slot_manager_obj.age_lookup[driver_age] == {1: "KA-01-HH-1234", 2: regno}


def test_park_vehicle_empty_slot_available_car_already_parked(slot_manager_obj):
    slot_manager_obj.available_slots.empty = MagicMock(return_value=False)
    slot_manager_obj.available_slots.get = MagicMock(return_value=1)
    regno = "KA-01-HH-1234"
    driver_age = "21"

    output = slot_manager_obj.park_vehicle(regno, driver_age)

    assert output == -2


def test_get_slot_numbers_from_driver_age_not_present(slot_manager_obj):
    driver_age = "18"

    output = slot_manager_obj.get_slot_numbers_from_driver_age(driver_age)

    assert output == ()


def test_get_slot_numbers_from_driver_age_is_present(slot_manager_obj):
    driver_age = "21"

    output = slot_manager_obj.get_slot_numbers_from_driver_age(driver_age)

    assert output == (1, 2)


def test_get_slot_number_from_regno_not_present(slot_manager_obj):
    regno = "PB-01-HH-1234"

    output = slot_manager_obj.get_slot_number_from_regno(regno)

    assert output == ()


def test_get_slot_number_from_regno_is_present(slot_manager_obj):
    regno = "KA-01-HH-1234"

    output = slot_manager_obj.get_slot_number_from_regno(regno)

    assert output == (1,)


def test_get_regno_from_driver_age_not_present(slot_manager_obj):
    driver_age = "18"

    output = slot_manager_obj.get_regno_from_driver_age(driver_age)

    assert output == ()


def test_get_regno_from_driver_age_is_present(slot_manager_obj):
    driver_age = "21"

    output = slot_manager_obj.get_regno_from_driver_age(driver_age)

    assert output == ("KA-01-HH-1234", "KA-01-HH-1235")


def test_leave_vehicle_slot_already_vacant(slot_manager_obj):
    slot = 3

    output = slot_manager_obj.leave_vehicle(slot)

    assert output == ()


def test_leave_vehicle_slot_is_occupied(slot_manager_obj):
    slot = 2
    regno = "KA-01-HH-1235"
    driver_age = "21"
    slot_manager_obj.available_slots = MagicMock()

    output = slot_manager_obj.leave_vehicle(slot)

    assert output == (2, regno, driver_age)
    assert slot not in slot_manager_obj.slots_lookup
    assert regno not in slot_manager_obj.regno_lookup
    assert slot not in slot_manager_obj.age_lookup[driver_age]
    assert slot_manager_obj.available_slots.put.call_count == 1
