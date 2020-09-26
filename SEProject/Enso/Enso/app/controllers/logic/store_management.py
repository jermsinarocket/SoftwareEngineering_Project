from Enso.app.models.rating import Rating
from Enso.app.models.opening_hours import OpeningHours

def openingDays(store_id):
    opening_days_qcdict = OpeningHours.objects.filter(food_store = store_id).values('weekday')

    defaultDaysArr = [0,1,2,3,4,5,6]
    daysArr = []
    for day in opening_days_qcdict:
         daysArr.append(day['weekday'])
    return list(set(defaultDaysArr) - set(daysArr))


def openingHours(store_id):
    opening_days_qcdict = OpeningHours.objects.filter(food_store = store_id)
    opening_hours = {}
    for day in opening_days_qcdict:
        opening_hours[day.weekday] = {'lb' :str(day.from_hour), 'up': str(day.to_hour)}
    return opening_hours

def averageRatingCalculator(store_id):
    ratings_qdict = Rating.objects.filter(food_store = store_id)
    if(len(ratings_qdict) == 0):
        return 0,0
    else:
        allRatings = []
        for rating in ratings_qdict:
            allRatings.append(rating.rating)

        return len(allRatings),int(sum(allRatings)/len(allRatings))
