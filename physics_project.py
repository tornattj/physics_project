#   physics_project 2020

print("Welcome")
print("Commands = f to c, c to f, get force, get energy, get work, exit")

def main():

    def f_to_c(f_temp): # function to convert f to c
        f_input = int(input("Enter a temperature in Fahrenheit to convert to Celsius: ")) # f_temp = input
        f_temp = f_input
        f_output = (f_temp - 32) * 5/9
        print(str(f_temp) + " degrees Fahrenheit is equal to " + str(f_output) + " degrees Celsius.")
        main()

    def c_to_f(c_temp): # function to convert c to f
        c_input = int(input("Enter a temperature in Celsius to convert to Fahrenheit: ")) # c_temp = input
        c_temp = c_input
        c_output = (c_temp * 9/5) + 32
        print(str(c_temp) + " degrees Celsius is equal to " + str(c_output) + " degrees Fahrenheit.")
        main()

    def get_force (mass, acceleration): # function that multiplies mass * acceleration to equal force
        mass_input = int(input("Enter a value for mass: ")) # inputs = mass and acceleration
        acceleration_input = int(input("Enter a value for acceleration: "))
        mass = mass_input
        acceleration = acceleration_input
        force = mass * acceleration
        print(str(mass) + " multiplied by " + str(acceleration) + " equals " + str(force) + " Newtons.")
        main()

    def get_energy (mass): # function get_energy multiplies mass by c squared
        mass_input = int(input("Enter a value for mass: "))
        mass = mass_input
        energy = mass * 3*10**8
        print(str(mass) + " multiplied by the speed of light equals " + str(energy) + " kg/s.")
        main()

    def get_work(mass): # function that takes mass, acceleration, and distance to calculate work
        mass_input = int(input("Enter a value for mass: "))
        mass = mass_input
        acceleration_input = int(input("Enter a value for acceleration: "))
        acceleration = acceleration_input
        distance_input = int(input("Enter a value for distance: "))
        distance = distance_input
        force = mass * acceleration
        work = force * distance
        print(str(force) + " Newtons multiplied by " + str(distance) + " meters equals " + str(work) + " Newton-meters.")
        main()

    first_input = input("Enter a command: ") # if the user types f to c, it will return it to the f_to_c function

    if first_input=="f to c": # if the user types f to c, it will return it to the f_to_c function
        f_to_c(first_input)
    elif first_input=="c to f": # if the user types c to f, it will return it to the c_to_f function
        c_to_f(first_input)
    elif first_input=="get force":
        get_force(first_input, first_input)
    elif first_input=="get energy":
        get_energy(first_input)
    elif first_input=="get work":
        get_work(first_input)
    elif first_input=="exit":
        print("Goodbye")
        exit()
    else:
        main()

main()

def exit(): # function to exit the program
    print("")
