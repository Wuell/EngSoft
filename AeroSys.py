from datetime import datetime

class Aeronave:
    instances = []

    def __init__(self, model, capacity, schedule, status):
        self.model = model
        self.capacity = capacity
        self.status = status
        self.schedule = schedule

    def schedule_action(self, event):
        self.schedule.append(event)
        self.schedule.sort()


class CartaoEmbarque:
    def __init__(self, boarding_id, seat, gate, boarding_time):
        self.boarding_id = boarding_id
        self.seat = seat
        self.gate = gate
        self.boarding_time = boarding_time


class Voo:
    instances = []
    routes = {1: ("São Paulo", "Rio de Janeiro")}

    def __init__(self, number, route, status, aircraft,
                 departure_time, arrival_time, capacity):
        self.number = number
        self.origin, self.destination = Voo.routes[route]
        self.status = status
        self.aircraft = aircraft
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.capacity_total = capacity
        self.capacity_available = capacity
        Voo.instances.append(self)

    def arrange_table(self):
        pass  # implementar futuramente

    def update_status(self, new_status):
        self.status = new_status


class Passageiro:
    def __init__(self, name, document, email):
        self.name = name
        self.document = document
        self.email = email
        self.flight = None
        self.boarding_pass = None

    def check_in(self, flight, seat, gate):
        self.flight = flight
        boarding_time = flight.departure_time
        self.boarding_pass = CartaoEmbarque(
            boarding_id=f"{flight.number}-{seat}",
            seat=seat,
            gate=gate,
            boarding_time=boarding_time
        )
        print(f"{self.name} realizou o check-in no voo {flight.number}.")

    def check_flight_status(self):
        if self.flight:
            print(f"\n Informações do Voo {self.flight.number}:")
            print(f"- Origem: {self.flight.origin}")
            print(f"- Destino: {self.flight.destination}")
            print(f"- Status: {self.flight.status}")
            print(f"- Partida: {self.flight.departure_time.strftime('%H:%M')}")
            print(f"- Chegada: {self.flight.arrival_time.strftime('%H:%M')}")
        else:
            print("Passageiro não está associado a nenhum voo.")

    def check_boarding_pass(self):
        if self.boarding_pass:
            print(f"\n Cartão de Embarque:")
            print(f"- ID: {self.boarding_pass.boarding_id}")
            print(f"- Assento: {self.boarding_pass.seat}")
            print(f"- Portão: {self.boarding_pass.gate}")
            print(f"- Horário de embarque: {self.boarding_pass.boarding_time.strftime('%H:%M')}")
        else:
            print("Nenhum cartão de embarque disponível.")


class Funcionario:
    def __init__(self, name, role, employee_id, password):
        self.name = name
        self.role = role
        self.employee_id = employee_id
        self.password = password
        self.entry_time = None
        self.exit_time = None

    def login(self, typed_password):
        if typed_password == self.password:
            print(f"{self.name} fez login com sucesso.")
            return True
        else:
            print("Senha incorreta.")
            return False

    def clock_in(self):
        self.entry_time = datetime.now()
        print(f"{self.name} registrou entrada às {self.entry_time.strftime('%H:%M:%S')}.")

    def clock_out(self):
        self.exit_time = datetime.now()
        print(f"{self.name} registrou saída às {self.exit_time.strftime('%H:%M:%S')}.")


class Gerente(Funcionario):
    def generate_flight_report(self, flights):
        print("\n Relatório de Voos:")
        for flight in flights:
            print(f"- Voo {flight.number}: {flight.origin} → {flight.destination} | "
                  f"{flight.status} | Partida: {flight.departure_time.strftime('%H:%M')}")

    def generate_employee_report(self, employees):
        print("\n Relatório de Funcionários:")
        for emp in employees:
            entry = emp.entry_time.strftime('%H:%M:%S') if emp.entry_time else "Sem registro"
            exit_ = emp.exit_time.strftime('%H:%M:%S') if emp.exit_time else "Sem registro"
            print(f"- {emp.name} ({emp.role}) | Entrada: {entry} | Saída: {exit_}")

    def change_employee_role(self, employee, new_role):
        old_role = employee.role
        employee.role = new_role
        print(f"Cargo de {employee.name} alterado de '{old_role}' para '{new_role}'.")

class Atendente(Funcionario):
    def check_in_passenger(self, passenger, flight, seat, gate):
        boarding_time = flight.departure_time
        boarding_pass = CartaoEmbarque(
            boarding_id=f"{flight.number}-{seat}",
            seat=seat,
            gate=gate,
            boarding_time=boarding_time
        )
        passenger.flight = flight
        passenger.boarding_pass = boarding_pass
        print(f"{passenger.name} foi registrado no voo {flight.number} com assento {seat}.")
