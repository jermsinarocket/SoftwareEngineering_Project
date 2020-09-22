from Enso.app.models.rating import Rating

def averageRatingCalculator(store_id):
    ratings_qdict = Rating.objects.filter(food_store = store_id)
    if(len(ratings_qdict) == 0):
        return 0,0
    else:
        allRatings = []
        for rating in ratings_qdict:
            allRatings.append(rating.rating)

        return len(allRatings),int(sum(allRatings)/len(allRatings))
