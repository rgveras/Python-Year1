"""
Ricardo Veras
Assignment 1

Calculating Electricity Cost by Time of Use

Off Peak = 7pm-7am
Peak = 7am-11am and 5pm-7pm
Mid-Peak = 11am-5pm
"""

# cost per kwh
OFFPEAKCOST = 0.085
PEAKCOST = 0.176
MIDPEAKCOST = 0.119

offpeak = float(input('Enter kwh during Off Peak period: '))    # Off Peak usage
while offpeak > 0:
    peak = float(input('Enter kwh during On Peak period: '))    # Peak usage
    midpeak = float(input('Enter kwh during Mid Peak period: '))    # Mid Peak usage
    senior = input('Is owner senior? (Y,y,N,n): ')

    offcost = OFFPEAKCOST * offpeak
    peakcost = PEAKCOST * peak
    midcost = MIDPEAKCOST * midpeak

    totalkwh = offpeak + peak + midpeak     # total usage

    totalcost = offcost + peakcost + midcost    # total cost before taxes

    if totalkwh >= 400:
        if peak < 150:
            peakcost = peakcost * 0.95
            totalcost = offcost + peakcost + midcost
    else:
        totalcost = totalcost * 0.96

    if senior == 'y' or senior == 'Y':
        totalcost = totalcost * 0.89

    finalcost = totalcost * 1.13    # total cost with taxes included

    print('Electricity cost: ${:.2f}\n' .format(finalcost))

    offpeak = float(input('Enter kwh during Off Peak period: '))
