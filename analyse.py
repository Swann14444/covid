from pylab import *
from collections import OrderedDict
lorraine = ["54","55","57","88"]
file = open("dataCovid.csv", "r")
valuesHospi = OrderedDict()
valuesRea = OrderedDict()
valuesDc = OrderedDict()
valuesHospi_lorraine = OrderedDict()
valuesRea_lorraine = OrderedDict()
valuesDc_lorraine = OrderedDict()
file.readline()

for line in file:
    parsedLine = line.split(";")
    try:
      valuesHospi[parsedLine[1]] += int(parsedLine[2])
      valuesRea[parsedLine[1]] += int(parsedLine[3])
      valuesDc[parsedLine[1]] += int(parsedLine[4])

    except:
      valuesHospi[parsedLine[1]] = int(parsedLine[2])
      valuesRea[parsedLine[1]] = int(parsedLine[3])
      valuesDc[parsedLine[1]] = int(parsedLine[4])
    if parsedLine[0] in lorraine:
        print("ping")
        try:
            valuesHospi_lorraine[parsedLine[1]] += int(parsedLine[2])
            valuesRea_lorraine[parsedLine[1]] += int(parsedLine[3])
            valuesDc_lorraine[parsedLine[1]] += int(parsedLine[4])
        except:
            valuesHospi_lorraine[parsedLine[1]] = int(parsedLine[2])
            valuesRea_lorraine[parsedLine[1]] = int(parsedLine[3])
            valuesDc_lorraine[parsedLine[1]] = int(parsedLine[4])

