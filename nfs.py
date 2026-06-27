import os
import sys
import time
import random
from datetime import datetime
                                                                           # --- VOLATILE IN-MEMORY DATA STORAGE ONLY ---
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",                              "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
]

# GLOBAL METRIC COUNTERS
total_packets_sent = 0
successful_hits = 0    # Status 200
client_errors = 0      # Status 4xx
server_failures = 0    # Status 5xx

def clear_screen():
    """Clears the terminal screen dynamically across all operating systems."""
    os.system("cls" if os.name == "nt" else "clear")

def display_dashboard():
    """Renders the minimalist layout showing only the NSF logo and author."""
    clear_screen()
    print("=" * 65)
    print("  ███╗   ██╗███████╗███████╗")
    print("  ████╗  ██║██╔════╝██╔════╝     [ AUTHOR: BA313 ]")
    print("  ██╔██╗ ██║███████╗█████╗  ")
    print("  ██║╚██╗██║╚════██║██╔══╝  ")
    print("  ██║ ╚████║███████║██║     ")
    print("  ╚═╝  ╚═══╝╚══════╝╚═╝     ")
    print("=" * 65)

def display_live_analytics(current_target):
    """Renders a flash telemetry panel instantly following any stream completion."""
    success_pct = (successful_hits / total_packets_sent * 100) if total_packets_sent > 0 else 0.0
    print("\n" + "-" * 65)
    print("📊            NSF INTERIM OPERATION TELEMETRY            📊")
    print("-" * 65)
    print(f"📡 ACTIVE TARGET PROFILE : {current_target}")
    print(f"📈 PACKETS SENT THIS RUN : {total_packets_sent}")
    print(f"✅ SUCCESSFUL SECTORS    : {successful_hits} ({success_pct:.1f}%)")
    print(f"⚠️  CLIENT INCEPTIONS    : {client_errors}")
    print(f"🔥 TOTAL DESTABILIZATIONS: {server_failures}")
    print("-" * 65)

def simulate_network_response(worker_id, thread_id):
    """Generates realistic HTTP network status codes with live timestamps."""
    global total_packets_sent, successful_hits, client_errors, server_failures

    total_packets_sent += 1
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    codes = [
        {"code": 200, "msg": "OK - Target Vulnerable", "type": "success"},
        {"code": 400, "msg": "Bad Request", "type": "client"},
        {"code": 403, "msg": "Forbidden - WAF Blocked", "type": "client"},
        {"code": 404, "msg": "Not Found", "type": "client"},
        {"code": 500, "msg": "Internal Server Error", "type": "server"},
        {"code": 503, "msg": "Service Unavailable", "type": "server"}
    ]

    rolled_list = random.choices(codes, weights=[65, 10, 10, 5, 5, 5], k=1)
    rolled_status = rolled_list[0]

    if rolled_status["type"] == "success":
        successful_hits += 1
        indicator = "🟢 [SUCCESS]"
    elif rolled_status["type"] == "client":
        client_errors += 1
        indicator = "🟡 [WARNING]"
    else:
        server_failures += 1
        indicator = "🔴 [CRITICAL]"

    print(f"    └─> [{current_time}] [W-{worker_id}/T-{thread_id}] {indicator} HTTP/{rolled_status['code']} - {rolled_status['msg']}")

def parse_input_param(prompt_text, default_val):
    """Handles universal input conversion supporting strings like 'inf' or numbers."""
    val = input(prompt_text).strip().lower()
    if not val:
        return default_val
    if val in ["inf", "infinite"]:
        return "infinite"
    try:
        int_val = int(val)
        return int_val if int_val > 0 else default_val
    except ValueError:
        return default_val

def configure_target_session(target, delay, attack_time, workers, threads):
    """Prompt workflow sequence updating configurations inside localized memory states."""
    print("\n🛠  [NSF TARGET CALIBRATION REQUIRED]")
    print("-" * 45)

    raw_target = input("[+] Enter Target IP or Domain (Default 127.0.0.1): ").strip()
    target = raw_target if raw_target else "127.0.0.1"

    try:
        user_delay = input("[+] Set Loop Delay (seconds, Default 2): ").strip()
        delay = int(user_delay) if user_delay else 2
    except ValueError:
        delay = 2

    attack_time = parse_input_param("[+] Set Attack Window (seconds or 'inf', Default 10): ", 10)
    workers = parse_input_param("[+] Allocate Simulated Workers (number or 'inf', Default 2): ", 2)
    threads = parse_input_param("[+] Set Threads per Worker (number or 'inf', Default 4): ", 4)

    return target, delay, attack_time, workers, threads

