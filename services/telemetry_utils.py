from services.fastf1_loader import load_session

def get_driver_telemetry(year, gp, driver):
    session = load_session(year, gp, "R")
    laps = session.laps.pick_driver(driver)
    fastest = laps.pick_fastest()
    return fastest.get_car_data().add_distance()

def compare_telemetry(year, gp, driver_a, driver_b):
    session = load_session(year, gp, "R")

    lap_a = session.laps.pick_driver(driver_a).pick_fastest()
    lap_b = session.laps.pick_driver(driver_b).pick_fastest()

    telA = lap_a.get_car_data().add_distance()
    telB = lap_b.get_car_data().add_distance()

    return telA, telB
