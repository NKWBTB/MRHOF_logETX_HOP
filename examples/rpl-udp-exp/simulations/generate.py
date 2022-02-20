import numpy as np
import re

if __name__ == '__main__':
    sim_xml = ""
    with open("template.csc", "r", encoding="utf-8") as f:
        sim_xml = f.read()

    pattern = r'(<success_ratio_rx>).*(</success_ratio_rx>)'
    p = re.compile(pattern)
    p.match(sim_xml)

    # Change RX Ratio from 30 to 100
    for rx in np.arange(0.3, 1.01, 0.1):
        sim_xml_out = re.sub(pattern, r'\g<1>{:.1f}\g<2>'.format(rx), sim_xml)
        outfile = "rpl-udp-cooja-automate-"+str(int(rx*100))+".csc"
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(sim_xml_out)