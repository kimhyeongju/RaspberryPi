from bluetooth import * 

class BtSocket(BluetoothSocket) :
    def __init__(self, *args):
        super().__init__(*args)
        self.buf = ''

    def readline(self):
        ix = self.buf.find('\r\n') 
        if ix != -1 :
            line = self.buf[:ix]
            self.buf = self.buf[ix+2:]
            return line

        self.buf += self.recv(1024).decode()
        return self.readline()
