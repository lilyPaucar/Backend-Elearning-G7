# crear una clase Persona en la cual se guarden su nombre, fecha_nacimiento, nacionalidad, dni, ademas tambien una clase Alumno y una clase Docente en la cual el alumno , a diferencia del docente, tenga una serie de cursos matriculados, y el docente por su parte tenga un numero del seguro social y su cuenta de la CTS. En base a lo visto de herencia crear las clases y ademas ver si hay algun atributo o metodo que deba de ser privado.

class Persona:
    def __init__(self, nombre,fecha_nacimiento,nacionalidad,dni):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad=nacionalidad
        self.dni=dni
   
    def info(self):
        return {
            'nombre': self.nombre,
            'fecha_de_nacimiento': self.fecha_nacimiento,            
            'nacionalidad':self.nacionalidad,
            'dni':self.dni
        }
class profesor(Persona):
    def __init__(self, nombre,fecha_nacimiento,nacionalidad,dni,cts,seg_social):
       
        self.cts = cts
        self.__seg = seg_social
        super().__init__(nombre,fecha_nacimiento,nacionalidad,dni)
       
    def info(self):
        infoDocente = super().info()
        data={
            
            'cts':self.cts
        }
        return {**data, **infoDocente
        }
    def segsocial(self):
        print(self.__seg)

class Alumno(Persona):
    def __init__(self, nombre,fecha_nacimiento,nacionalidad,dni,curso):
        self.curso=["matematica","comunicacion"]
        super().__init__(nombre,fecha_nacimiento,nacionalidad,dni)
        
    def info(self):
        infoDocente = super().info()
        data={
            
            'cursos':self.curso
        }
        return {**data, **infoDocente
        }

       

print("------DATOS DOCENTE-----") 
docente=profesor("andres","12/07/98","peruano","70885641","56789","3")
print(docente.info())
docente.segsocial()
print("------DATOS ALUMNOS-----") 
alum=Alumno("andres","12/07/98","peruano","70885641","")
print(alum.info())
