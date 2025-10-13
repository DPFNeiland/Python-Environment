class Atom:
    def __init__(self, protons, neutrons, electrons):
        self.protons = protons
        self.neutrons = neutrons
        self.electrons = electrons

    def element_symbol(self):
        periodic_table = {
            1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N", 8: "O", 9: "F", 10: "Ne"
            # Adicione mais elementos conforme necessário
        }
        return periodic_table.get(self.protons, "Desconhecido")

    def atomic_mass(self):
        return self.protons + self.neutrons

    def charge(self):
        return self.protons - self.electrons

    def display_info(self):
        print(f"Elemento: {self.element_symbol()}")
        print(f"Prótons: {self.protons}")
        print(f"Nêutrons: {self.neutrons}")
        print(f"Elétrons: {self.electrons}")
        print(f"Massa Atômica: {self.atomic_mass()}")
        print(f"Carga: {self.charge()}")

# Exemplo de uso
if __name__ == "__main__":
    print("Simulador de Modelo Atômico")
    protons = int(input("Digite o número de prótons: "))
    neutrons = int(input("Digite o número de nêutrons: "))
    electrons = int(input("Digite o número de elétrons: "))

    atom = Atom(protons, neutrons, electrons)
    atom.display_info()