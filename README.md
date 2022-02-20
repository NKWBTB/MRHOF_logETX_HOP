# MRHOF_logETX_HOP (CPR E 548X Project)
A hybrid OF for RPL 

## Reproduction Instructions

1. Setup [contiki-ng](https://github.com/contiki-ng/contiki-ng), this project is tested on [docker image](https://hub.docker.com/layers/contiker/contiki-ng/66cbc3434/images/sha256-deae47d07406e49a066da8f183722ace94762578a9e50b52387c801f77c881db?context=explore)

2. Replace the following file in the original contiki-ng repo with our modification
 - `os/net/routing/rpl-lite/rpl-conf.h`
 - `os/net/routing/rpl-lite/rpl-mrhof.c`

3. Copy the modified testbed to the contiki-ng repo's `examples` folder 

- `examples/rpl-udp-exp`

4. Follow simulation instructions in `examples/rpl-udp-exp/README.md`
