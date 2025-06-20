import time
import os
from datetime import datetime, timedelta

#This script allows you to choose either Christian Prayer & Ramadan Prayer times

# ------------------ LENT PRAYER FUNCTIONS ------------------

lent_prayer_times = {
    "Morning Prayer (Lauds)": "06:30",
    "Midday Prayer (Sext)": "12:00",
    "Afternoon Prayer (None)": "15:00",
    "Evening Prayer (Vespers)": "18:30",
    "Night Prayer (Compline)": "21:00"
}

def get_lent_prayer_times():
    return {name: datetime.strptime(t, "%H:%M").time() for name, t in lent_prayer_times.items()}

def display_lent_schedule():
    lent_times_today = get_lent_prayer_times()
    last_update_day = datetime.today().day

    while True:
        try:
            now = datetime.now()
            if now.day != last_update_day:
                lent_times_today = get_lent_prayer_times()
                last_update_day = now.day

            os.system("cls" if os.name == "nt" else "clear")
            print("\n✝️ Lent Prayer Schedule (Press Ctrl+C to return to menu):\n")
            for name, prayer_time in lent_times_today.items():
                event_dt = datetime.combine(now.date(), prayer_time)
                if now > event_dt:
                    event_dt += timedelta(days=1)
                remaining = str(event_dt - now).split('.')[0]
                print(f"🙏 {name} at {prayer_time.strftime('%H:%M')} — ⏳ {remaining}")
            time.sleep(5)

        except KeyboardInterrupt:
            print("\nReturning to menu...\n")
            break

# ------------------ RAMADAN PRAYER FUNCTIONS ------------------

ramadan_start = datetime(2025, 3, 2)
fajr_time = "05:19"
shuruq_time = "07:12"
dhuhr_time = "12:41"
asr_time = "16:16"
maghrib_time = "18:10"
isha_time = "19:56"
suhoor_time = "05:00"
iftar_time = "18:30"

def convert_prayer_times():
    return {
        "🪬Fajr": datetime.strptime(fajr_time, "%H:%M").time(),
        "🪬Shuruq": datetime.strptime(shuruq_time, "%H:%M").time(),
        "🪬Dhuhr": datetime.strptime(dhuhr_time, "%H:%M").time(),
        "🪬Asr": datetime.strptime(asr_time, "%H:%M").time(),
        "🪬Maghrib": datetime.strptime(maghrib_time, "%H:%M").time(),
        "🪬Isha": datetime.strptime(isha_time, "%H:%M").time(),
        "🪬Suhoor": datetime.strptime(suhoor_time, "%H:%M").time(),
        "🪬Iftar": datetime.strptime(iftar_time, "%H:%M").time()
    }

def ramadan_countdown():
    today = datetime.today()
    days_left = (ramadan_start - today).days
    print(f"🌙 Days until Ramadan: {days_left} days")

def display_ramadan_schedule():
    prayer_times = convert_prayer_times()
    ramadan_countdown()

    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("🌙 Ramadan Prayer Countdown (Press Ctrl+C to return to menu):\n")
            now = datetime.now()

            for name, time_val in prayer_times.items():
                event_dt = datetime.combine(now.date(), time_val)
                if now.time() > time_val:
                    event_dt += timedelta(days=1)
                remaining = str(event_dt - now).split('.')[0]
                print(f"{name} at {time_val.strftime('%H:%M')} — ⏳ {remaining}")
            time.sleep(5)

        except KeyboardInterrupt:
            print("\nReturning to menu...\n")
            break

# ------------------ MAIN MENU ------------------

def main():
    while True:
        print("\nWhich schedule would you like to run?")
        print("1. ✝️ Lent Prayer Countdown")
        print("2. 🌙 Ramadan Prayer Countdown")
        print("3. ❌ Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            display_lent_schedule()
        elif choice == "2":
            display_ramadan_schedule()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
