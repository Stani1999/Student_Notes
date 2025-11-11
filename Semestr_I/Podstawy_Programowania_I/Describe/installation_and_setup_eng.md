# **Python Installation**
To run the Bike Rental System, ensure Python is installed on your system.

#### **Windows**
1. Download the installer:
   <div style="text-align: left;">
      <img src="python.png" alt="Python" />
   </div> 
2. Run the installer and check the box for **"Add Python to PATH"**.
3. Click **Install Now**.

#### **Linux (Debian/Ubuntu-based)**
1. Open a terminal and run:
    ```bash
    sudo apt update
    sudo apt install python3
    ```

---

## **Environment Setup**
It is recommended to use virtual environments to isolate project dependencies.

### **Creating and Activating a Virtual Environment**
#### **Windows**
1. Create a virtual environment:
    ```bash
    python -m venv env
    ```
2. Activate the environment:
    ```bash
    env\Scripts\activate
    ```

#### **Linux/macOS**
1. Create a virtual environment:
    ```bash
    python3 -m venv env
    ```
2. Activate the environment:
    ```bash
    source env/bin/activate
    ```

---