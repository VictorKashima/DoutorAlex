import time
#Aprendendo estrutura with

while True:

    archive = open("Sim.txt", "w")
    archive.write("se ta doido")
    archive.close()

    archive = open("Sim.txt", "r")
    print(archive.read())
    archive.close()

    time.sleep(2)

    with open("Sim.txt", "w") as archive:
        archive.write("Se ta doido motorista")
    with open("Sim.txt", "r") as archive:
        print(archive.read())

    time.sleep(2)

    archive = open("Sim.txt", "w")
    archive.write("Ta maluco")
    archive.close()

    archive = open("Sim.txt", "r")
    print(archive.read())
    archive.close()

    time.sleep(2)