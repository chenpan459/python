import serial
import time

#############################################
#pip install pyserial # 安装依赖库
#############################################
def open_serial(port='/dev/ttyUSB0', baudrate=115200, timeout=1):
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        print(f"串口 {port} 已打开，波特率 {baudrate}")
        return ser
    except serial.SerialException as e:
        print(f"串口打开失败: {e}")
        return None

def run_serial_listener(ser):
    while True:
        if ser.in_waiting:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            print(f"收到: {line}")
            
            # 识别输入内容
            if line.lower() == "ping":
                ser.write(b"pong\n")
                print("回应: pong")
            elif "hello" in line.lower():
                ser.write(b"Hi there!\n")
                print("回应: Hi there!")
            elif line.lower() == "exit":
                print("收到退出指令，关闭串口")
                break

        time.sleep(0.1)  # 减少 CPU 占用

if __name__ == "__main__":
    # 根据实际设备修改串口名称
    serial_port = open_serial(port='/dev/ttyUSB0', baudrate=9600)
    if serial_port:
        try:
            run_serial_listener(serial_port)
        finally:
            serial_port.close()
            print("串口已关闭")
