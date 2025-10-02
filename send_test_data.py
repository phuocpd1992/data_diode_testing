import time
from pyModbusTCP.client import ModbusClient
from datetime import datetime

# ===================== CONFIGURATION =====================
IP_HOST = "192.168.1.1"
PORT = 502
UNIT_ID = 1
TOTAL_ELEMENTS = 1000
MAX_REGISTER = 100

# ===================== PREPARE DATA =====================
elements = list(range(1, TOTAL_ELEMENTS + 1))

# ===================== HELPER FUNCTION =====================
def transform_string_to_list(input_string):
    return [int(x) for x in input_string.split(',') if x.strip()]

# ===================== TCP CONNECTION FUNCTION =====================
def connect_tcp():
    tcp_client = ModbusClient(host=IP_HOST, port=PORT, unit_id=UNIT_ID, auto_open=True)
    if tcp_client.open():
        print("Connected to Modbus TCP server")
        return tcp_client
    else:
        print("Failed to connect, retrying...")
        return None

# ===================== SEND DATA INFINITE LOOP =====================
tcp = None
run_count = 0  # Count the number of full cycles

while True:
    if tcp is None or not tcp.is_open:
        tcp = connect_tcp()
        if tcp is None:
            time.sleep(1)
            continue

    run_count += 1
    start_time = datetime.now()

    # Split data into batches
    batches = [elements[i:i + MAX_REGISTER] for i in range(0, TOTAL_ELEMENTS, MAX_REGISTER)]

    # Write each batch (errors are logged only once per batch)
    for index, batch in enumerate(batches):
        combined_string = "1" + str(index) + ',' + ','.join(map(str, batch))
        try:
            tcp.write_multiple_registers(0, transform_string_to_list(combined_string))
            print(f"batch {index} : {combined_string}")
        except Exception:
            # Only print error once per batch instead of every number
            print(f"[Warning] Failed to write batch {index}")
            continue

    # Print summary per cycle
    end_time = datetime.now()
    elapsed_ms = (end_time - start_time).total_seconds() * 1000
    print(f"Cycle {run_count}: Sent {TOTAL_ELEMENTS} numbers in {elapsed_ms:.2f} ms")

    # Optional: small pause between cycles
    time.sleep(0.1)
