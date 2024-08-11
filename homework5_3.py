class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
house1 = Building(6, 'жилое')
house2 = Building(6, 'нежилое')
print(house1 == house2)
        