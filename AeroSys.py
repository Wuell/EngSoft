from datetime import datetime

class Aeronave:
    instances = []

    def __init__(self, model: str, capacity: int, schedule: list, status: str, seats: list):
        # Modelo da aeronave
        self.model = model
        # Capacidade total de assentos
        self.capacity = capacity
        # Status atual da aeronave
        self.status = status
        # Agenda da aeronave
        self.schedule = schedule
        # Lista de assentos disponíveis
        self.seats = seats

    def programar_agenda(self, event: str):
        """Adiciona um evento à agenda da aeronave"""
        self.schedule.append(event)
        self.schedule.sort()

    def retirar_agenda(self, event: str):
        """Remove um evento da agenda"""
        self.schedule.remove(event)


class CartaoEmbarque:
    def __init__(self, id: int, assento: str, portao: str, horario_embarque: datetime):
        # Identificador único do cartão
        self.id = id
        # Assento reservado
        self.assento = assento
        # Portão de embarque
        self.portao = portao
        # Horário previsto para embarque
        self.horario_embarque = horario_embarque


class Voo:
    instances = []
    routes = {1: ("casa", "casa2")}

    def __init__(self, number: int, route: int, status: str, aircraft, time_depart: datetime, time_arrival: datetime, pilot):
        # Número identificador do voo
        self.number = number
        # Origem e destino definidos pelo índice de rota
        self.origin, self.destination = Voo.routes[route]
        # Status do voo
        self.status = status
        # Aeronave que fará o voo
        self.aeroplane = aircraft
        # Horário de partida e chegada
        self.time_depart = time_depart
        self.time_arrival = time_arrival
        # Capacidade total e assentos disponíveis herdados da aeronave
        self.capacity_total = aircraft.capacity
        self.capacity_avaliable = aircraft.capacity
        self.seats_avaliable = aircraft.seats
        # Piloto designado ao voo
        self.pilot = pilot
        Voo.instances.append(self)

    def alocar_assento(self):
        """Retorna o primeiro assento disponível e o remove da lista"""
        try:
            assento = self.seats_avaliable[0]
            self.seats_avaliable.pop(0)
        except:
            print("O voo não possui mais assentos disponíveis.")
            return -1
        return assento


class Passageiro:
    def __init__(self, name: str, document: str, email: str):
        # Dados do passageiro
        self.name = name
        self.document = document
        self.email = email
        # Atributos para armazenar o voo e o cartão de embarque
        self.flight = None
        self.boarding_pass = None

    def check_flight_status(self):
        """Mostra as informações do voo associado ao passageiro"""
        if self.flight:
            print(f"\nInformações do Voo {self.flight.number}:")
            print(f"- Origem: {self.flight.origin}")
            print(f"- Destino: {self.flight.destination}")
            print(f"- Status: {self.flight.status}")
            print(f"- Partida: {self.flight.time_depart.strftime('%H:%M')}")
            print(f"- Chegada: {self.flight.time_arrival.strftime('%H:%M')}")
        else:
            print("Passageiro não está associado a nenhum voo.")

    def check_boarding_pass(self):
        """Mostra o cartão de embarque do passageiro"""
        if self.boarding_pass:
            print(f"\nCartão de Embarque:")
            print(f"- ID: {self.boarding_pass.id}")
            print(f"- Assento: {self.boarding_pass.assento}")
            print(f"- Portão: {self.boarding_pass.portao}")
            print(f"- Horário de embarque: {self.boarding_pass.horario_embarque.strftime('%H:%M')}")
        else:
            print("Nenhum cartão de embarque disponível.")


class Funcionario:
    def __init__(self, name: str, role: str, employee_id: str, password: str):
        # Dados do funcionário
        self.name = name
        self.role = role
        self.employee_id = employee_id
        self.password = password
        self.entry_time = None
        self.exit_time = None

    def login(self, typed_password: str):
        """Autentica o funcionário com senha"""
        if typed_password == self.password:
            print(f"{self.name} fez login com sucesso.")
            return True
        else:
            print("Senha incorreta.")
            return False

    def clock_in(self):
        """Registra entrada"""
        self.entry_time = datetime.now()
        print(f"{self.name} registrou entrada às {self.entry_time.strftime('%H:%M:%S')}.")

    def clock_out(self):
        """Registra saída"""
        self.exit_time = datetime.now()
        print(f"{self.name} registrou saída às {self.exit_time.strftime('%H:%M:%S')}.")


class Gerente(Funcionario):
    def generate_flight_report(self, flights: list):
        """Gera relatório de todos os voos"""
        print("\nRelatório de Voos:")
        for flight in flights:
            pilot_name = flight.pilot.name if flight.pilot else "Não atribuído"
            print(f"- Voo {flight.number}: {flight.origin} → {flight.destination}")
            print(f"  Aeronave: {flight.aeroplane.model} | Status: {flight.status}")
            print(f"  Partida: {flight.time_depart.strftime('%H:%M')} | Chegada: {flight.time_arrival.strftime('%H:%M')}")
            print(f"  Piloto responsável: {pilot_name}")

    def generate_employee_report(self, employees: list):
        """Gera relatório com horários dos funcionários"""
        print("\nRelatório de Funcionários:")
        for emp in employees:
            entry = emp.entry_time.strftime('%H:%M:%S') if emp.entry_time else "Sem registro"
            exit_ = emp.exit_time.strftime('%H:%M:%S') if emp.exit_time else "Sem registro"
            print(f"- {emp.name} ({emp.role}) | Entrada: {entry} | Saída: {exit_}")

    def change_employee_role(self, employee, new_role: str):
        """Altera o cargo de um funcionário"""
        old_role = employee.role
        employee.role = new_role
        print(f"Cargo de {employee.name} alterado de '{old_role}' para '{new_role}'.")


class Atendente(Funcionario):
    def check_in_passenger(self, passenger, flight, seat: str, gate: str):
        """Faz check-in e gera cartão de embarque para o passageiro"""
        boarding_time = flight.time_depart
        boarding_pass = CartaoEmbarque(
            id=f"{flight.number}-{seat}",
            assento=seat,
            portao=gate,
            horario_embarque=boarding_time
        )
        passenger.flight = flight
        passenger.boarding_pass = boarding_pass
        print(f"{passenger.name} foi registrado no voo {flight.number} com assento {seat}.")


class Piloto(Funcionario):
    def __init__(self, name: str, role: str, employee_id: str, password: str):
        super().__init__(name, role, employee_id, password)
        self.current_flight = None

    def report_flight(self):
        """Mostra o voo atual do piloto"""
        if self.current_flight:
            print(f"\nRelatório de Voo do Piloto {self.name}:")
            print(f"- Voo: {self.current_flight.number}")
            print(f"- Origem: {self.current_flight.origin}")
            print(f"- Destino: {self.current_flight.destination}")
            print(f"- Aeronave: {self.current_flight.aeroplane.model}")
            print(f"- Status: {self.current_flight.status}")
            print(f"- Partida: {self.current_flight.time_depart.strftime('%H:%M')}")
        else:
            print(f"{self.name} não está associado a nenhum voo.")

    def end_flight(self):
        """Finaliza o voo atual e atualiza o status"""
        if self.current_flight:
            self.current_flight.status = "Finalizado"
            print(f"{self.name} finalizou o voo {self.current_flight.number}.")
            self.current_flight = None
        else:
            print(f"{self.name} não possui voo em andamento.")
