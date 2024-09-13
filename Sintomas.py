sintoma1=input("O paciente teve febre?(Sim/Não): ").lower()

sintoma2=input("O paciente teve tosse?(Sim/Não): ").lower()

if sintoma1== "sim" and sintoma2== "sim":

    print ("O Paciente está com uma possivel Gripe")

elif sintoma1 == "sim" and sintoma2 == "não":

    print ("Possivel infeccção viral")

else:

    print ("Consulte um médico")