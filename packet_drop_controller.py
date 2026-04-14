from pox.core import core
import pox.openflow.libopenflow_01 as of
import random

log = core.getLogger()
DROP_PROBABILITY = 0.3

def _handle_PacketIn(event):
    packet = event.parsed

    if not packet.parsed:
        return

    # Random drop
    if random.random() < DROP_PROBABILITY:
        log.info("Dropping packet")
        return

    # INSTALL FLOW RULE (THIS IS THE FIX)
    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet)
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

    log.info("Flow installed")


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Packet Drop Controller Running...")
