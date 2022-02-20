import re
import os

def parselog():
    LOG_FILE = "COOJA.testlog"

    pattern = r"([0-9]+):([0-9]+):\[(INFO|WARN|ERR|DBG): *([A-Za-z]+) *\] *(.*)"
    p = re.compile(pattern)
    send_pattern = r"Sending request ([0-9]+) to (.*)"
    sp = re.compile(send_pattern)
    rec_pattern = r"Received request 'hello ([0-9]+)' from (.*)"
    rp = re.compile(rec_pattern)
    ip_pattern = r"Tentative link-local IPv6 address: (.*)"
    ip = re.compile(ip_pattern)

    ip2node = {}
    # node2ip = {}

    packets = {}

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            m = p.match(line)
            if not m: continue

            TIMESTAMP = m.group(1)
            NODE_ID = m.group(2)
            LEVEL = m.group(3)
            MODULE = m.group(4)
            MESSAGE = m.group(5)

            if MODULE == 'Main':
                if "Tentative link-local IPv6 address" in MESSAGE:
                    m = ip.match(MESSAGE)
                    ipv6 = m.group(1).strip()
                    # Remove prefix
                    ipv6 = ipv6[ipv6.find("::"):]
                    ip2node[ipv6] = NODE_ID
                    # node2ip[NODE_ID] = ipv6

            elif MODULE == 'App':
                if 'Sending request' in MESSAGE:
                    m = sp.match(MESSAGE)
                    REQUEST_ID = m.group(1)
                    # ipv6 = m.group(2).strip()
                    packets[(NODE_ID, REQUEST_ID)] = { "st": float(TIMESTAMP) / 1e3 }  
                elif 'Received request' in MESSAGE:
                    m = rp.match(MESSAGE)
                    REQUEST_ID = m.group(1)
                    ipv6 = m.group(2).strip()
                    # Remove prefix
                    ipv6 = ipv6[ipv6.find("::"):]
                    node_id = ip2node[ipv6]
                    packets[(node_id, REQUEST_ID)]["ed"] = float(TIMESTAMP) / 1e3

    delay = 0
    received_packets = 0
    for packet in packets.values():
        if "ed" in packet:
            delay += packet["ed"] - packet["st"]
            received_packets += 1

    num_packets = len(packets)
    
    Average_PDR = received_packets / num_packets * 100
    Average_lag = delay / received_packets

    return Average_PDR, Average_lag

if __name__ == "__main__":
    sims = os.listdir("simulations")

    results = {}
    for run in sims:
        if run.startswith("rpl") and run.endswith("csc"):
            print(run)
            cmd = "CONTIKI=$HOME/contiki-ng && sudo -E java -Xshare:on -jar $CONTIKI/tools/cooja/dist/cooja.jar -nogui=$CONTIKI/examples/rpl-udp-exp/" + \
                "simulations/{} -contiki=$CONTIKI".format(run)
            os.system(cmd)
            results[run] = parselog()
            print(results[run])
    
    print(results)
            