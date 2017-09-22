
lengte =eval((input('lengte: ')))
def lang_genoeg(lengte):
    if lengte >= 120:
        return('je bent lang genoeg om in de attractie te gaan')
    else:
        return('je bent te klein')

print(lang_genoeg(lengte))

