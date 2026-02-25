# Membuat sebuah kelas
#Grand Prix

class GetToKnowMe:
    def __init__(self, name, rider, number):
        self.name = name
        self.rider = rider
        self.number = number

    def perkenalan_diri(self):
        print(f"You can call me {self.name},  my favorite rider is {self.rider}")

    def change_rider(self, change_rider):
        self.rider = change_rider
        print(f"My current favorite rider is {self.rider}")

    def circuit(self):
        print(f"His Fav circuit is {self.number}")

GetToKnowMeFanOne = GetToKnowMe("Amanda", "Marquez", "93")
GetToKnowMeFanTwo = GetToKnowMe("Izan", "Bagnaia", "63")
GetToKnowMeFanThree= GetToKnowMe("Fernandes", "Quartararo", "20")

print(GetToKnowMeFanOne.name)
print(GetToKnowMeFanOne.number)
GetToKnowMeFanOne.perkenalan_diri()
GetToKnowMeFanOne.change_rider("Aldeguer")
GetToKnowMeFanOne.perkenalan_diri
