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
            {
        "name": "Jazz szelet (ajándék)",
        "baking_time": 30,
        "price": "present",
        "deadline": 3,
        "isDone":False
    },
            {
        "name": "Jazz szelet (ajándék)",
        "baking_time": 30,
        "price": "present",
        "deadline": 3,
        "isDone":False
    },
        {
        "name": "Beállsz-elet (ajándék)",
        "baking_time": 50,
        "price": "present",
        "deadline": 3,
        "isDone":False
    },
                {
        "name": "Jazz szelet (extra)",
        "baking_time": 60,
        "price": 9,
        "deadline": 1,
        "isDone":False
    },
                    {
        "name": "Jazz szelet (extra)",
        "baking_time": 60,
        "price": 9,
        "deadline": 1,
        "isDone":False
    },
]
maxDeadlineDay = 6 #Hilda has max 5 days to bake all the cookies, but it is used exclusively
maxBakingTimePerDay = 240 #in minutes
solution=[]
HildasPTODay = 3

def sumBakingTime(dayList):
    sum = 0
    for i in range(len(dayList)):
        if(dayList[i]):
            sum=sum+dayList[i]["baking_time"]
    return sum

def countForPTO(PTODay):
    for i in range(1, PTODay):
        for cookieIndex in range(len(cookies)):
            actualCookie = cookies[cookieIndex]
            if(not actualCookie["isDone"] and actualCookie["deadline"]==PTODay and sumBakingTime(solution[i])+actualCookie["baking_time"]<=maxBakingTimePerDay):
                if(len(solution)<=i):
                    solution.append([])
                solution[i].append(actualCookie)
                cookies[cookieIndex]["isDone"]=True
            else:
                if(actualCookie["deadline"]==i and i == PTODay-1 and not sumBakingTime(solution[i])+actualCookie["baking_time"]<=maxBakingTimePerDay):
                    print("A(z) "+actualCookie["name"]+" sütit nem tudom bevállalni")

def sumIncome(listOfCookies):
    sum = 0
    for cookie in listOfCookies:
        if(cookie["price"] != "present"):
            sum=sum+cookie["price"]
    return sum

def createListBasedOnTheOther(paramList):
    tempList = []
    for thing in paramList:
        tempList.append(thing)
    return tempList
    
def createListBasedOnTheOtherButRemoveOne(paramList,index):
    tempList = []
    for i in range(len(paramList)):
        if(i!=index):
            tempList.append(paramList[i])
    return tempList

def correction(listOfCookiesThatDay, actualCookie):
    possibleCookies = listOfCookiesThatDay
    possibleCookies.append(actualCookie)
    possibleSolution = createListBasedOnTheOther(possibleCookies)
    maxIncome = 0
    realSolution = createListBasedOnTheOther(possibleCookies)
    for i in range (len(possibleCookies)):
        possibleSolution=createListBasedOnTheOtherButRemoveOne(possibleCookies,i)
        if(sumBakingTime(possibleSolution)<=maxBakingTimePerDay and sumIncome(possibleSolution)>maxIncome):
            maxIncome=sumIncome(possibleSolution)
            realSolution = createListBasedOnTheOther(possibleSolution)
    print("Korrigálva:")
    print(maxIncome)
    print(realSolution)
    return realSolution

    

def countForActualDeadLineDay(actualDeadlineDay):
    print("Counting for deadline day: "+str(actualDeadlineDay))
    if(actualDeadlineDay==HildasPTODay):
        countForPTO(HildasPTODay)
    else:
        solution.append([])
        #first approach is to bake everything on deadline day
        for i in range(len(cookies)):
            actualCookie = cookies[i]
            if(len(solution)<=actualDeadlineDay):
                solution.append([])
            if(not actualCookie["isDone"] and actualCookie["deadline"]==actualDeadlineDay and sumBakingTime(solution[actualDeadlineDay])+actualCookie["baking_time"]<=maxBakingTimePerDay):
                solution[actualDeadlineDay].append(actualCookie)
                cookies[i]["isDone"]=True
            else:
                if(actualCookie["deadline"]==actualDeadlineDay and not sumBakingTime(solution[actualDeadlineDay])+actualCookie["baking_time"]<=maxBakingTimePerDay):
                    print("A(z) "+actualCookie["name"]+" sütit nem tudom bevállalni, korrigálok")
                    solution[actualDeadlineDay] = correction(solution[actualDeadlineDay], actualCookie)

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