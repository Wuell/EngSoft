
from datetime import datetime
from AeroSys import *

# ==== INSTANCIANDO OBJETOS PRINCIPAIS ====
print("="*50)
print("🚀 SISTEMA DE GERENCIAMENTO DE COMPANHIA AÉREA".center(50))
print("="*50)

aeronave = Aeronave("Boeing 737", 5, [], "Disponível", ["1A", "1B", "1C", "2A", "2B"])
piloto = Piloto("João Souza", "Piloto", "P001", "senha123")
voo = Voo(101, 1, "Confirmado", aeronave,
          datetime(2025, 4, 10, 14, 30),
          datetime(2025, 4, 10, 17, 00),
          piloto)
piloto.current_flight = voo

atendente = Atendente("Carlos Lima", "Atendente", "A001", "senha456")
gerente = Gerente("Paula Torres", "Gerente", "G001", "senha789")

passageiros = [
    Passageiro("Lucas Silva", "123456789", "lucas@email.com"),
    Passageiro("Mariana Lima", "987654321", "mariana@email.com")
]

for i, passageiro in enumerate(passageiros):
    assento = voo.alocar_assento()
    atendente.check_in_passenger(passageiro, voo, assento, gate=f"C{i+1}")

for passageiro in passageiros:
    passageiro.check_flight_status()
    passageiro.check_boarding_pass()

gerente.generate_flight_report([voo])
gerente.generate_employee_report([atendente, piloto, gerente])

piloto.report_flight()
piloto.end_flight()
print(f"Status atualizado do voo {voo.number}: {voo.status}")
