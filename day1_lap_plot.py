import fastf1
import matplotlib.pyplot as plt

# 1. Turn on the cache
fastf1.Cache.enable_cache("cache")

# 2. Choose a race: year, track, session ('R' = Race)
session = fastf1.get_session(2024, "Monza", "R")

# 3. Download and load the data
session.load(weather=False, messages=False)

# 4. Pick one driver's fastest lap
lap = session.laps.pick_drivers("VER").pick_fastest()
print("Driver:", lap["Driver"])
print("Lap time:", lap["LapTime"])
print("Tyre:", lap["Compound"])

# 5. Get that lap's car telemetry and add a distance column
tel = lap.get_car_data().add_distance()
print(tel[["Distance", "Speed", "Throttle", "Brake", "nGear"]].head())

# 6. Plot four graphs stacked on one shared x-axis
fig, axes = plt.subplots(4, 1, figsize=(12, 9), sharex=True)

axes[0].plot(tel["Distance"], tel["Speed"])
axes[0].set_ylabel("Speed (km/h)")

axes[1].plot(tel["Distance"], tel["Throttle"])
axes[1].set_ylabel("Throttle (%)")

axes[2].plot(tel["Distance"], tel["Brake"].astype(int))
axes[2].set_ylabel("Brake (on/off)")

axes[3].plot(tel["Distance"], tel["nGear"])
axes[3].set_ylabel("Gear")
axes[3].set_xlabel("Distance (m)")

fig.suptitle(f"{lap['Driver']} fastest lap - Monza 2024")
plt.tight_layout()
plt.savefig("lap_telemetry.png", dpi=150)
plt.show()