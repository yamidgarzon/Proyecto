def registrarPersonas():

# Formulario para solicitar datos
    individuo ={}
    
    
    nombre = input("Nombre completo:")
    individuo["nombre"]=nombre
    edad = int(input("edad:"))
    individuo["edad"]=edad
    ciudad = input("ciudad:")
    individuo["ciudad"]=ciudad
    genero=["Masculino","Femenino"]
    generoValido=False
    while generoValido!=True:
        print(genero)
        genero = input("cual su genero")
        if genero in genero:
            individuo["gernero"]=genero
            generoValido=True
    print(personas)
    print(individuo)
    return individuo


def main():

    cuantasPersonas=int(input( "Cuantas personas se vana a registrar?"))

                        # Registrando persoanas
    personas={}
    for i in range (0,cuantasPersonas):
     print("i",i)
     print(personas)
     personas[i]= registrarPersonas ()
                        
                        # Mostrar persoanas
    cuantasPersonas(personas)  
  
main()