def execute_stream_loop(target, delay, attack_time, workers, threads):
    """A single execution block handler managing flexible loop timers for the flood vector."""
    is_infinite_time = (str(attack_time).lower() == "infinite")
    start_time = time.time()

    try:
        while is_infinite_time or (time.time() - start_time) < float(attack_time):
            w_id = random.randint(1, int(workers)) if str(workers).isdigit() else random.randint(1, 9999)
            t_id = random.randint(1, int(threads)) if str(threads).isdigit() else random.randint(1, 999)
            selected_agent = random.choice(USER_AGENTS)

            print(f"\n   [+] Packet payload vector dispatched:")
            print(f"       ├── Target Host: http://{target}/index.php")
            print(f"       └── User-Agent : {selected_agent[:45]}...")

            simulate_network_response(w_id, t_id)

            sleep_dur = (delay / 10) if delay > 0 else 0.02
            time.sleep(sleep_dur)

        if not is_infinite_time:
            print(f"\n⏱️  [COMPLETE] Timed attack window threshold reached ({attack_time}s elapsed).")
            # FIXED: Triggers live metric review instantly upon timer finish condition
            display_live_analytics(target)
    except KeyboardInterrupt:
        print("\n\n🟢 [PAUSED] Transmission sequence interrupted by operator safely.")
        # FIXED: Triggers live metric review instantly upon forced keyboard interrupt cancellation
        display_live_analytics(target)

def pause_and_return():
    """Helper utility to hold the screen output before looping back."""
    input("\n[📌] Press ENTER to return to Tactical Control...")

def main():
    target = "NOT SET"
    delay = 2
    workers = 2
    threads = 4
    attack_time = 10

    while True:
        display_dashboard()

        print("1️⃣ Execute Spoofed HTTP Flood")
        print("2️⃣ Shift Target IP/Domain")
        print("3️⃣ Full Performance Re-Calibration")
        print("4️⃣ Secure Terminal Wipe & Session Final Report")
        print("-" * 65)

        choice = input("[>] Select strategic vector [1-4]: ").strip()

        # VECTOR 1: ATTACK DISPATCH
        if choice == "1":
            target, delay, attack_time, workers, threads = configure_target_session(
                target, delay, attack_time, workers, threads
            )

            print(f"\n🔥 Deploying packet payload arrays to {target}...")
            print("🛑 Stream active. Press [CTRL + C] to return to the option menu.")
            time.sleep(1)
            execute_stream_loop(target, delay, attack_time, workers, threads)
            pause_and_return()

        # VECTOR 2: QUICK TARGET SHIFT
        elif choice == "2":
            new_target = input("\n[+] Feed new destination target: ").strip()
            if new_target:
                target = new_target
                print(f"🟢 Context initialized. Target shifted to: {target}")
            time.sleep(1.5)

        # VECTOR 3: PERFORMANCE TUNING
        elif choice == "3":
            print("\n⚙️ --- CALIBRATION INTERFACE ---")
            try:
                new_delay = input("[+] Feed loop delay threshold in seconds: ").strip()
                if new_delay:
                    delay = int(new_delay)
            except ValueError:
                print("❌ Invalid input type. Keeping existing delay parameter.")

            attack_time = parse_input_param("[+] Re-set Attack Window Duration (seconds or 'inf'): ", attack_time)
            workers = parse_input_param("[+] Adjust Worker allocation scale (number or 'inf'): ", workers)
            threads = parse_input_param("[+] Adjust Threads scale (number or 'inf'): ", threads)
            print("🟢 Operational properties synchronized successfully.")
            time.sleep(1.5)

        # VECTOR 4: DISCONNECT & METRICS
        elif choice == "4":
            print("\n" + "🧹" + " Cleaning system blocks...")
            time.sleep(1)
            clear_screen()

            success_pct = (successful_hits / total_packets_sent * 100) if total_packets_sent > 0 else 0.0

            print("=" * 65)
            print("📊        NSF OPERATIONAL SESSION METRICS REPORT        📊")
            print("=" * 65)
            print(f"👤 LEAD INVESTIGATOR: BA313")
            print(f"📡 FINAL TARGET LOGGED: {target}")
            print("-" * 65)
            print(f"📈 TOTAL SIMULATED PACKETS TRANSMITTED : {total_packets_sent}")
            print(f"✅ SUCCESSFUL TARGET HITS (HTTP 200)  : {successful_hits} ({success_pct:.1f}%)")
            print(f"⚠️  CLIENT INTERCEPTIONS   (HTTP 4xx)  : {client_errors}")
            print(f"🔥 TOTAL SERVICE BREAKDOWNS (HTTP 5xx) : {server_failures}")
            print("=" * 65)
            print("💥 WORKSPACE VOLATILE STORAGE Wiped. ZERO LOGS SAVED ON DEVICE DISK.")
            print("👋 Terminal session closed. Goodbye.")
            sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🚨 Hard abort registered. Disconnecting safely.")
        sys.exit(0)
