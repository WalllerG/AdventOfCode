from Util.util import read_input
data = read_input(True)

seeds = [int(x) for x in data[0].split(": ")[-1].split(" ")]
seed2soil = {}
soil2fertilizer = {}
fertilizer2water = {}
water2light = {}
light2temperature= {}
temperature2humidity = {}
humidity2location = {}
soils = []
fertilizers = []
waters = []
lights = []
temperatures = []
humidities = []
locations = []


count = 2
while count < len(data):
    if data[count].startswith("seed"):
        count += 1
        while len(data[count]) != 0:
            line = [int(x) for x in data[count].split(" ")]
            ran = line[2]
            a = (line[1], line[1]+ran-1)
            b = (line[0], line[0]+ran-1)
            seed2soil[a] = b
            count += 1
    count += 1
    if data[count].startswith("soil"):
        count += 1
        while len(data[count]) != 0:
            line = [int(x) for x in data[count].split(" ")]
            ran = line[2]
            a = (line[1], line[1] + ran - 1)
            b = (line[0], line[0] + ran - 1)
            soil2fertilizer[a] = b
            count += 1
    if data[count].startswith("fertilizer"):
        count += 1
        while len(data[count]) != 0:
            line = [int(x) for x in data[count].split(" ")]
            ran = line[2]
            a = (line[1], line[1] + ran - 1)
            b = (line[0], line[0] + ran - 1)
            fertilizer2water[a] = b
            count += 1
    if data[count].startswith("water"):
        count += 1
        while len(data[count]) != 0:
            line = [int(x) for x in data[count].split(" ")]
            ran = line[2]
            a = (line[1], line[1] + ran - 1)
            b = (line[0], line[0] + ran - 1)
            water2light[a] = b
            count += 1
    if data[count].startswith("light"):
        count += 1
        while len(data[count]) != 0:
            line = [int(x) for x in data[count].split(" ")]
            ran = line[2]
            a = (line[1], line[1] + ran - 1)
            b = (line[0], line[0] + ran - 1)
            light2temperature[a] = b
            count += 1
    if data[count].startswith("temperature"):
        count += 1
        while len(data[count]) != 0:
            line = [int(x) for x in data[count].split(" ")]
            ran = line[2]
            a = (line[1], line[1] + ran - 1)
            b = (line[0], line[0] + ran - 1)
            temperature2humidity[a] = b
            count += 1
    if data[count].startswith("humidity"):
        count += 1
        while len(data[count]) != 0:
            line = [int(x) for x in data[count].split(" ")]
            ran = line[2]
            a = (line[1], line[1] + ran - 1)
            b = (line[0], line[0] + ran - 1)
            humidity2location[a] = b
            count += 1
            if count == len(data):
                break

for seed in seeds:
    is_in_range = False
    for lb, up in seed2soil.keys():
        if lb <= seed <= up:
            diff = seed - lb
            soils.append(diff+seed2soil[(lb, up)][0])
            is_in_range = True
    if not is_in_range:
        soils.append(seed)

for soil in soils:
    is_in_range = False
    for lb, up in soil2fertilizer.keys():
        if lb <= soil <= up:
            diff = soil - lb
            fertilizers.append(diff + soil2fertilizer[(lb, up)][0])
            is_in_range = True
    if not is_in_range:
        fertilizers.append(soil)

for fertilizer in fertilizers:
    is_in_range = False
    for lb, up in fertilizer2water.keys():
        if lb <= fertilizer <= up:
            diff = fertilizer - lb
            waters.append(diff + fertilizer2water[(lb, up)][0])
            is_in_range = True
    if not is_in_range:
        waters.append(fertilizer)

for water in waters:
    is_in_range = False
    for lb, up in water2light.keys():
        if lb <= water <= up:
            diff = water - lb
            lights.append(diff + water2light[(lb, up)][0])
            is_in_range = True
    if not is_in_range:
        lights.append(water)


for light in lights:
    is_in_range = False
    for lb, up in light2temperature.keys():
        if lb <= light <= up:
            diff = light - lb
            temperatures.append(diff + light2temperature[(lb, up)][0])
            is_in_range = True
    if not is_in_range:
        temperatures.append(light)

for temperature in temperatures:
    is_in_range = False
    for lb, up in temperature2humidity.keys():
        if lb <= temperature <= up:
            diff = temperature - lb
            humidities.append(diff + temperature2humidity[(lb, up)][0])
            is_in_range = True
    if not is_in_range:
        humidities.append(temperature)

for humidity in humidities:
    is_in_range = False
    for lb, up in humidity2location.keys():
        if lb <= humidity <= up:
            diff = humidity - lb
            locations.append(diff + humidity2location[(lb, up)][0])
            is_in_range = True
    if not is_in_range:
        locations.append(humidity)

print(min(locations))