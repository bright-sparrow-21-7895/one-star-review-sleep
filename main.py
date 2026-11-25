# One-star review of sleep, the one essential nobody can uninstall.
# The joke treats sleep like badly shipped software: an eight-hour
# install every night, a crash whenever a baby sneezes two streets
# away, and a snooze button that promises nine more minutes and
# delivers a scam. Essential, beloved, and still only worth one star.
import os

ENTRY = "One star. Sleep takes eight hours to install, crashes if a baby sneezes two streets away, and the snooze button is a scam."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
