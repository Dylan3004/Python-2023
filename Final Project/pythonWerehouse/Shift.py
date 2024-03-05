class Shift :
    def __init__(self,place_of_shift,shift_time,shift_date,shift_employer,shift_id,shift_list):
        self.place_of_shift = place_of_shift
        self.shift_time = shift_time
        self.shift_date = shift_date
        self.shift_employer = shift_employer
        self.shift_id = shift_id
        self.shift_list = shift_list

    def get_shift(self):
        print("Place of shift: " + self.place_of_shift)
        print("Shift time: " + self.shift_time)
        print("Shift date: " + self.shift_date)
        print("Shift employer: " + self.shift_employer)
        print("Shift id: " + str(self.shift_id))
        print("Shift list: " + str(self.shift_list))