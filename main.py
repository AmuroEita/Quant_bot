from common.utils import place_order,send_to_telegram,get_signal,get_signal_fast
import time
import os
from datetime import datetime

if __name__ == '__main__':
    while True:
        side,n1,n2 = get_signal_fast() 
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        print()
        print(f'<Quant bot> side:{side} n1:{n1} n2:{n2} current_time:{date_time}') 
        
        if side != 'PASS':
            send_to_telegram(message=side)
            place_order(side) 
        time.sleep(60*15)
        os.system("cls") 