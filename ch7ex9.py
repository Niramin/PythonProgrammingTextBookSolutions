def main():
    vehicles={'Bicycle','Scooter','Car','Bike','Truck','Bus','Rickshaw'}
    heavyVehicles={'Truck','Bus'}
    lightVehicles={'Rickshaw','Scooter','Bike','Bicycle'}
    #questions
    lytVehicles=vehicles-heavyVehicles
    print(lytVehicles)
    hvyVehicles=vehicles-lightVehicles
    print(hvyVehicles)
    avgWeightVehicles=lytVehicles & hvyVehicles
    print(avgWeightVehicles)
    transport=lightVehicles | heavyVehicles
    print(transport)
    transport.add('Car')
    print(transport)
    for i in vehicles:
        print(i)
    print(len(vehicles))
    print(min(vehicles))
    print(set.union(vehicles,lightVehicles,heavyVehicles))

if __name__=="__main__":
    main()