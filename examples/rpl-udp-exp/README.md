# Simulation instructions

## Files

- `simulations/template.csc`: cooja simulation file
- `simulations/generate.py`: generate simualtion files with different RX ratio based on `template.csc`
- `config.h`: some defined constants for the UDP communication
- `project-conf.h`: RPL settings
- `udp-client.c`: UDP client code
- `udp-server.c`: UDP server code
- `run_sim.py`: script for running the simulation and parse log files for PDR and latency

## 1. Simulation settings

This example is modified from offical [example](https://github.com/contiki-ng/contiki-ng/tree/develop/examples/rpl-udp).

A simple RPL network with UDP communication. This is a self-contained example:
it includes a DAG root (`udp-server.c`) and DAG nodes (`udp-clients.c`).
This example runs without a border router -- this is a stand-alone RPL network.

The DAG root also acts as UDP server. The DAG nodes are UDP client. The clients
send a UDP request periodically, that simply includes a counter as payload.

## 2. RPL setting in `project-conf.h`

1. to use **OF0**, uncomment the follwing directive
```c
#define RPL_CONF_OF_OCP             RPL_OCP_OF0
```
2. to use **MRHOF-ETX** , comment the **OF0** and **logETX** directive
```c
// #define RPL_CONF_OF_OCP             RPL_OCP_OF0
// #define RPL_MRHOF_LOGARITHM_ETX     1
```
3. Based on 2, to use **MRHOF-ETX^2**, uncomment the follwing directive
```c
#define RPL_MRHOF_CONF_SQUARED_ETX  1
```
4. Based on 2, to use **MRHOF-HOP**, set the following directive
```c
#define RPL_MRHOF_LOGARITHM_ETX     1
#define RPL_MRHOF_HOP_WEIGHT        1
#define RPL_MRHOF_LOGETX_WEIGHT     0
```
5. Based on 2, to use **MRHOF-logETX**, set the following directive
```c
#define RPL_MRHOF_LOGARITHM_ETX     1
#define RPL_MRHOF_HOP_WEIGHT        0
#define RPL_MRHOF_LOGETX_WEIGHT     1
```
6. Based on 2, to use **MRHOF-logETX+HOP**, set the following directive
```c
#define RPL_MRHOF_LOGARITHM_ETX     1
#define RPL_MRHOF_HOP_WEIGHT        1
#define RPL_MRHOF_LOGETX_WEIGHT     1
```
## 2. Run simulation
1. Build [cooja](https://github.com/contiki-ng/contiki-ng/wiki/Tutorial:-Running-Contiki%E2%80%90NG-in-Cooja)
2. Change ``project-conf.h`` for desired RPL settings
3. Change path settings in `run_sim.py` for launching cooja simulator
4. Run ``python3 run_sim.py`` to run simulations