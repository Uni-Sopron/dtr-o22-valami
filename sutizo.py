cookies = [
    {
        "name": "Barackos pite",
        "baking_time": 60,
        "price": 8,
        "deadline": 2,
        "isDone":False
    },
        {
        "name": "Hóvirág lepény",
        "baking_time": 40,
        "price": 7,
        "deadline": 1,
        "isDone":False
    },
        {
        "name": "Hóvirág lepény",
        "baking_time": 40,
        "price": 7,
        "deadline": 1,
        "isDone":False
    },
        {
        "name": "Kis Peti kedvence",
        "baking_time": 70,
        "price": 13,
        "deadline": 4,
        "isDone":False
    },
        {
        "name": "Leveles mézes",
        "baking_time": 20,
        "price": 7,
        "deadline": 2,
        "isDone":False
    },
        {
        "name": "Kávé szelet",
        "baking_time": 25,
        "price": 5,
        "deadline": 5,
        "isDone":False
    },
        {
        "name": "Jazz szelet",
        "baking_time": 30,
        "price": 6,
        "deadline": 4,
        "isDone":False
    },
        {
        "name": "Jazz szelet",
        "baking_time": 30,
        "price": 6,
        "deadline": 3,
        "isDone":False
    },
        {
        "name": "Ezüst álom",
        "baking_time": 35,
        "price": 3,
        "deadline": 5,
        "isDone":False
    },
        {
        "name": "Kókusz fókusz",
        "baking_time": 45,
        "price": 7,
        "deadline": 2,
        "isDone":False
    },
        {
        "name": "Beállsz-elet",
        "baking_time": 50,
        "price": 7,
        "deadline": 1,
        "isDone":False
    },
]
maxDeadlineDay = 6 #Hilda has max 5 days to bake all the cookies, but it is used exclusively
maxBakingTimePerDay = 240 #in minutes
solution=[]

def sumBakingTime(dayList):
    sum = 0
    for i in range(len(dayList)):
        if(dayList[i]):
            sum=sum+dayList[i]["baking_time"]
    return sum


def countForActualDeadLineDay(actualDeadlineDay):
    print("Counting for deadline day: "+str(actualDeadlineDay))
    solution.append([])
    #first approach is to bake everything on deadline day
    for i in range(len(cookies)):
        actualCookie = cookies[i]
        if(actualCookie["deadline"]==actualDeadlineDay and sumBakingTime(solution[actualDeadlineDay-1])+actualCookie["baking_time"]<=maxBakingTimePerDay):
            if(len(solution)<=actualDeadlineDay):
                solution.append([])
            solution[actualDeadlineDay].append(actualCookie)
    actualDeadlineDay = actualDeadlineDay +1

def solve_problem():
    for i in range(1, maxDeadlineDay):
        countForActualDeadLineDay(i)
    print("\n\nThe solution is:")
    for i in range(1, maxDeadlineDay):
        print("\nCookies for day "+str(i))
        print("Total baking time: "+str(sumBakingTime(solution[i])))
        print("Cookies:")
        for cookie in solution[i]:
            print(cookie["name"]+", "+str(cookie["baking_time"]))

solve_problem()