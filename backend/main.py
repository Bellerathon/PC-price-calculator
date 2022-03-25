from pcpartpicker import API
import re
import json


# api = API()
# cpu_data = api.retrieve("cpu")

# cpus = []
# for cpu in cpu_data["cpu"]:
#     cpu = str(cpu)
#     words = cpu.strip("CPU(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     cpus.append(" ".join([brand, model]))

# with open(f"./parts/cpus_array.txt", 'w') as file:
#     for cpu in cpus:
#         file.write(cpu + "\n")
# file.close()

# api = API()
# gpu_data = api.retrieve("video-card")
# gpus = []
# for gpu in gpu_data["video-card"]:
#     gpu = str(gpu)
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

#     gpus.append(" ".join([brand, model, chipset]))

# with open(f"./parts/gpus_array.txt", 'w') as file:
#     for gpu in gpus:
#         file.write(gpu + "\n")
# file.close()

# api = API()
# cpu_cooler_data = api.retrieve("cpu-cooler")
# cpu_coolers = []
# for cpu_cooler in cpu_cooler_data["cpu-cooler"]:
#     gpu = str(cpu_cooler)
#     words = gpu.strip("CPUCooler(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     cpu_coolers.append(" ".join([brand, model]))

# with open(f"./parts/cpucoolers_array.txt", 'w') as file:
#     for cpu in cpu_coolers:
#         file.write(cpu + "\n")
# file.close()

# api = API()
# case_fan_data = api.retrieve("case-fan")
# case_fans = []
# for case_fan in case_fan_data["case-fan"]:
#     gpu = str(case_fan)
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

#     case_fans.append(" ".join([brand , model, size]))

# with open(f"./parts/fans_array.txt", 'w') as file:
#     for cpu in case_fans:
#         file.write(cpu + "\n")
# file.close()

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

#     motherboards.append(" ".join([brand, model, chipset, form]))

# with open(f"./parts/motherboards_array.txt", 'w') as file:
#     for cpu in motherboards:
#         file.write(cpu + "\n")
# file.close()

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

#     hdds.append(" ".join([brand, model, size, form, interface]))

# with open(f"./parts/hdds_array.txt", 'w') as file:
#     for cpu in hdds:
#         file.write(cpu + "\n")
# file.close()

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

#     monitors.append(" ".join([brand, model, size + "inch", rfr + "Hz"]))

# with open(f"./parts/monitors_array.txt", 'w') as file:
#     for cpu in monitors:
#         file.write(cpu + "\n")
# file.close()

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

#     cases.append(" ".join([brand, model, form]))

# with open(f"./parts/cases_array.txt", 'w') as file:
#     for cpu in cases:
#         file.write(cpu + "\n")
# file.close()

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

#     features = [brand, model, style, switches, backlight, connection, color]
#     name = ""
#     for feature in features:
#         if feature != 'None' and feature != "Non":
#             name = name + " " + feature
#     keyboards.append(name)

# with open(f"./parts/keyboards_array.txt", 'w') as file:
#     for cpu in keyboards:
#         file.write(cpu + "\n")
# file.close()

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

#     features = [brand, model, tracking, connection, color]
#     name = ""
#     for feature in features:
#         if feature != 'None' and feature != "Non":
#             name = name + " " + feature
#     mouses.append(name)

# with open(f"./parts/mouses_array.txt", 'w') as file:
#     for cpu in mouses:
#         file.write(cpu + "\n")
# file.close()

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
#     powersupplys.append(" ".join([brand, model, entry["name"]]))

# with open(f"./parts/powersupply_array.txt", 'w') as file:
#     for cpu in powersupplys:
#         file.write(cpu + "\n")
# file.close()

# api = API()
# memory_data = api.retrieve("memory")
# memorys = []
# for memory in memory_data["memory"]:
#     gpu = str(memory)
#     entry = {}
#     words = gpu.strip("Memory(").split(",")
#     edit1 = words[0].strip()
#     edit2 = edit1.strip("brand=")
#     brand = edit2.strip("'")

#     edit1 = words[1].strip()
#     edit2 = edit1.strip("model=")
#     model = edit2.strip("'")

#     edit1 = words[2].strip()
#     edit2 = edit1.strip("module_type=")
#     module_type = edit2.strip("'")

#     try:
#         edit1 = words[3].strip()
#         edit2 = edit1.strip("speed=ClockSpeed(cycles=")
#         edit2 = edit2.strip(")")
#         speed = int(edit2) / 1000000
#         speed = str(speed)[:-2]
#     except:
#         speed = "n/a"

#     try:
#         edit1 = words[5].strip()
#         edit2 = edit1.strip("module_size=Bytes(total=")
#         edit2 = edit2.strip(")")
#         size = int(edit2) / 1000000000
#         size = str(size)[:-2]
#     except:
#         size = "n/a"

#     entry["brand"] = brand
#     entry["model"] = model
#     entry["module_type"] = module_type
#     entry["speed"] = speed + "MHz"
#     entry["size"] = size + "GB"
#     memorys.append(" ".join([brand, model, module_type, entry["speed"]]))

# with open(f"./parts/RAM.txt", 'w') as file:
#     for cpu in memorys:
#         file.write(cpu + "\n")
# file.close()
