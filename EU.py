import datetime as dt

class Aeronave:
    instances = []

    def __init__(self, model, capacity, schedule, status):
        self.model = model
        self.capacity = capacity
        self.status = status
        self.schedule = schedule

    def programar_acao(self, event):
        self.schedule.append(event)
        self.schedule.sort()

class Cartao_Embarque:
    def __init__(self, id, assento, portao, horario_embarque):
        self.id = id
        self.assento = assento
        self.portao = portao
        self.horario_embarque = horario_embarque



class Voo:
    instances = []
    routes = {1: ("casa", "casa2")}

    def __init__(self, number, route, status, aircraft,
                 time_depart, time_arrival,  capacity):
        self.number = number
        self.origin, self.destination = Voo.routes[route]
        self.status = status
        self.aeroplane = aircraft
        self.time_depart = time_depart
        self.time_arrival = time_arrival
        self.capacity_total = capacity
        self.capacity_avaliable = capacity
        Voo.instances.append(self)

    def arrage_table(self):
        1+1

    def atualizar_status(self, new_status):
        self.status = new_status
