#!/usr/bin/env python3
"""
DecoyCards - Fake Gift Card Generator for Scambaiting
By Baitrix

This tool generates fake gift card codes and provides a store timer
to help scambaiters waste scammers' time. The codes are intentionally
invalid and should be tested before use to ensure they don't work.

IMPORTANT: These are FAKE codes for scambaiting purposes only!
Always test codes first to confirm they are invalid.
"""

import random
import string
import os
import time
import platform
import subprocess
import threading
import sys
from datetime import datetime

# Try to import GUI library - gracefully handle if not available
try:
    import customtkinter as ctk
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False


class DecoyCards:
    """
    Main class that handles fake gift card generation and scambaiting utilities.
    
    This class provides methods to:
    - Generate fake gift card codes for various platforms
    - Calculate realistic travel times for "going to store" scenarios  
    - Play notification sounds when timers complete
    - Bring the application window to foreground for attention
    """
    def __init__(self):
        # Character set for generating fake codes (uppercase letters + digits)
        self.chars = string.ascii_uppercase + string.digits

    def clear_screen(self):
        """Clear the terminal screen (works on Windows and Unix-like systems)"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def play_sound(self):
        """
        Play a notification sound to alert the user when timers complete.
        Uses playsound3 library for cross-platform compatibility with fallbacks:
        - Windows: Uses system message beep
        - macOS: Plays Glass.aiff system sound  
        - Linux: Tries various system sound files
        - Fallback: Terminal bell character if all else fails
        """
        try:
            from playsound3 import playsound
            # Try to play a system notification sound
            system = platform.system().lower()
            
            if system == 'windows':
                # Use Windows system sound
                import winsound
                winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
            elif system == 'darwin':
                # Try macOS system sound first
                try:
                    playsound('/System/Library/Sounds/Glass.aiff', block=False)
                except:
                    os.system('afplay /System/Library/Sounds/Glass.aiff')
            elif system == 'linux':
                # Try Linux system sounds
                sound_files = [
                    '/usr/share/sounds/alsa/Front_Left.wav',
                    '/usr/share/sounds/ubuntu/stereo/bell.ogg',
                    '/usr/share/sounds/gnome/default/alerts/glass.ogg'
                ]
                
                sound_played = False
                for sound_file in sound_files:
                    if os.path.exists(sound_file):
                        try:
                            playsound(sound_file, block=False)
                            sound_played = True
                            break
                        except:
                            continue
                
                if not sound_played:
                    # Fallback to terminal bell
                    print('\a')
            else:
                print('\a')
        except ImportError:
            # Fallback if playsound3 not available
            print('\a')
        except Exception:
            # Any other error, use terminal bell
            print('\a')

    def bring_to_foreground(self):
        """
        Bring the application window to the front to get user's attention.
        Platform-specific implementations:
        - Windows: Uses Win32 API to set foreground window
        - macOS: Activates Terminal application
        - Linux: Uses wmctrl or xdotool to activate window
        """
        system = platform.system().lower()

        try:
            if system == 'windows':
                try:
                    import ctypes
                    from ctypes import wintypes

                    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
                    user32 = ctypes.WinDLL('user32', use_last_error=True)

                    hWnd = kernel32.GetConsoleWindow()
                    if hWnd:
                        user32.SetForegroundWindow(hWnd)
                        user32.ShowWindow(hWnd, 9)
                        user32.SetWindowPos(
                            hWnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)
                except:
                    pass

            elif system == 'darwin':
                subprocess.run(['osascript', '-e', 'tell application "Terminal" to activate'],
                               capture_output=True, check=False)

            elif system == 'linux':
                try:
                    subprocess.run(['wmctrl', '-a', 'DecoyCards'],
                                   capture_output=True, check=False)
                except:
                    try:
                        result = subprocess.run(['xdotool', 'search', '--name', 'DecoyCards'],
                                                capture_output=True, text=True)
                        if result.stdout.strip():
                            window_id = result.stdout.strip().split('\n')[0]
                            subprocess.run(['xdotool', 'windowactivate', window_id],
                                           capture_output=True)
                    except:
                        pass

        except Exception:
            pass

    # === FAKE GIFT CARD GENERATORS ===
    # Each method generates codes in the format expected by that platform
    # All codes are intentionally fake and should be tested to ensure invalidity

    def generate_xbox(self):
        """Generate fake Xbox Live gift card code (format: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX)"""
        segments = []
        for _ in range(5):
            segment = ''.join(random.choice(self.chars) for _ in range(5))
            segments.append(segment)
        return '-'.join(segments)

    def generate_psn(self):
        """Generate fake PlayStation Network gift card code (format: XXXX-XXXX-XXXX)"""
        segments = []
        for _ in range(3):
            segment = ''.join(random.choice(self.chars) for _ in range(4))
            segments.append(segment)
        return '-'.join(segments)

    def generate_amazon(self):
        """Generate fake Amazon gift card code (format: XXXX-XXXXXX-XXXXX)"""
        segment1 = ''.join(random.choice(self.chars) for _ in range(4))
        segment2 = ''.join(random.choice(self.chars) for _ in range(6))
        segment3 = ''.join(random.choice(self.chars) for _ in range(5))
        return f"{segment1}-{segment2}-{segment3}"

    def generate_google_play(self):
        """Generate fake Google Play gift card code (format: XXXXXXX-XXXXXXX-XXXXX)"""
        segment1 = ''.join(random.choice(self.chars) for _ in range(7))
        segment2 = ''.join(random.choice(self.chars) for _ in range(7))
        segment3 = ''.join(random.choice(self.chars) for _ in range(5))
        return f"{segment1}-{segment2}-{segment3}"

    def generate_apple(self):
        """Generate fake Apple/iTunes gift card code (16 characters, starts with X)"""
        # Apple uses specific character set excluding confusing letters
        apple_chars = '0123456789ABCDEFGHJKMNPQRSTVWXY'
        code = 'X' + ''.join(random.choice(apple_chars) for _ in range(15))
        return code

    def generate_steam(self):
        """Generate fake Steam wallet code (format: XXXXX-XXXXX-XXXXX)"""
        segments = []
        for _ in range(3):
            segment = ''.join(random.choice(self.chars) for _ in range(5))
            segments.append(segment)
        return '-'.join(segments)

    def generate_walmart(self):
        """Generate fake Walmart gift card with card number and PIN"""
        card_number = ''.join(random.choice(string.digits) for _ in range(16))
        pin = ''.join(random.choice(string.digits) for _ in range(4))
        return f"Card: {card_number[:4]}-{card_number[4:8]}-{card_number[8:12]}-{card_number[12:16]} | PIN: {pin}"

    def generate_target(self):
        """Generate fake Target gift card with card number and PIN"""
        card_number = ''.join(random.choice(string.digits) for _ in range(15))
        pin = ''.join(random.choice(string.digits) for _ in range(4))
        return f"Card: {card_number} | PIN: {pin}"

    def generate_visa(self):
        """Generate fake Visa gift card with full details (card, expiry, CVV, claim code)"""
        card_number = ''.join(random.choice(string.digits) for _ in range(16))
        exp_month = random.choice(
            ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
        exp_year = random.choice(['25', '26', '27', '28', '29'])
        cvv = ''.join(random.choice(string.digits) for _ in range(3))
        claim_code = ''.join(random.choice(self.chars) for _ in range(8))
        return f"Card: {card_number[:4]}-{card_number[4:8]}-{card_number[8:12]}-{card_number[12:16]} | Exp: {exp_month}/{exp_year} | CVV: {cvv} | Claim: {claim_code}"

    def get_card_info(self, card_type):
        """
        Get metadata about different gift card types including:
        - Display name
        - Expected format
        - Test URL where codes can be validated (if available)
        """
        card_info = {
            'xbox': {
                'name': 'Xbox Live Gift Card',
                'format': 'XXXXX-XXXXX-XXXXX-XXXXX-XXXXX',
                'test_url': 'https://www.xbox.com/en-US/redeem'
            },
            'psn': {
                'name': 'PlayStation Network Gift Card',
                'format': 'XXXX-XXXX-XXXX',
                'test_url': None
            },
            'amazon': {
                'name': 'Amazon Gift Card',
                'format': 'XXXX-XXXXXX-XXXXX',
                'test_url': 'https://www.amazon.com/gc/redeem'
            },
            'google-play': {
                'name': 'Google Play Gift Card',
                'format': 'XXXXXXX-XXXXXXX-XXXXX',
                'test_url': None
            },
            'apple': {
                'name': 'Apple/iTunes Gift Card',
                'format': 'X + 15 alphanumeric characters (no O, U, I, L, Z)',
                'test_url': None
            },
            'steam': {
                'name': 'Steam Wallet Code',
                'format': 'XXXXX-XXXXX-XXXXX',
                'test_url': 'https://store.steampowered.com/account/redeemwalletcode'
            },
            'walmart': {
                'name': 'Walmart Gift Card',
                'format': '16-digit card + 4-digit PIN',
                'test_url': None
            },
            'target': {
                'name': 'Target Gift Card',
                'format': '15-digit card + 4-digit PIN',
                'test_url': None
            },
            'visa': {
                'name': 'Visa Gift Card',
                'format': '16-digit + expiry + CVV + claim code',
                'test_url': None
            }
        }
        return card_info.get(card_type, {})

    def generate(self, card_type, count=1):
        """
        Generate one or more fake gift cards of the specified type.
        
        Args:
            card_type: Type of card to generate (xbox, psn, amazon, etc.)
            count: Number of cards to generate (default: 1)
            
        Returns:
            tuple: (list_of_cards, card_info_dict) or (None, error_message)
        """
        generators = {
            'xbox': self.generate_xbox,
            'psn': self.generate_psn,
            'amazon': self.generate_amazon,
            'google-play': self.generate_google_play,
            'apple': self.generate_apple,
            'steam': self.generate_steam,
            'walmart': self.generate_walmart,
            'target': self.generate_target,
            'visa': self.generate_visa
        }

        if card_type not in generators:
            return None, f"Invalid card type. Available: {', '.join(generators.keys())}"

        cards = []
        for _ in range(count):
            cards.append(generators[card_type]())

        card_info = self.get_card_info(card_type)

        return cards, card_info

    # === STORE TIMER UTILITIES ===
    # These methods help create realistic "going to store" scenarios

    def calculate_travel_time(self, distance, unit, speed_type):
        """
        Calculate realistic travel time based on distance and transportation method.
        
        Args:
            distance: Distance to travel
            unit: 'miles' or 'km' 
            speed_type: 'walking', 'biking', or 'car'
            
        Returns:
            tuple: (hours, minutes, seconds, total_minutes) or None if invalid
        """
        speeds = {
            'walking': {'mph': 3, 'kmh': 5},
            'biking': {'mph': 12, 'kmh': 20},
            'car': {'mph': 30, 'kmh': 50}
        }

        if speed_type == 'not specified':
            return None

        if unit == 'miles':
            speed = speeds[speed_type]['mph']
        else:
            speed = speeds[speed_type]['kmh']

        time_hours = distance / speed
        time_minutes = time_hours * 60

        hours = int(time_minutes // 60)
        minutes = int(time_minutes % 60)
        seconds = int((time_minutes % 1) * 60)

        return hours, minutes, seconds, time_minutes

    def format_time(self, hours, minutes, seconds):
        """Format time duration into human-readable string"""
        if hours > 0:
            return f"{hours}h {minutes}m {seconds}s"
        elif minutes > 0:
            return f"{minutes}m {seconds}s"
        else:
            return f"{seconds}s"

    def countdown_timer(self, total_minutes, phase):
        """
        Run a countdown timer for the specified duration.
        Shows real-time countdown and plays sound + brings window to foreground when complete.
        
        Args:
            total_minutes: Duration of timer in minutes
            phase: Description of what phase this timer represents (e.g. "Going to store")
        """
        print(f"\n{phase} timer started!")
        print("Press Ctrl+C to stop the timer early")

        total_seconds = int(total_minutes * 60)

        try:
            for remaining in range(total_seconds, -1, -1):
                hours = remaining // 3600
                minutes = (remaining % 3600) // 60
                seconds = remaining % 60

                if hours > 0:
                    time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                else:
                    time_str = f"{minutes:02d}:{seconds:02d}"

                print(f"\r{phase}: {time_str} remaining", end="", flush=True)
                time.sleep(1)

            print(f"\n\n{phase} complete!")
            self.play_sound()
            self.bring_to_foreground()

        except KeyboardInterrupt:
            print(f"\n\n{phase} timer stopped early.")

    def store_timer(self):
        """
        Interactive store timer that helps create realistic "going to store" scenarios.
        
        Prompts user for:
        - Distance to store and transportation method (for realistic timing)
        - OR manual time specification
        
        Runs two phases:
        1. "Going to store" timer
        2. "Returning home" timer
        
        This helps scambaiters create believable delays when "buying" gift cards.
        """
        self.clear_screen()
        print("DecoyCards - Store Timer")
        print("Tell your scammer you're going to the store!")
        print()

        print("Distance unit:")
        print("1. Miles")
        print("2. Kilometers")
        print("3. Not specified")

        while True:
            unit_choice = input("Select (1-3): ").strip()
            if unit_choice == '1':
                unit = 'miles'
                break
            elif unit_choice == '2':
                unit = 'km'
                break
            elif unit_choice == '3':
                unit = 'not specified'
                break
            else:
                print("Please select 1-3")

        if unit == 'not specified':
            while True:
                try:
                    total_minutes = float(
                        input("\nEnter travel time in minutes: "))
                    if total_minutes <= 0:
                        print("Time must be positive")
                        continue
                    hours = int(total_minutes // 60)
                    minutes = int(total_minutes % 60)
                    seconds = int((total_minutes % 1) * 60)
                    time_str = self.format_time(hours, minutes, seconds)
                    break
                except ValueError:
                    print("Please enter a valid number")

            print(f"\nYou can tell the scammer:")
            print(f"\"I'm going to the store to get the gift card.")
            print(f"I'll be back in about {time_str}.\"")
        else:
            while True:
                try:
                    distance = float(
                        input(f"\nDistance to store in {unit} (enter number): "))
                    if distance <= 0:
                        print("Distance must be positive")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number")

            print("\nTransportation method:")
            print("1. Walking")
            print("2. Biking")
            print("3. Car")

            while True:
                transport_choice = input("Select (1-3): ").strip()
                if transport_choice == '1':
                    transport = 'walking'
                    break
                elif transport_choice == '2':
                    transport = 'biking'
                    break
                elif transport_choice == '3':
                    transport = 'car'
                    break
                else:
                    print("Please select 1-3")

            travel_time = self.calculate_travel_time(distance, unit, transport)
            hours, minutes, seconds, total_minutes = travel_time
            time_str = self.format_time(hours, minutes, seconds)
            print(f"\nCalculated travel time: {time_str}")

            print(f"\nYou can tell the scammer:")
            print(
                f"\"I'm going to the store to get the gift card. It's {distance} {unit} away")
            print(f"by {transport}, so I'll be back in about {time_str}.\"")

        input("\nPress Enter to start the 'going to store' timer...")
        self.countdown_timer(total_minutes, "Going to store")

        input("\nPress Enter to start the 'returning home' timer...")
        self.countdown_timer(total_minutes, "Returning home")

        print("\nYou can now tell the scammer you're back with the gift card!")
        input("Press Enter to continue...")


class DecoyCardsGUI:
    """
    Modern GUI interface for DecoyCards using CustomTkinter.
    
    Provides a user-friendly graphical interface with:
    - Gift card generation with copy-to-clipboard functionality
    - Visual store timer with progress bars and dialogs
    - Dark theme with modern styling
    - Real-time timer updates and notifications
    - Cross-platform window management for attention-getting
    """
    def __init__(self):
        # Initialize core components
        self.decoy = DecoyCards()
        
        # Timer state management
        self.timer_active = False
        self.current_phase = None
        self.total_seconds = 0
        self.remaining_seconds = 0
        self.timer_job = None

        # Set up modern dark theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Create main window
        self.root = ctk.CTk()
        self.root.title("DecoyCards - Scambait tool thingie by Baitrix")
        self.root.geometry("900x650")
        self.root.resizable(True, True)
        self.root.minsize(800, 600)

        # Configure grid layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.setup_ui()

    def setup_ui(self):
        main_container = ctk.CTkFrame(self.root, corner_radius=10)
        main_container.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)
        main_container.grid_rowconfigure(1, weight=1)
        main_container.grid_columnconfigure(0, weight=1)

        header_frame = ctk.CTkFrame(main_container, height=75, corner_radius=8)
        header_frame.grid(row=0, column=0, sticky="ew", padx=15, pady=(15, 8))
        header_frame.grid_propagate(False)

        title_label = ctk.CTkLabel(
            header_frame,
            text="DecoyCards",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title_label.pack(pady=(8, 1))

        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Scambait tool thingie by Baitrix",
            font=ctk.CTkFont(size=12),
            text_color="gray70"
        )
        subtitle_label.pack()

        warning_label = ctk.CTkLabel(
            header_frame,
            text="⚠ FAKE CODES FOR SCAMBAITING ONLY ⚠",
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="#ff6b35"
        )
        warning_label.pack(pady=(1, 0))

        self.tabview = ctk.CTkTabview(main_container, corner_radius=8)
        self.tabview.grid(row=1, column=0, sticky="nsew",
                          padx=15, pady=(0, 15))

        self.tabview.add("Gift Cards")
        self.setup_gift_cards_tab()

        self.tabview.add("Store Timer")
        self.setup_timer_tab()

    def setup_gift_cards_tab(self):
        tab = self.tabview.tab("Gift Cards")
        tab.grid_rowconfigure(2, weight=1)
        tab.grid_columnconfigure(0, weight=1)

        instruction_frame = ctk.CTkFrame(tab, corner_radius=8)
        instruction_frame.grid(
            row=0, column=0, sticky="ew", padx=15, pady=(15, 8))

        ctk.CTkLabel(
            instruction_frame,
            text="Generate Fake Gift Card Codes",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=(10, 3))

        ctk.CTkLabel(
            instruction_frame,
            text="Select a gift card type below to generate fake codes for scambaiting",
            font=ctk.CTkFont(size=12),
            text_color="gray70"
        ).pack(pady=(0, 10))

        quantity_frame = ctk.CTkFrame(tab, corner_radius=8)
        quantity_frame.grid(row=1, column=0, sticky="ew", padx=15, pady=8)

        ctk.CTkLabel(
            quantity_frame,
            text="Number of cards to generate:",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(side="left", padx=(15, 8), pady=10)

        self.card_count_var = ctk.StringVar(value="1")
        self.card_count_entry = ctk.CTkEntry(
            quantity_frame,
            textvariable=self.card_count_var,
            width=80,
            font=ctk.CTkFont(size=14, weight="bold"),
            justify="center"
        )
        self.card_count_entry.pack(side="left", padx=(0, 15), pady=10)

        cards_frame = ctk.CTkFrame(tab, corner_radius=8)
        cards_frame.grid(row=2, column=0, sticky="nsew", padx=15, pady=(0, 15))

        for i in range(3):
            cards_frame.grid_columnconfigure(i, weight=1)

        card_types = [
            ("Xbox Live", "xbox", "#107c10"),
            ("PlayStation", "psn", "#003791"),
            ("Amazon", "amazon", "#ff9900"),
            ("Google Play", "google-play", "#34a853"),
            ("Apple iTunes", "apple", "#000000"),
            ("Steam", "steam", "#1b2838"),
            ("Walmart", "walmart", "#0071ce"),
            ("Target", "target", "#cc0000"),
            ("Visa Gift Card", "visa", "#1a1f71")
        ]

        for i, (name, code, color) in enumerate(card_types):
            row = i // 3
            col = i % 3

            btn = ctk.CTkButton(
                cards_frame,
                text=name,
                font=ctk.CTkFont(size=14, weight="bold"),
                fg_color=color,
                hover_color=self.adjust_color(color, -20),
                height=50,
                width=220,
                corner_radius=8,
                command=lambda c=code, n=name: self.generate_main_cards(c, n)
            )
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="ew")

    def setup_timer_tab(self):
        tab = self.tabview.tab("Store Timer")
        tab.grid_rowconfigure(2, weight=1)
        tab.grid_columnconfigure(0, weight=1)

        header_frame = ctk.CTkFrame(tab, corner_radius=8)
        header_frame.grid(row=0, column=0, sticky="ew", padx=15, pady=(15, 5))

        ctk.CTkLabel(
            header_frame,
            text="⏰ Store Timer - ⚠️ ROUND TRIP (Going + Returning)",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ff6b35"
        ).pack(pady=8)

        config_frame = ctk.CTkFrame(tab, corner_radius=8)
        config_frame.grid(row=1, column=0, sticky="ew", padx=15, pady=5)
        config_frame.grid_columnconfigure(1, weight=1)

        self.live_calc_frame = ctk.CTkFrame(
            config_frame, fg_color="#1a4d3a", corner_radius=6)
        self.live_calc_frame.grid(
            row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=(8, 6))

        self.live_calc_label = ctk.CTkLabel(
            self.live_calc_frame,
            text="📊 Configure settings to see live calculation",
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="#4caf50",
            wraplength=400
        )
        self.live_calc_label.pack(pady=4)

        controls_frame = ctk.CTkFrame(config_frame, fg_color="transparent")
        controls_frame.grid(row=1, column=0, columnspan=3,
                            sticky="ew", padx=10, pady=4)

        ctk.CTkLabel(controls_frame, text="Unit:", font=ctk.CTkFont(size=10, weight="bold")).grid(
            row=0, column=0, sticky="w", padx=(0, 3), pady=2
        )

        self.unit_var = ctk.StringVar(value="miles")
        self.unit_menu = ctk.CTkOptionMenu(
            controls_frame,
            values=["miles", "km", "manual"],
            variable=self.unit_var,
            command=self.on_unit_change,
            width=80,
            height=26,
            font=ctk.CTkFont(size=10)
        )
        self.unit_menu.grid(row=1, column=0, padx=(0, 8), pady=2)

        self.distance_label = ctk.CTkLabel(
            controls_frame, text="Distance:", font=ctk.CTkFont(size=10, weight="bold"))
        self.distance_label.grid(
            row=0, column=1, sticky="w", padx=(0, 3), pady=2)

        self.distance_entry = ctk.CTkEntry(
            controls_frame,
            placeholder_text="Distance",
            width=90,
            height=26,
            font=ctk.CTkFont(size=10)
        )
        self.distance_entry.grid(row=1, column=1, padx=(0, 8), pady=2)
        self.distance_entry.bind('<KeyRelease>', self.update_live_calculation)

        self.transport_label = ctk.CTkLabel(
            controls_frame, text="Transport:", font=ctk.CTkFont(size=10, weight="bold"))
        self.transport_label.grid(
            row=0, column=2, sticky="w", padx=(0, 3), pady=2)

        self.transport_var = ctk.StringVar(value="walking")
        self.transport_menu = ctk.CTkOptionMenu(
            controls_frame,
            values=["walking", "biking", "car"],
            variable=self.transport_var,
            command=self.update_live_calculation,
            width=90,
            height=26,
            font=ctk.CTkFont(size=10)
        )
        self.transport_menu.grid(row=1, column=2, padx=(0, 8), pady=2)

        self.manual_label = ctk.CTkLabel(
            controls_frame, text="Time (min):", font=ctk.CTkFont(size=10, weight="bold"))
        self.manual_entry = ctk.CTkEntry(
            controls_frame,
            placeholder_text="Minutes",
            width=90,
            height=26,
            font=ctk.CTkFont(size=10)
        )
        self.manual_entry.bind('<KeyRelease>', self.update_live_calculation)

        button_frame = ctk.CTkFrame(config_frame, fg_color="transparent")
        button_frame.grid(row=2, column=0, columnspan=3, pady=6)

        self.start_btn = ctk.CTkButton(
            button_frame,
            text="🚀 START",
            font=ctk.CTkFont(size=12, weight="bold"),
            height=32,
            width=100,
            corner_radius=6,
            fg_color="#4caf50",
            hover_color="#388e3c",
            command=self.start_timer
        )
        self.start_btn.pack(side="left", padx=6)

        self.stop_btn = ctk.CTkButton(
            button_frame,
            text="⏹ STOP",
            font=ctk.CTkFont(size=12, weight="bold"),
            height=32,
            width=80,
            corner_radius=6,
            fg_color="#f44336",
            hover_color="#d32f2f",
            command=self.stop_timer,
            state="disabled"
        )
        self.stop_btn.pack(side="left", padx=6)

        display_frame = ctk.CTkFrame(tab, corner_radius=8)
        display_frame.grid(row=2, column=0, sticky="nsew",
                           padx=15, pady=(0, 15))
        display_frame.grid_rowconfigure(1, weight=1)
        display_frame.grid_columnconfigure(0, weight=1)

        self.phase_label = ctk.CTkLabel(
            display_frame,
            text="⏱️ Ready to Start",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="gray60"
        )
        self.phase_label.grid(row=0, column=0, pady=(8, 2))

        self.time_label = ctk.CTkLabel(
            display_frame,
            text="--:--",
            font=ctk.CTkFont(size=48, weight="bold", family="Consolas"),
            text_color="#4caf50"
        )
        self.time_label.grid(row=1, column=0, pady=3)

        self.progress_bar = ctk.CTkProgressBar(
            display_frame,
            width=300,
            height=10,
            corner_radius=5,
            progress_color="#4caf50"
        )
        self.progress_bar.grid(row=2, column=0, pady=5, padx=25, sticky="ew")
        self.progress_bar.set(0)

        self.status_label = ctk.CTkLabel(
            display_frame,
            text="Configure settings above and click START to begin",
            font=ctk.CTkFont(size=11),
            text_color="gray60",
            wraplength=350
        )
        self.status_label.grid(row=3, column=0, pady=(2, 8))

    def adjust_color(self, hex_color, adjustment):
        """Adjust hex color brightness"""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        rgb = tuple(max(0, min(255, c + adjustment)) for c in rgb)
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

    def on_unit_change(self, choice):
        if choice == "manual":
            self.distance_label.grid_remove()
            self.distance_entry.grid_remove()
            self.transport_label.grid_remove()
            self.transport_menu.grid_remove()

            self.manual_label.grid(
                row=0, column=1, sticky="w", padx=(0, 3), pady=2)
            self.manual_entry.grid(row=1, column=1, padx=(0, 8), pady=2)
        else:
            self.manual_label.grid_remove()
            self.manual_entry.grid_remove()

            self.distance_label.grid(
                row=0, column=1, sticky="w", padx=(0, 3), pady=2)
            self.distance_entry.grid(row=1, column=1, padx=(0, 8), pady=2)
            self.transport_label.grid(
                row=0, column=2, sticky="w", padx=(0, 3), pady=2)
            self.transport_menu.grid(row=1, column=2, padx=(0, 8), pady=2)

        self.update_live_calculation()

    def update_live_calculation(self, event=None):
        """Update the live travel time calculation display"""
        try:
            unit = self.unit_var.get()

            if unit == "manual":
                time_text = self.manual_entry.get().strip()
                if time_text:
                    try:
                        total_minutes = float(time_text)
                        if total_minutes > 0:
                            one_way_str = self.decoy.format_time(
                                int(total_minutes // 60), int(total_minutes % 60), 0)
                            round_trip_minutes = total_minutes * 2
                            round_trip_str = self.decoy.format_time(
                                int(round_trip_minutes // 60), int(round_trip_minutes % 60), 0)

                            calc_text = f"✅ One-way: {one_way_str} | Total round trip: {round_trip_str}\n"
                            calc_text += f"Phase 1: Going to store ({one_way_str}) + Phase 2: Returning home ({one_way_str})"

                            self.live_calc_label.configure(
                                text=calc_text,
                                text_color="#4caf50"
                            )
                            return
                    except ValueError:
                        pass

                self.live_calc_label.configure(
                    text="⏳ Enter travel time in minutes to see calculation",
                    text_color="gray60"
                )
            else:
                distance_text = self.distance_entry.get().strip()
                transport = self.transport_var.get()

                if distance_text:
                    try:
                        distance = float(distance_text)
                        if distance > 0:
                            unit_display = unit

                            travel_time = self.decoy.calculate_travel_time(
                                distance, unit_display, transport)
                            if travel_time:
                                hours, minutes, seconds, total_minutes = travel_time
                                one_way_str = self.decoy.format_time(
                                    hours, minutes, seconds)

                                round_trip_minutes = total_minutes * 2
                                round_trip_str = self.decoy.format_time(
                                    int(round_trip_minutes // 60), int(round_trip_minutes % 60), 0)

                                calc_text = f"✅ {distance} {unit_display} by {transport}\n"
                                calc_text += f"One-way: {one_way_str} | Total round trip: {round_trip_str}\n"
                                calc_text += f"Phase 1: Going to store ({one_way_str}) + Phase 2: Returning home ({one_way_str})"

                                self.live_calc_label.configure(
                                    text=calc_text,
                                    text_color="#4caf50"
                                )
                                return
                    except ValueError:
                        pass

                unit_display = unit
                self.live_calc_label.configure(
                    text=f"⏳ Enter distance in {unit_display} to see live calculation",
                    text_color="gray60"
                )

        except Exception:
            self.live_calc_label.configure(
                text="📊 Configure settings below to see live travel time calculation",
                text_color="gray60"
            )

    def copy_to_clipboard(self, text):
        """Copy text to clipboard"""
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.root.update()
        except Exception:
            pass

    def generate_main_cards(self, card_type, card_name):
        try:
            count = int(self.card_count_var.get()
                        ) if self.card_count_var.get().strip() else 1
            count = max(1, min(count, 100))
        except ValueError:
            count = 1

        cards, card_info = self.decoy.generate(card_type, count)

        if cards:
            self.show_main_card_results(card_type, card_name, cards, card_info)

    def show_main_card_results(self, card_type, card_name, cards, card_info):
        dialog = ctk.CTkToplevel(self.root)
        dialog.title(f"{card_name} Cards Generated" if len(
            cards) > 1 else f"{card_name} Card Generated")

        if len(cards) == 1:
            dialog.geometry("450x400")
            height = 400
        elif len(cards) <= 3:
            dialog.geometry("450x500")
            height = 500
        else:
            dialog.geometry("450x550")
            height = 550

        dialog.transient(self.root)
        dialog.grab_set()
        dialog.resizable(False, False)

        self.center_window(dialog, 450, height)

        header_text = "🎁 Gift Cards Generated!" if len(
            cards) > 1 else "🎁 Gift Card Generated!"
        ctk.CTkLabel(
            dialog,
            text=header_text,
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=(15, 8))

        subtitle_text = f"{len(cards)} {card_name} Cards" if len(
            cards) > 1 else f"{card_name} Card"
        ctk.CTkLabel(
            dialog,
            text=subtitle_text,
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        ).pack()

        cards_frame = ctk.CTkFrame(dialog, corner_radius=8)
        cards_frame.pack(fill="x", padx=15, pady=15)

        if len(cards) == 1:
            ctk.CTkLabel(
                cards_frame,
                text="Gift Card Code:",
                font=ctk.CTkFont(size=12, weight="bold")
            ).pack(pady=(15, 5))

            code_container = ctk.CTkFrame(cards_frame, fg_color="transparent")
            code_container.pack(fill="x", padx=15, pady=(0, 8))

            code_text = ctk.CTkEntry(
                code_container,
                font=ctk.CTkFont(size=14, family="Consolas", weight="bold"),
                height=35,
                justify="center"
            )
            code_text.pack(side="left", fill="x", expand=True, padx=(0, 8))
            code_text.insert(0, cards[0])
            code_text.configure(state="readonly")

            copy_btn = ctk.CTkButton(
                code_container,
                text="📋",
                font=ctk.CTkFont(size=14, weight="bold"),
                width=40,
                height=35,
                fg_color="#4caf50",
                hover_color="#388e3c",
                command=lambda: self.copy_to_clipboard(cards[0])
            )
            copy_btn.pack(side="right")

        else:
            ctk.CTkLabel(
                cards_frame,
                text="Generated Codes:",
                font=ctk.CTkFont(size=12, weight="bold")
            ).pack(pady=(15, 8))

            scrollable_frame = ctk.CTkScrollableFrame(cards_frame, height=200)
            scrollable_frame.pack(fill="x", padx=15, pady=(0, 8))

            for i, card in enumerate(cards, 1):
                card_row = ctk.CTkFrame(
                    scrollable_frame, fg_color="transparent")
                card_row.pack(fill="x", pady=2)

                ctk.CTkLabel(
                    card_row,
                    text=f"{i}.",
                    font=ctk.CTkFont(size=11, weight="bold"),
                    width=25
                ).pack(side="left", padx=(5, 0))

                code_text = ctk.CTkEntry(
                    card_row,
                    font=ctk.CTkFont(
                        size=11, family="Consolas", weight="bold"),
                    height=30
                )
                code_text.pack(side="left", fill="x", expand=True, padx=5)
                code_text.insert(0, card)
                code_text.configure(state="readonly")

                copy_btn = ctk.CTkButton(
                    card_row,
                    text="📋",
                    font=ctk.CTkFont(size=10, weight="bold"),
                    width=30,
                    height=30,
                    fg_color="#4caf50",
                    hover_color="#388e3c",
                    command=lambda c=card: self.copy_to_clipboard(c)
                )
                copy_btn.pack(side="right", padx=(0, 5))

        test_url = card_info.get('test_url')
        if test_url:
            ctk.CTkLabel(
                cards_frame,
                text=f"Test at: {test_url}",
                font=ctk.CTkFont(size=10),
                text_color="gray60"
            ).pack(pady=(0, 8))

        warning_text = "⚠️ FAKE CODES - Test first to ensure invalid!" if len(
            cards) > 1 else "⚠️ FAKE CODE - Test first to ensure invalid!"
        ctk.CTkLabel(
            cards_frame,
            text=warning_text,
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="#ff6b35"
        ).pack(pady=(0, 15))

        ctk.CTkButton(
            dialog,
            text="CLOSE",
            font=ctk.CTkFont(size=12, weight="bold"),
            height=35,
            width=100,
            command=dialog.destroy
        ).pack(pady=(0, 15))

    def open_card_generator(self, card_type, card_name):
        dialog = ctk.CTkToplevel(self.root)
        dialog.title(f"Generate {card_name} Cards")
        dialog.geometry("550x650")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.resizable(False, False)

        self.center_window(dialog, 550, 650)

        header_frame = ctk.CTkFrame(dialog, corner_radius=10, height=80)
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        header_frame.pack_propagate(False)

        ctk.CTkLabel(
            header_frame,
            text=f"Generate {card_name} Cards",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=20)

        input_frame = ctk.CTkFrame(dialog, corner_radius=10)
        input_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            input_frame,
            text="Number of cards to generate:",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(pady=(20, 5))

        count_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Enter number (default: 1)",
            width=200,
            font=ctk.CTkFont(size=14),
            justify="center"
        )
        count_entry.pack(pady=(0, 20))

        generate_btn = ctk.CTkButton(
            input_frame,
            text="GENERATE CARDS",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=45,
            command=lambda: self.generate_cards_gui(
                card_type, count_entry, result_text)
        )
        generate_btn.pack(pady=(0, 20))

        results_frame = ctk.CTkFrame(dialog, corner_radius=10)
        results_frame.pack(fill="both", expand=True, padx=20, pady=10)

        ctk.CTkLabel(
            results_frame,
            text="Generated Cards:",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(pady=(20, 10))

        result_text = ctk.CTkTextbox(
            results_frame,
            height=300,
            font=ctk.CTkFont(size=12, family="Consolas"),
            wrap="word"
        )
        result_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        ctk.CTkButton(
            dialog,
            text="CLOSE",
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            width=100,
            command=dialog.destroy
        ).pack(pady=(0, 20))

    def generate_cards_gui(self, card_type, count_entry, result_text):
        try:
            count = int(count_entry.get()) if count_entry.get().strip() else 1
            count = max(1, min(count, 100))
        except ValueError:
            count = 1

        cards, card_info = self.decoy.generate(card_type, count)

        if cards:
            result_text.delete("1.0", "end")

            result_text.insert(
                "1.0", f"Generated {len(cards)} {card_type.upper()} cards:\n")
            result_text.insert("end", "=" * 50 + "\n\n")

            for i, card in enumerate(cards, 1):
                result_text.insert("end", f"{i:2d}. {card}\n")

            result_text.insert("end", "\n" + "=" * 50 + "\n")

            test_url = card_info.get('test_url')
            if test_url:
                result_text.insert("end", f"Test at: {test_url}\n")

            result_text.insert(
                "end", "\nIMPORTANT: Test these codes first to ensure they are invalid!\n")
            result_text.insert(
                "end", "These are FAKE codes for scambaiting purposes only.")

    def start_timer(self):
        if self.timer_active:
            return

        try:
            if self.unit_var.get() == "manual":
                time_text = self.manual_entry.get().strip()
                if not time_text:
                    self.show_error(
                        "Missing Time", "Please enter travel time in minutes.")
                    return
                total_minutes = float(time_text)
                if total_minutes <= 0:
                    raise ValueError("Time must be positive")
            else:
                distance_text = self.distance_entry.get().strip()
                if not distance_text:
                    self.show_error("Missing Distance",
                                    "Please enter a distance value.")
                    return
                distance = float(distance_text)
                if distance <= 0:
                    raise ValueError("Distance must be positive")

                unit = self.unit_var.get()
                transport = self.transport_var.get()

                travel_time = self.decoy.calculate_travel_time(
                    distance, unit, transport)
                if not travel_time:
                    raise ValueError("Could not calculate travel time")

                _, _, _, total_minutes = travel_time

        except (ValueError, TypeError) as e:
            error_msg = str(e) if str(e) != "Time must be positive" and str(
                e) != "Distance must be positive" else "Please enter valid positive numbers for all fields."
            self.show_error("Invalid Input", error_msg)
            return

        self.timer_active = True
        self.total_seconds = int(total_minutes * 60)
        self.remaining_seconds = self.total_seconds
        self.current_phase = "Going to store"

        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self.phase_label.configure(
            text="🚗 Going to store...", text_color="#ff9800")
        self.status_label.configure(
            text="Phase 1: Journey started - Tell the scammer you're heading to the store!")

        self.update_timer()

    def update_timer(self):
        if not self.timer_active:
            return

        hours = self.remaining_seconds // 3600
        minutes = (self.remaining_seconds % 3600) // 60
        seconds = self.remaining_seconds % 60

        if hours > 0:
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            time_str = f"{minutes:02d}:{seconds:02d}"

        self.time_label.configure(text=time_str)

        progress = 1 - (self.remaining_seconds / self.total_seconds)
        self.progress_bar.set(progress)

        if self.remaining_seconds <= 0:
            self.phase_complete()
            return

        self.remaining_seconds -= 1
        self.timer_job = self.root.after(1000, self.update_timer)

    def phase_complete(self):
        self.decoy.play_sound()
        self.bring_gui_to_foreground()

        if self.current_phase == "Going to store":
            self.show_store_reached_dialog()
        else:
            self.timer_complete()

    def start_return_phase(self):
        self.current_phase = "Returning home"
        self.remaining_seconds = self.total_seconds
        self.phase_label.configure(
            text="🏠 Returning home...", text_color="#4caf50")
        self.status_label.configure(
            text="Return journey - Tell the scammer you're coming back!")
        self.progress_bar.set(0)
        self.update_timer()

    def timer_complete(self):
        self.timer_active = False
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")

        self.phase_label.configure(
            text="✅ Timer Complete!", text_color="#4caf50")
        self.time_label.configure(text="DONE")
        self.progress_bar.set(1)
        self.status_label.configure(
            text="You can now tell the scammer you're back with the gift card!")

        self.show_completion_dialog()

    def show_store_reached_dialog(self):
        dialog = ctk.CTkToplevel(self.root)
        dialog.title("Store Reached!")
        dialog.geometry("380x280")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.resizable(False, False)

        self.center_window(dialog, 380, 280)

        ctk.CTkLabel(
            dialog,
            text="🏪",
            font=ctk.CTkFont(size=40)
        ).pack(pady=(15, 8))

        ctk.CTkLabel(
            dialog,
            text="Store Reached!",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=8)

        ctk.CTkLabel(
            dialog,
            text="You've reached the store!\nWhat would you like to do next?",
            font=ctk.CTkFont(size=12),
            justify="center"
        ).pack(pady=15)

        button_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        button_frame.pack(pady=15)

        generate_btn = ctk.CTkButton(
            button_frame,
            text="🎁 GENERATE GIFT CARD",
            font=ctk.CTkFont(size=12, weight="bold"),
            height=40,
            width=180,
            fg_color="#4caf50",
            hover_color="#388e3c",
            command=lambda: [dialog.destroy(), self.show_gift_card_selection()]
        )
        generate_btn.pack(pady=4)

        return_btn = ctk.CTkButton(
            button_frame,
            text="🏠 START RETURN TRIP",
            font=ctk.CTkFont(size=12, weight="bold"),
            height=40,
            width=180,
            command=lambda: [dialog.destroy(), self.start_return_phase()]
        )
        return_btn.pack(pady=4)

    def show_gift_card_selection(self):
        dialog = ctk.CTkToplevel(self.root)
        dialog.title("Select Gift Card Type")
        dialog.geometry("350x500")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.resizable(False, False)

        self.center_window(dialog, 350, 500)

        ctk.CTkLabel(
            dialog,
            text="🎁 Generate Gift Card",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=(15, 8))

        ctk.CTkLabel(
            dialog,
            text="Select gift card type:",
            font=ctk.CTkFont(size=12)
        ).pack(pady=(0, 15))

        cards_frame = ctk.CTkFrame(dialog)
        cards_frame.pack(fill="both", expand=True, padx=15, pady=10)

        card_types = [
            ("Xbox Live", "xbox", "#107c10"),
            ("PlayStation", "psn", "#003791"),
            ("Amazon", "amazon", "#ff9900"),
            ("Google Play", "google-play", "#34a853"),
            ("Apple iTunes", "apple", "#000000"),
            ("Steam", "steam", "#1b2838"),
            ("Walmart", "walmart", "#0071ce"),
            ("Target", "target", "#cc0000"),
            ("Visa Gift Card", "visa", "#1a1f71")
        ]

        for name, code, color in card_types:
            btn = ctk.CTkButton(
                cards_frame,
                text=name,
                font=ctk.CTkFont(size=12, weight="bold"),
                fg_color=color,
                hover_color=self.adjust_color(color, -20),
                height=35,
                width=280,
                corner_radius=6,
                command=lambda c=code, n=name: [
                    dialog.destroy(), self.generate_from_timer(c, n)]
            )
            btn.pack(pady=3, padx=15)

        ctk.CTkButton(
            dialog,
            text="CLOSE",
            font=ctk.CTkFont(size=12, weight="bold"),
            height=35,
            width=80,
            command=dialog.destroy
        ).pack(pady=15)

    def generate_from_timer(self, card_type, card_name):
        cards, card_info = self.decoy.generate(card_type, 1)

        if cards:
            result_dialog = ctk.CTkToplevel(self.root)
            result_dialog.title(f"{card_name} Card Generated")
            result_dialog.geometry("450x350")
            result_dialog.transient(self.root)
            result_dialog.grab_set()
            result_dialog.resizable(False, False)

            self.center_window(result_dialog, 450, 350)

            ctk.CTkLabel(
                result_dialog,
                text="🎁 Gift Card Generated!",
                font=ctk.CTkFont(size=20, weight="bold")
            ).pack(pady=(15, 8))

            ctk.CTkLabel(
                result_dialog,
                text=f"{card_name} Gift Card",
                font=ctk.CTkFont(size=14),
                text_color="gray70"
            ).pack()

            card_frame = ctk.CTkFrame(result_dialog, corner_radius=8)
            card_frame.pack(fill="x", padx=15, pady=15)

            ctk.CTkLabel(
                card_frame,
                text="Gift Card Code:",
                font=ctk.CTkFont(size=12, weight="bold")
            ).pack(pady=(15, 5))

            code_container = ctk.CTkFrame(card_frame, fg_color="transparent")
            code_container.pack(fill="x", padx=15, pady=(0, 8))

            code_text = ctk.CTkEntry(
                code_container,
                font=ctk.CTkFont(size=14, family="Consolas", weight="bold"),
                height=35,
                justify="center"
            )
            code_text.pack(side="left", fill="x", expand=True, padx=(0, 8))
            code_text.insert(0, cards[0])
            code_text.configure(state="readonly")

            copy_btn = ctk.CTkButton(
                code_container,
                text="📋",
                font=ctk.CTkFont(size=14, weight="bold"),
                width=40,
                height=35,
                fg_color="#4caf50",
                hover_color="#388e3c",
                command=lambda: self.copy_to_clipboard(cards[0])
            )
            copy_btn.pack(side="right")

            test_url = card_info.get('test_url')
            if test_url:
                ctk.CTkLabel(
                    card_frame,
                    text=f"Test at: {test_url}",
                    font=ctk.CTkFont(size=10),
                    text_color="gray60"
                ).pack(pady=(0, 8))

            ctk.CTkLabel(
                card_frame,
                text="⚠️ FAKE CODE - Test first to ensure it's invalid!",
                font=ctk.CTkFont(size=10, weight="bold"),
                text_color="#ff6b35"
            ).pack(pady=(0, 15))

            button_frame = ctk.CTkFrame(result_dialog, fg_color="transparent")
            button_frame.pack(pady=15)

            ctk.CTkButton(
                button_frame,
                text="🏠 START RETURN",
                font=ctk.CTkFont(size=12, weight="bold"),
                height=35,
                width=140,
                command=lambda: [
                    result_dialog.destroy(), self.start_return_phase()]
            ).pack(side="left", padx=8)

            ctk.CTkButton(
                button_frame,
                text="🎁 GENERATE ANOTHER",
                font=ctk.CTkFont(size=12, weight="bold"),
                height=35,
                width=160,
                fg_color="#4caf50",
                hover_color="#388e3c",
                command=lambda: [
                    result_dialog.destroy(), self.show_gift_card_selection()]
            ).pack(side="left", padx=8)

    def stop_timer(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)

        self.timer_active = False
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")

        self.phase_label.configure(text="⏸ Timer Stopped", text_color="gray60")
        self.status_label.configure(
            text="Timer stopped. Configure settings and click START TIMER to begin.")
        self.progress_bar.set(0)

    def show_phase_dialog(self, title, message, button_text, callback):
        dialog = ctk.CTkToplevel(self.root)
        dialog.title(title)
        dialog.geometry("400x250")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.resizable(False, False)

        self.center_window(dialog, 400, 250)

        ctk.CTkLabel(
            dialog,
            text=title,
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=(30, 10))

        ctk.CTkLabel(
            dialog,
            text=message,
            font=ctk.CTkFont(size=14),
            wraplength=350
        ).pack(pady=20, padx=20)

        ctk.CTkButton(
            dialog,
            text=button_text,
            font=ctk.CTkFont(size=16, weight="bold"),
            height=45,
            width=200,
            command=lambda: [callback(), dialog.destroy()]
        ).pack(pady=20)

    def show_completion_dialog(self):
        dialog = ctk.CTkToplevel(self.root)
        dialog.title("Timer Complete!")
        dialog.geometry("450x300")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.resizable(False, False)

        self.center_window(dialog, 450, 300)

        ctk.CTkLabel(
            dialog,
            text="🎉",
            font=ctk.CTkFont(size=48)
        ).pack(pady=(30, 10))

        ctk.CTkLabel(
            dialog,
            text="Timer Complete!",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=10)

        ctk.CTkLabel(
            dialog,
            text="You can now tell the scammer you're back\nwith the gift card and ready to provide the codes!",
            font=ctk.CTkFont(size=14),
            wraplength=400,
            justify="center"
        ).pack(pady=20, padx=20)

        ctk.CTkButton(
            dialog,
            text="AWESOME!",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=45,
            width=150,
            command=dialog.destroy
        ).pack(pady=20)

    def show_error(self, title, message):
        dialog = ctk.CTkToplevel(self.root)
        dialog.title(title)
        dialog.geometry("350x200")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.resizable(False, False)

        self.center_window(dialog, 350, 200)

        ctk.CTkLabel(
            dialog,
            text="⚠️",
            font=ctk.CTkFont(size=32)
        ).pack(pady=(20, 10))

        ctk.CTkLabel(
            dialog,
            text=title,
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack()

        ctk.CTkLabel(
            dialog,
            text=message,
            font=ctk.CTkFont(size=12),
            wraplength=300
        ).pack(pady=20, padx=20)

        ctk.CTkButton(
            dialog,
            text="OK",
            command=dialog.destroy
        ).pack(pady=(0, 20))

    def center_window(self, window, width, height):
        window.update_idletasks()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def bring_gui_to_foreground(self):
        """Bring the GUI window to the front"""
        try:
            self.root.lift()
            self.root.attributes('-topmost', True)
            self.root.after(
                100, lambda: self.root.attributes('-topmost', False))
            self.root.focus_force()

            system = platform.system().lower()
            if system == 'windows':
                try:
                    import ctypes
                    from ctypes import wintypes

                    user32 = ctypes.WinDLL('user32', use_last_error=True)

                    hwnd = self.root.winfo_id()
                    if hwnd:
                        user32.SetForegroundWindow(hwnd)
                        user32.ShowWindow(hwnd, 9)
                except:
                    pass
            elif system == 'darwin':
                subprocess.run(['osascript', '-e', 'tell application "Python" to activate'],
                               capture_output=True, check=False)
            elif system == 'linux':
                try:
                    subprocess.run(['wmctrl', '-a', self.root.title()],
                                   capture_output=True, check=False)
                except:
                    pass
        except Exception:
            pass

    def run(self):
        self.root.mainloop()


def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() in ['--gui', '-g', 'gui']:
        if GUI_AVAILABLE:
            app = DecoyCardsGUI()
            app.run()
            return
        else:
            print("GUI not available. Please install customtkinter:")
            print("pip install customtkinter")
            return

    decoy = DecoyCards()

    decoy.clear_screen()
    print("DecoyCards - Made by Baitrix")
    print("WARNING: These are fake codes for scambaiting only")
    if GUI_AVAILABLE:
        print("Tip: Run with '--gui' or '-g' for graphical interface")
    print()

    card_types = {
        '1': 'xbox', '2': 'psn', '3': 'amazon', '4': 'google-play',
        '5': 'apple', '6': 'steam', '7': 'walmart', '8': 'target', '9': 'visa'
    }

    while True:
        print("GIFT CARDS:")
        print("1. Xbox Live")
        print("2. PlayStation Network")
        print("3. Amazon")
        print("4. Google Play")
        print("5. Apple/iTunes")
        print("6. Steam")
        print("7. Walmart")
        print("8. Target")
        print("9. Visa")
        print()
        print("TOOLS:")
        print("T. Store Timer")
        if GUI_AVAILABLE:
            print("G. Launch GUI")
        print("0. Exit")

        choice = input(
            f"\nSelect (1-9, T{', G' if GUI_AVAILABLE else ''}) or 0 to exit: ").strip().lower()

        if choice == '0':
            break

        if choice == 'g' and GUI_AVAILABLE:
            app = DecoyCardsGUI()
            app.run()
            decoy.clear_screen()
            print("DecoyCards - Made by Baitrix")
            print("WARNING: These are fake codes for scambaiting only")
            if GUI_AVAILABLE:
                print("Tip: Run with '--gui' or '-g' for graphical interface")
            print()
            continue

        if choice == 't':
            decoy.store_timer()
            decoy.clear_screen()
            print("DecoyCards - Made by Baitrix")
            print("WARNING: These are fake codes for scambaiting only")
            if GUI_AVAILABLE:
                print("Tip: Run with '--gui' or '-g' for graphical interface")
            print()
            continue

        if choice not in card_types:
            print("Invalid choice")
            input("Press Enter to continue...")
            decoy.clear_screen()
            print("DecoyCards - Made by Baitrix")
            print("WARNING: These are fake codes for scambaiting only")
            if GUI_AVAILABLE:
                print("Tip: Run with '--gui' or '-g' for graphical interface")
            print()
            continue

        card_type = card_types[choice]

        try:
            count = int(input("How many cards? (default 1): ") or "1")
            if count <= 0:
                count = 1
        except ValueError:
            count = 1

        cards, card_info = decoy.generate(card_type, count)

        if cards:
            print(f"\nGenerated {len(cards)} {card_type} cards:")
            for i, card in enumerate(cards, 1):
                print(f"{i}. {card}")

            test_url = card_info.get('test_url')
            if test_url:
                print(f"\nTest at: {test_url}")

            print("IMPORTANT: Test these codes first to ensure they are invalid")

        input("\nPress Enter to continue...")
        decoy.clear_screen()
        print("DecoyCards - Made by Baitrix")
        print("WARNING: These are fake codes for scambaiting only")
        if GUI_AVAILABLE:
            print("Tip: Run with '--gui' or '-g' for graphical interface")
        print()


if __name__ == "__main__":
    main()
