import serial

cad_arduino = '100101'
arduino = serial.Serial('COM3', 9600, timeout=1)
if not arduino is None:
    arduino.write(cad_arduino.encode())
    arduino.close()