import datetime

class Aeronave:
    instances = []

    def __init__(self, id : str, model : str, capacity : int, schedule : list, status : str, seats : list):
        Aeronave.instances.append(self)
        self.id = id
        self.model = model
        self.capacity = capacity
        self.status = status
        self.schedule = schedule
        self.seats = seats

    def adicionar_agenda(self, event : str):
        self.schedule.append(event)
        self.schedule.sort()
    
    def retirar_agenda(self, event : str):
        self.schedule.remove(event)


class Cartao_Embarque:
    def __init__(self, id : str, assento : str, portao : str, horario_embarque : datetime.time):
        self.id = id
        self.assento = assento
        self.portao = portao
        self.horario_embarque = horario_embarque


class Voo:
    instances = []
    routes = {1: ("casa", "casa2")}

    def __init__(self, number : int, route : int, status : str, aircraft : Aeronave,
                 time_depart : datetime.time, time_arrival : datetime.time, pilot : str):
        Voo.instances.append(self)
        self.number = number
        self.origin, self.destination = Voo.routes[route]
        self.status = status
        self.aeroplane = aircraft
        self.time_depart = time_depart
        self.time_arrival = time_arrival
        self.capacity_total = aircraft.capacity
        self.capacity_avaliable = aircraft.capacity
        self.seats_avaliable = aircraft.seats
        self.pilot = pilot
        
    def alocar_assento(self)->str:
        if len(self.seats_avaliable) == 0:
            print("O voo nao possui mais assentos disponiveis.")
            exit()

        assento = self.seats_avaliable[0]
        self.seats_avaliable.pop(0)
        return assento
    

