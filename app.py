from flask import Flask, current_app, jsonify, request
import gerechten

# static_url_path is de pad die in url zichtbaar is voor static
# static_folder="static" is de folder static
app = Flask(__name__, static_url_path="", static_folder="static")


@app.route('/')
@app.route('/view1')
@app.route('/view2')
@app.route('/view3')
def index():
    return current_app.send_static_file('index.html')


def obj_dict(obj):
    return obj.__dict__


@app.route('/get_unregistered')
def getUnregistered():
    return jsonify(gerechten.gerechtenListToJson(gerechten.unregistered))


@app.route('/deny_gerecht', methods=['POST'])
def denyGerecht():
    # Haal gerechtsnaam uit de post parameters (formulier veld)
    gerechtsNaam = request.form['gerecht']
    # Gerecht verwijderd?
    verwijderd = False

    # Zoek voor gerechten met deze naam
    for gerecht in gerechten.unregistered:
        # Als gerecht met hetzelfde naam bestaat; Verwijder het
        if (gerecht.getNaam() == gerechtsNaam):
            gerechten.unregistered.remove(gerecht)
            verwijderd = True
            break
    return '{"success": ' + str(verwijderd) + '}'

@app.route('/register_gerecht', methods=['POST'])
def registerGerecht():
    # Haal gerechtsnaam uit de post parameters (formulier veld)
    gerechtsNaam = request.form['gerecht']
    # Gerecht verplaatst?
    verplaatst = False

    # Zoek voor gerechten met deze naam
    for gerecht in gerechten.unregistered:
        # Als gerecht met hetzelfde naam bestaat; verplaats het naar registered
        if (gerecht.getNaam() == gerechtsNaam):
            gerechten.unregistered.remove(gerecht)
            gerechten.registered.append(gerecht)
            verplaatst = True
            break

    return '{"success": ' + str(verplaatst) + '}'

@app.route('/get_registered')
def getRegistered():
    return jsonify(gerechten.gerechtenListToJson(gerechten.registered))


@app.route('/unregister_gerecht', methods=['POST'])
def unregisterGerecht():
    # Haal gerechtsnaam uit de post parameters (formulier veld)
    gerechtsNaam = request.form['gerecht']
    # Gerecht verplaatst?
    verplaatst = False

    # Zoek voor gerechten met deze naam
    for gerecht in gerechten.registered:
        # Als gerecht met hetzelfde naam bestaat; verplaats het naar unregistered
        if (gerecht.getNaam() == gerechtsNaam):
            gerechten.registered.remove(gerecht)
            gerechten.unregistered.append(gerecht)
            verplaatst = True
            break

    return '{"success": ' + str(verplaatst) + '}'
