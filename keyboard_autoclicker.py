import keyboard
import time
import sys

def keyboard_autoclicker(keys, interval_seconds=0.5, stop_key='esc'):
    print(f"\nAutoclicker ACTIVE - Cycling: {', '.join(keys)} every {interval_seconds}s")
    print(f"PRESS {stop_key.upper()} TO STOP\n")
    
    try:
        while True:
            if keyboard.is_pressed(stop_key):
                print(f"\n[{stop_key}] pressed - Stopping autoclicker")
                break
                
            for key in keys:
                if keyboard.is_pressed(stop_key):
                    break
                keyboard.press_and_release(key)
                time.sleep(interval_seconds)
                
    except KeyboardInterrupt:
        print("\nStopped by user (Ctrl+C)")
    except Exception as e:
        print(f"\nERROR: {str(e)}")

if __name__ == "__main__":
    print("KEYBOARD AUTOCLICKER")
    print("--------------------")
    
    # Customize these settings:
    KEYS = ['E']  # Keys to cycle through
    INTERVAL = 0.01                # Time between key presses (seconds)
    
    print(f"Default keys: {', '.join(KEYS)}")
    print(f"Default interval: {INTERVAL} seconds")
    print("\nTIP: Edit the script to change keys/interval")
    print("      Keep this window focused while running")
    print("      Switch to target window BEFORE starting\n")
    
    input("Press ENTER to start (switch to target window now)...")
    keyboard_autoclicker(KEYS, INTERVAL)