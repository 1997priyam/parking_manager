"""
This module is responsible for handling all the command type queries related to the
parking lot.
"""

from queue import PriorityQueue

class SlotsManager:
    """
    This class manages the availability of slots, and handles different types of
    get queries. It maintains different data strucutres internally to handle the 
    allocation and deallocation of slots.

    Attributes:
        available_slots: Priority queue to get the available slot.
        age_lookup: A dictionary to lookup slots and reg no from age
        regno_lookup: A dictionary to lookup slot from reg no.
        slots_lookup: A dictionary to lookup reg no and driver age from the slot.
    """
    def __init__(self, num_slots):
        """
        Constructor to initialize the slots manager object
        """
        self.available_slots = PriorityQueue(maxsize=num_slots)
        self.age_lookup = {}
        self.regno_lookup = {}
        self.slots_lookup = {}
        self.__initialize_available_slots(num_slots)

    def __initialize_available_slots(self, num_slots):
        """
        It adds all the available slots into the priority queue initially.

        Args:
            num_slots: Number of slots to be added into Pqueue.
        """
        for i in range(1, num_slots+1):
            self.available_slots.put(i)

    def park_vehicle(self, regno, driver_age):
        """
        This functions parks and allocates an available slot to the car.

        Args:
            regno: Registration number of the car
            driver_age: The age of the driver

        Returns:
            -1: If no slot is available.
            -2: If the car with a reg no is already parked.
            slotNumber: If the slot is allocated successfully
        """
        if self.available_slots.empty():
            return -1
        
        if regno in self.regno_lookup:
            return -2

        slot = self.available_slots.get()
        self.regno_lookup[regno] = slot
        self.slots_lookup[slot] = [regno, driver_age]
        
        if driver_age in self.age_lookup:
            self.age_lookup[driver_age][slot] = regno
        else:
            slot_regno_map = {}
            slot_regno_map[slot] = regno
            self.age_lookup[driver_age] = slot_regno_map

        return slot

    def get_slot_numbers_from_driver_age(self, driver_age):
        """
        This functions gets all the slot numbers of cars from driver age

        Args:
            driver_age: The age of the driver

        Returns:
            Empty tuple if no slots are found.
            A tuple with values if slots are found.
        """
        if driver_age in self.age_lookup:
            slot_regno_map = self.age_lookup[driver_age]
            return tuple(slot_regno_map.keys())
        return ()

    def get_slot_number_from_regno(self, regno):
        """
        This functions gets the slot number of car from its reg no.

        Args:
            regno: The registration of the car

        Returns:
            Empty tuple if no slots is found.
            A tuple with slot, if found.
        """
        if regno in self.regno_lookup:
            return (self.regno_lookup[regno],)
        return ()

    def get_regno_from_driver_age(self, driver_age):
        """
        This functions gets all the slot numbers of cars from reg no

        Args:
            driver_age: The age of the driver

        Returns:
            Empty tuple is no slots are found.
            A tuple with values if slots are found.
        """
        if driver_age in self.age_lookup:
            slot_regno_map = self.age_lookup[driver_age]
            return tuple(slot_regno_map.values())
        return ()

    def leave_vehicle(self, slot):
        """
        This functions deallocates the slot to make it available for
        other cars.

        Args:
            slot: Slot number to deallocate

        Returns:
            Empty tuple if slot is already vacant.
            A tuple with values(slot, regno, driver_age) if its occupied.
        """
        if slot in self.slots_lookup:
            regno, driver_age = self.slots_lookup[slot]
            del self.slots_lookup[slot]
            del self.regno_lookup[regno]
            del self.age_lookup[driver_age][slot]
            self.available_slots.put(slot)
            return (slot, regno, driver_age)
        return ()