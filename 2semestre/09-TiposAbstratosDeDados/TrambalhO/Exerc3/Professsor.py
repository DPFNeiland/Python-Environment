

class Professor:

    def __init__(
            self, 
            nome: str,
            numero_aulas_semanais: float,
            hora_aula: float,
            titulo: str
        ):
        self.nome = nome    
        self.numero_aulas_semanais = numero_aulas_semanais
        self.hora_aula = hora_aula
        self.titulo = titulo


    def calcular_salario_base(self) -> float:
        salario_base = self.numero_aulas_semanais*4.5*self.hora_aula
        
        if self.titulo.lower() == "mestre":
            salario_base*=1.085

        elif self.titulo.lower() == "doutor":
            salario_base*=1.12
        
        return salario_base

    def calcular_adicional_hora(self) -> float:

        return self.calcular_salario_base()*0.05
    
    def calcular_descanso_remunerado(self) ->  float:

        return (self.calcular_adicional_hora() + self.calcular_salario_base()) * 1 / 6
    
    def calcular_salario(self):
        sal_base = self.calcular_salario_base()
        adicional = self.calcular_adicional_hora()
        descanso = self.calcular_descanso_remunerado()

        return sal_base + adicional + descanso