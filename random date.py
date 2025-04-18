import random
import time

def getRandomDate (startDate,endDate):
    print("printing random number between ",startDate,"and",endDate)
    randomGenrotor = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate,dateFormat))
    endTime = time.mktime(time.strptime(endDate,dateFormat))

    randomtime = startTime + randomGenrotor *(endTime - startTime)
    randomDate = time.strftime(dateFormat,time.localtime(randomtime))
    return randomDate

print("random date = ",getRandomDate("1/1/2013","12/12/2015"))