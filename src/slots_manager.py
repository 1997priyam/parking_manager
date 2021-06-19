from queue import PriorityQueue

class SlotsManager:
    def __init__(self, num_slots):
        self.available_slots = PriorityQueue(maxsize=num_slots)
        self.age_lookup = {}
        self.regno_lookup = {}
        self.slots_lookup = {}
        self.__initialize_available_slots(num_slots)

    def __initialize_available_slots(self, num_slots):
        for i in range(1, num_slots+1):
            self.available_slots.put(i)

    def park_vehicle(self, regno, driver_age):
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
        if driver_age in self.age_lookup:
            slot_regno_map = self.age_lookup[driver_age]
            return tuple(slot_regno_map.keys())
        return ()

    def get_slot_number_from_regno(self, regno):
        if regno in self.regno_lookup:
            return (self.regno_lookup[regno],)
        return ()

    def get_regno_from_driver_age(self, driver_age):
        if driver_age in self.age_lookup:
            slot_regno_map = self.age_lookup[driver_age]
            return tuple(slot_regno_map.values())
        return ()

    def leave_vehicle(self, slot):
        if slot in self.slots_lookup:
            regno, driver_age = self.slots_lookup[slot]
            del self.slots_lookup[slot]
            del self.regno_lookup[regno]
            del self.age_lookup[driver_age][slot]
            self.available_slots.put(slot)
            return (slot, regno, driver_age)
        return ()