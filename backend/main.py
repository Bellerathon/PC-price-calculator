from pcpartpicker import API
import re
import json


# api = API()
# cpu_data = api.retrieve("cpu")

# cpus = []
# for cpu in cpu_data["cpu"]:
#     cpu = str(cpu)
#     entry = {}
#     words = cpu.strip("CPU(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     entry["brand"] = brand
#     entry["model"] = model
#     cpus.append(entry)

# saveFile = open(f"./pcparts_data/cpus.txt", 'w')
# json.dump(cpus, saveFile, indent=4)

# api = API()
# gpu_data = api.retrieve("video-card")
# print(gpu_data)
# gpus = []
# for gpu in gpu_data["video-card"]:
#     gpu = str(gpu)
#     entry = {}
#     words = gpu.strip("GPU(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     edit1 = words[2].strip()
#     edit2 = edit1.strip("chipset=")
#     chipset = edit2.strip("'")

#     entry["brand"] = brand
#     entry["chipset"] = chipset
#     entry["model"] = model
#     gpus.append(entry)

# saveFile = open(f"./pcparts_data/gpus.txt", 'w')
# json.dump(gpus, saveFile, indent=4)

# api = API()
# cpu_cooler_data = api.retrieve("cpu-cooler")
# cpu_coolers = []
# for cpu_cooler in cpu_cooler_data["cpu-cooler"]:
#     gpu = str(cpu_cooler)
#     entry = {}
#     words = gpu.strip("CPUCooler(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     entry["brand"] = brand
#     entry["model"] = model
#     cpu_coolers.append(entry)

# saveFile = open(f"./pcparts_data/cpu_coolers.txt", 'w')
# json.dump(cpu_coolers, saveFile, indent=4)

# api = API()
# case_fan_data = api.retrieve("case-fan")
# case_fans = []
# for case_fan in case_fan_data["case-fan"]:
#     gpu = str(case_fan)
#     entry = {}
#     words = gpu.strip("Fan(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     edit1 = words[2].strip()
#     edit2 = edit1.strip("size=")
#     size = edit2.strip("'")

#     entry["brand"] = brand
#     entry["size"] = size
#     entry["model"] = model
#     case_fans.append(entry)

# saveFile = open(f"./pcparts_data/case_fans.txt", 'w')
# json.dump(case_fans, saveFile, indent=4)

# api = API()
# motherboard_data = api.retrieve("motherboard")
# motherboards = []
# for motherboard in motherboard_data["motherboard"]:
#     gpu = str(motherboard)
#     entry = {}
#     words = gpu.strip("Motherboard(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     edit1 = words[2].strip()
#     edit2 = edit1.strip("socket=")
#     chipset = edit2.strip("'")

#     edit1 = words[3].strip()
#     edit2 = edit1.strip("form_factor=")
#     form = edit2.strip("'")

#     entry["brand"] = brand
#     entry["chipset"] = chipset
#     entry["form"] = form
#     entry["model"] = model
#     motherboards.append(entry)

# saveFile = open(f"./pcparts_data/motherboards.txt", 'w')
# json.dump(motherboards, saveFile, indent=4)

# api = API()
# hdd_data = api.retrieve("internal-hard-drive")
# hdds = []
# for hdd in hdd_data["internal-hard-drive"]:
#     gpu = str(hdd)
#     entry = {}
#     words = gpu.strip("StorageDrive(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     edit1 = words[2].strip()
#     edit2 = edit1.strip("capacity=Bytes(total=")
#     edit2 = edit2.strip(")")
#     edit2 = int(edit2) / 1000000000
#     if (edit2 >= 1000):
#         edit2 = edit2 / 1000
#         edit2 = str(edit2) + "TB"
#     else:
#         edit2 = str(edit2) + "GB"

#     size = edit2

#     edit1 = words[4].strip()
#     edit2 = edit1.strip("storage_type=")
#     form = edit2.strip("'")

#     edit1 = words[8].strip()
#     edit2 = edit1.strip("interface=")
#     interface = edit2.strip("'")

#     entry["brand"] = brand
#     entry["model"] = model
#     entry["size"] = size
#     entry["form"] = form
#     entry["interface"] = interface
#     hdds.append(entry)

# saveFile = open(f"./pcparts_data/storage.txt", 'w')
# json.dump(hdds, saveFile, indent=4)

# api = API()
# monitor_data = api.retrieve("monitor")
# monitors = []
# for monitor in monitor_data["monitor"]:
#     gpu = str(monitor)
#     entry = {}
#     words = gpu.strip("Monitor(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     edit1 = words[2].strip()
#     size = edit1.strip("size=")

#     edit1 = words[5].strip()
#     rfr = edit1.strip("refresh_rate=")

#     entry["brand"] = brand
#     entry["model"] = model
#     entry["size"] = size
#     entry["Hz"] = rfr
#     monitors.append(entry)

# saveFile = open(f"./pcparts_data/monitors.txt", 'w')
# json.dump(monitors, saveFile, indent=4)

