import gerechtenModel

# Bestaande gerechten lijst vullen
unregistered = [
    gerechtenModel.Gerecht("Sashimi", "Sushi", 1.99),
    gerechtenModel.Gerecht("Kaviaar", "Viseieren", 49.99),
    gerechtenModel.Gerecht("Grilled chicken in soy sauce", "Grill", 49.99),
    gerechtenModel.Gerecht("Sake", "Alcohol", 49.99),
    gerechtenModel.Gerecht("Tako Maki", "Sushi", 49.99)
]
registered = []


def gerechtenListToJson(input):
    response = []
    for gerecht in input:
        response.append(gerecht.serialize())
    return response
