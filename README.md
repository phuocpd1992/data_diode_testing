# Data Diode Testing

This project provides a Python script to test the functionality of a Data Diode (one-way optical data isolation device).
The default setting parameters of the Only Send Module:
IP_HOST = "192.168.1.1"   # Modbus TCP server IP  
PORT = 502                # Modbus TCP port  
UNIT_ID = 1               # Modbus server Unit ID  
TOTAL_ELEMENTS = 1000     # Total number of elements to process  
MAX_REGISTER = 100        # Maximum registers per request  

---

## 🚀 How to Run

1. **Clone the repository**  
   git clone https://github.com/phuocpd1992/data_diode_testing.git  
   cd data_diode_testing  

2. **Create a virtual environment (recommended)**  
   python -m venv venv  

3. **Activate the environment**  
   - On Windows: venv\Scripts\activate  
   - On macOS/Linux: source venv/bin/activate  

4. **Install dependencies**  
   pip install -r requirements.txt  

5. **Run the program**  
   python send_test_data.py  

---

## 📂 Project Structure
```data_diode_testing/
│-- send_test_data.py # Main entry point of the program
│-- requirements.txt # List of required dependencies
│-- README.md # Documentation
```
---

## 🛠 Requirements
- Python 3.10+