# api = API()
# case_data = api.retrieve("case")
# cases = []
# for case in case_data["case"]:
#     gpu = str(case)
#     entry = {}
#     words = gpu.strip("Case(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     edit1 = words[2].strip()
#     form = edit1.strip("form_factor=")

#     entry["brand"] = brand
#     entry["model"] = model
#     entry["form"] = form
#     cases.append(entry)

# saveFile = open(f"./pcparts_data/cases.txt", 'w')
# json.dump(cases, saveFile, indent=4)

# api = API()
# keyboard_data = api.retrieve("keyboard")
# keyboards = []
# for keyboard in keyboard_data["keyboard"]:
#     gpu = str(keyboard)
#     entry = {}
#     words = gpu.strip("Keyboard(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     edit1 = words[2].strip()
#     edit2 = edit1.strip("style=")
#     style = edit2.strip("'")

#     edit1 = words[3].strip()
#     edit2 = edit1.strip("switches=")
#     switches = edit2.strip("'")

#     edit1 = words[4].strip()
#     edit2 = edit1.strip("backlight=")
#     backlight = edit2.strip("'")

#     edit1 = words[6].strip()
#     edit2 = edit1.strip("connection=")
#     connection = edit2.strip("'")

#     edit1 = words[7].strip()
#     edit2 = edit1.strip("color=")
#     color = edit2.strip("'")

#     entry["brand"] = brand
#     entry["model"] = model
#     entry["name"] = " ".join([style, switches, backlight, connection, color]) 
#     keyboards.append(entry)

# saveFile = open(f"./pcparts_data/keyboards.txt", 'w')
# json.dump(keyboards, saveFile, indent=4)

# api = API()
# mouse_data = api.retrieve("mouse")
# mouses = []
# for mouse in mouse_data["mouse"]:
#     gpu = str(mouse)
#     entry = {}
#     words = gpu.strip("Mouse(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     edit1 = words[2].strip()
#     edit2 = edit1.strip("tracking=")
#     tracking = edit2.strip("'")

#     edit1 = words[3].strip()
#     edit2 = edit1.strip("connection=")
#     connection = edit2.strip("'")

#     edit1 = words[6].strip()
#     edit2 = edit1.strip("color=")
#     color = edit2.strip("'")

#     entry["brand"] = brand
#     entry["model"] = model
#     entry["details"] = " ".join([tracking, connection, color]) 
#     mouses.append(entry)

# saveFile = open(f"./pcparts_data/mouses.txt", 'w')
# json.dump(mouses, saveFile, indent=4)

# api = API()
# powersupply_data = api.retrieve("power-supply")
# powersupplys = []
# for powersupply in powersupply_data["power-supply"]:
#     gpu = str(powersupply)
#     entry = {}
#     words = gpu.strip("PSU(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     edit1 = words[2].strip()
#     edit2 = edit1.strip("form_factor=")
#     form = edit2.strip("'")

#     edit1 = words[3].strip()
#     edit2 = edit1.strip("effiency_rating=")
#     efficiency = edit2.strip("'")

#     edit1 = words[4].strip()
#     edit2 = edit1.strip("wattage=")
#     wattage = edit2.strip("'")

#     edit1 = words[5].strip()
#     edit2 = edit1.strip("modular=")
#     modular = edit2.strip("'")

#     entry["brand"] = brand
#     entry["model"] = model
#     entry["name"] = " ".join([form, efficiency, wattage + "W", modular + " modular"]) 
#     powersupplys.append(entry)

# saveFile = open(f"./pcparts_data/powersupplys.txt", 'w')
# json.dump(powersupplys, saveFile, indent=4)

api = API()
memory_data = api.retrieve("memory")
memorys = []
for memory in memory_data["memory"]:
    gpu = str(memory)
    entry = {}
    words = gpu.strip("Memory(").split(",")
    edit1 = words[0].strip()
    edit2 = edit1.strip("brand=")
    brand = edit2.strip("'")

    edit1 = words[1].strip()
    edit2 = edit1.strip("model=")
    model = edit2.strip("'")

    edit1 = words[2].strip()
    edit2 = edit1.strip("module_type=")
    module_type = edit2.strip("'")

    try:
        edit1 = words[3].strip()
        edit2 = edit1.strip("speed=ClockSpeed(cycles=")
        edit2 = edit2.strip(")")
        speed = int(edit2) / 1000000
        speed = str(speed)[:-2]
    except:
        speed = "n/a"

    try:
        edit1 = words[5].strip()
        edit2 = edit1.strip("module_size=Bytes(total=")
        edit2 = edit2.strip(")")
        size = int(edit2) / 1000000000
        size = str(size)[:-2]
    except:
        size = "n/a"

    entry["brand"] = brand
    entry["model"] = model
    entry["module_type"] = module_type
    entry["speed"] = speed + "MHz"
    entry["size"] = size + "GB"
    memorys.append(entry)

saveFile = open(f"./pcparts_data/memory.txt", 'w')
json.dump(memorys, saveFile, indent=4)