def plot_week_mean_hospi():
    figure("Nouvelles admissions journalieres moyenne à l'hopital sur une semaine")
    x, y = zip(*valuesHospi.items())
    new_x = x[::7]
    new_y = [0] * len(new_x)
    for i in range(len(y)):
        # une semaine va de 0 à 6 modulo 7 (semaine de 7 à 13, 14 à 20 ...)
        # last_week_fix vaut dont 7/nombre de jour ecoulé sur la semaine en cours. Cela permet d'extrapolé les rea/hospi de la semaine en cours
        jours_ecoulé = 7 * (i / 7 - i // 7) + 1
        last__week_fix = 7 / jours_ecoulé if jours_ecoulé != 0 else 0

        new_y[int(i / 7)] += y[i]
    new_y[-1] = new_y[-1] * last__week_fix

    _ = matplotlib.pyplot.plot(new_x, new_y)
    ax = matplotlib.pyplot.gca()
    matplotlib.pyplot.xticks(rotation=90)
    for label in ax.get_xaxis().get_ticklabels()[::]:
        label.set_visible(False)
    for label in ax.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(True)


def plot_week_mean_rea():
    figure("Nouvelles admissions journalieres moyenne en reanimation sur une semaine")
    x, y = zip(*valuesRea.items())
    new_x = x[::7]
    new_y = [0] * len(new_x)
    for i in range(len(y)):
        # une semaine va de 0 à 6 modulo 7 (semaine de 7 à 13, 14 à 20 ...)
        # last_week_fix vaut dont 7/nombre de jour ecoulé sur la semaine en cours. Cela permet d'extrapolé les rea/hospi de la semaine en cours
        jours_ecoulé = 7 * (i / 7 - i // 7) + 1
        last__week_fix = 7 / jours_ecoulé if jours_ecoulé != 0 else 0

        new_y[int(i / 7)] += y[i]
    new_y[-1] = new_y[-1] * last__week_fix

    _ = matplotlib.pyplot.plot(new_x, new_y)
    ax = matplotlib.pyplot.gca()
    matplotlib.pyplot.xticks(rotation=90)
    for label in ax.get_xaxis().get_ticklabels()[::]:
        label.set_visible(False)
    for label in ax.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(True)


def plot_week_mean_dc():
    figure("Nouveaux déces moyen sur une semaine")
    x, y = zip(*valuesDc.items())
    new_x = x[::7]
    new_y = [0] * len(new_x)
    for i in range(len(y)):
        # une semaine va de 0 à 6 modulo 7 (semaine de 7 à 13, 14 à 20 ...)
        # last_week_fix vaut dont 7/nombre de jour ecoulé sur la semaine en cours. Cela permet d'extrapolé les rea/hospi de la semaine en cours
        jours_ecoulé = 7 * (i / 7 - i // 7) + 1
        last__week_fix = 7 / jours_ecoulé if jours_ecoulé != 0 else 0

        new_y[int(i / 7)] += y[i]
    new_y[-1] = new_y[-1] * last__week_fix

    _ = matplotlib.pyplot.plot(new_x, new_y)
    ax = matplotlib.pyplot.gca()
    matplotlib.pyplot.xticks(rotation=90)
    for label in ax.get_xaxis().get_ticklabels()[::]:
        label.set_visible(False)
    for label in ax.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(True)


def plot_week_mean_hospi_lorraine():
    figure("Nouvelles admissions journalieres moyenne à l'hopital sur une semaine lorraine")
    x, y = zip(*valuesHospi_lorraine.items())
    new_x = x[::7]
    new_y = [0] * len(new_x)
    for i in range(len(y)):
        # une semaine va de 0 à 6 modulo 7 (semaine de 7 à 13, 14 à 20 ...)
        # last_week_fix vaut dont 7/nombre de jour ecoulé sur la semaine en cours. Cela permet d'extrapolé les rea/hospi de la semaine en cours
        jours_ecoulé = 7 * (i / 7 - i // 7) + 1
        last__week_fix = 7 / jours_ecoulé if jours_ecoulé != 0 else 0

        new_y[int(i / 7)] += y[i]
    new_y[-1] = new_y[-1] * last__week_fix

    _ = matplotlib.pyplot.plot(new_x, new_y)
    ax = matplotlib.pyplot.gca()
    matplotlib.pyplot.xticks(rotation=90)
    for label in ax.get_xaxis().get_ticklabels()[::]:
        label.set_visible(False)
    for label in ax.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(True)


def plot_week_mean_rea_lorraine():
    figure("Nouvelles admissions journalieres moyenne en reanimation sur une semaine lorraine")
    x, y = zip(*valuesRea_lorraine.items())
    new_x = x[::7]
    new_y = [0] * len(new_x)
    for i in range(len(y)):
        # une semaine va de 0 à 6 modulo 7 (semaine de 7 à 13, 14 à 20 ...)
        # last_week_fix vaut dont 7/nombre de jour ecoulé sur la semaine en cours. Cela permet d'extrapolé les rea/hospi de la semaine en cours
        jours_ecoulé = 7 * (i / 7 - i // 7) + 1
        last__week_fix = 7 / jours_ecoulé if jours_ecoulé != 0 else 0

        new_y[int(i / 7)] += y[i]
    new_y[-1] = new_y[-1] * last__week_fix

    _ = matplotlib.pyplot.plot(new_x, new_y)
    ax = matplotlib.pyplot.gca()
    matplotlib.pyplot.xticks(rotation=90)
    for label in ax.get_xaxis().get_ticklabels()[::]:
        label.set_visible(False)
    for label in ax.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(True)


def plot_week_mean_dc_lorraine():
    figure("Nouveaux déces moyen sur une semaine lorraine")
    x, y = zip(*valuesDc_lorraine.items())
    new_x = x[::7]
    new_y = [0] * len(new_x)
    for i in range(len(y)):
        # une semaine va de 0 à 6 modulo 7 (semaine de 7 à 13, 14 à 20 ...)
        # last_week_fix vaut dont 7/nombre de jour ecoulé sur la semaine en cours. Cela permet d'extrapolé les rea/hospi de la semaine en cours
        jours_ecoulé = 7 * (i / 7 - i // 7) + 1
        last__week_fix = 7 / jours_ecoulé if jours_ecoulé != 0 else 0

        new_y[int(i / 7)] += y[i]
    new_y[-1] = new_y[-1] * last__week_fix

    _ = matplotlib.pyplot.plot(new_x, new_y)
    ax = matplotlib.pyplot.gca()
    matplotlib.pyplot.xticks(rotation=90)
    for label in ax.get_xaxis().get_ticklabels()[::]:
        label.set_visible(False)
    for label in ax.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(True)



plot_week_mean_hospi()
plot_week_mean_rea()
plot_week_mean_dc()
plot_week_mean_hospi_lorraine()
plot_week_mean_rea_lorraine()
plot_week_mean_dc_lorraine()

show()
