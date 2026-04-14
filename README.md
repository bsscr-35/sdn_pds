# SDN Packet Drop Simulation (POX)

## Description
Simulates packet loss using SDN controller.

## Setup
Run:
python3.8 pox.py openflow.of_01 --port=6634 misc.packet_drop_controller

Then:
sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6634

## Results
- Packet loss observed
- Flow rules installed
- Controller logs show dropped packets

## Screenshots
(Add images)
