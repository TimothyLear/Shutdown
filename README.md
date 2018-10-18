# Shutdown Button & Resistor Detect

Momentary button connected to GPIO3 and GND
    
    performs pi/shutdown/shutdown and awakes from halted state
    
Pull Down resistor connected to GPIO4,GND, and power supply 5v
   
    detects power outage and performs pi/shutdown/shutdown 


Create listen-for-shutdown.py file with     
    
    sudo listen-for-shutdow.py

Make script run on boot
   
    sudo mv listen-for-shutdown.py /usr/local/bin/

Make executable            
    
    sudo chmod +x /usr/local/bin/listen-for-shutdown.py

Script to Start/Stop   
 
    sudo listen-for-shutdown.sh

Make script run on boot   

    sudo mv listen-for-shutdown.sh /etc/init.d/

Make executable 

    sudo chmod +x /etc/init.d/listen-forshutdown.sh

    sudo update-rc.d listen-for-shutdown.sh defaults

Terminal command to run manually 

    sudo /etc/init.d/listen-for-shutdown.sh start
