import random
import asyncio

iterations = 0
max_fitness = 0
max_fitness_items = []
barang = []
kategori = ["Kepentingan","Deadline","SDM","Requirements","Demand"]
# kategori = ["Deadline","SDM","Requirements"]

max_weight = 20
max_width = 30
max_humid = 20
sdm_available = 10
global_tracer_elitism = []
global_tracer_new_population = []
main_string = ""
trig = 1


fittests = []








def create(nilai):
    # temp = ''.join((random.choice(alp)) for x in range()) 
    temp = []
    
    for i in range(0,len(nilai)):
        temp.append(random.randint(0,1)) 
    
    return temp
        

def individual(created, nilai):
    
    return [created,calc_fitness(max_fitness,created, nilai)]
    
def mate(created1, created2, nilai):
    child_created = []
    
    for i in range(0,len(created1[0])):
        
        randomnumber = random.randint(0,100)/100
        
        if randomnumber < 0.45:
            child_created.append(created1[0][i]);
        
        elif randomnumber < 0.90:
            child_created.append(created2[0][i]);
        
        else:
            # child_created += random.choice(alp)
            if created1[0][i] == 1:
                child_created.append(0)
            else:
                child_created.append(1)
            
    return [child_created,calc_fitness(max_fitness,child_created, nilai)]
        
def set_max(value):
    max_fitness += 1
    
def calc_fitness(max_fit,created, nilai):
    global max_fitness
    global max_fitness_items
    global iterations
    global kategori

    fitness = 0
    deadline = 0
    sdm = 0
    requirements = 0
    importance = 0
    demand = 0
    # for i in range(0,4):
    for i in range(0,len(created)):
        if created[i] == 1:
            deadline += nilai[i][1]
            sdm += nilai[i][2]
            requirements += nilai[i][3]
            demand += nilai[i][4]
            importance += nilai[i][0]
            # deadline += nilai[i][0]
            # sdm += nilai[i][1]
            # requirements += nilai[i][2]
            
            
    
    try:
        fitness += 5 / deadline
    except ZeroDivisionError:
        fitness += 0
        
    try:
        fitness += 5 / sdm
    except ZeroDivisionError:
        fitness += 0
    
    try:
        fitness += 5 / requirements
    except ZeroDivisionError:
        fitness += 0
    
    fitness += importance
    
    if deadline > max_weight:
        fitness = 0
    if sdm > sdm_available:
        fitness = 0
    if requirements > max_humid:
        fitness = 0
    if max_fitness < fitness:
        max_fitness = fitness
        max_fitness_items = created
        iterations = 0
    return fitness
    




def start(projects, values):
        iterations = 0
        barang = []
        kategori = ["Kepentingan","Deadline","SDM","Requirements","Demand"]
        main_string = ""
        trig = 1
        nilai = []
        initial_population = []
        initial_population_fittest = []
        generations = []


        for i in projects:
            barang.append(i)
        
        for i in values:
            nilai.append(i)

        

        
        generation = 0

        for i in range(0,50):
            individ = individual(create(nilai), nilai)
            initial_population.append(individ)
            generations.append(individ[0])

            

        while(True):
            sort = sorted(initial_population, key=lambda x: x[1], reverse=True)
            new_population = []

            tracer_elitism = []
            tracer_new_population = []
            
            if iterations > 1000:
                trig = 2
                break
            
            for i in range(0,5):
                new_population.append(sort[i])
                tracer_elitism.append(sort[i])
                
            
            for i in range(0,45):
                
                rand = random.randint(0,25)
                created1 = sort[rand]
                rand = random.randint(0,25)
                created2 = sort[rand]
                created_child = mate(created1,created2, nilai)
                new_population.append(created_child)
                tracer_new_population.append(created_child)
            initial_population = new_population
            generations.append(sort[0][0])
            iterations += 1
            generation += 1
            global_tracer_elitism.append(tracer_elitism)
            global_tracer_new_population.append(tracer_new_population)

            print("Generation : "+str(generation), "| Iteration : "+str(iterations), "Value : "+str(sort[0][1]), "| Items : "+str(sort[0][0]))
            main_string = "Generation : "+str(generation), "| Iteration : "+str(iterations), "Value : "+str(sort[0][1]), "| Items : "+str(sort[0][0])
        return {
            "final":sorted(initial_population, key=lambda x: x[1], reverse=True)[0],
            "generations": generations
            }



def get_global_elitism():

    return "test"

# main()
