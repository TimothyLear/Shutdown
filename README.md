# Shutdown Button & Resistor Detect

Momentary button connected to GPIO3 and GND
    
    performs pi/shutdown/shutdown and awakes from halted state
    
Pull Down resistor connected to GPIO4,GND, and power supply 5v
   
    detects power outage and performs pi/shutdown/shutdown 


Create Shutdown.py file with     
    
    sudo shutdow.py

Make script run on boot
   
    sudo mv shutdown.py /usr/local/bin/

Make executable            
    
    sudo chmod +x /usr/local/bin/shutdown.py

Script to Start/Stop   
 
    sudo shutdown.sh

Make script run on boot   

    sudo mv shutdown.sh /etc/init.d/

Make executable 

    sudo chmod +x /etc/init.d/shutdown.sh

    sudo update-rc.d shutdown.sh defaults

Terminal command to run manually 

    sudo /etc/init.d/shutdown.sh start
