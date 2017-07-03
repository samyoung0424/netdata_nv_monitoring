# netdata_nv_monitoring
# README #

## Overview ##
<!-- MarkdownTOC depth=0 -->

- [About](#about)
- [Requirements](#requirements)
- [Installation](#installation)
	- [General](#general)
	- [Installation Example](#installation-example)
- [Options](#options)
	- [Memory Clock Factor](#memory-clock-factor)
	- [Legacy Mode](#legacy-mode)
- [Charts](#charts)
- [Known Bugs/Issues](#known-bugsissues)
- [FAQ](#faq)
- [License](#license)


<!-- /MarkdownTOC -->

## About ##

[NetData](https://github.com/firehol/netdata/) plugin that polls Nvidia GPU data and specifically for Mapd Occupancy.

Original Plugin: [netdata_nv_plugin](https://github.com/coraxx/netdata_nv_plugin.git)

## Requirements ##

* Nvidia driver installed (this plugin uses the NVML library)
* nvidia-ml-py Python package (Python NVML wrapper)


## Installation ##

### General ###

Install the nvidia-ml-py Python package via `pip install nvidia-ml-py`.

**IMPORTANT**: Version 7.352.0 of the nvidia-ml-py package does not work with Python >=3.2 -> see known bugs section of this readme.

With default NetData installation copy the nv.chart.py script to `/usr/libexec/netdata/python.d/` and the nv.conf config file to `/etc/netdata/python.d/`.

Then restart NetData to activate the plugin.

To disable the nv plugin, edit `/etc/netdata/python.d.conf` and add `nv: no`.


### Installation Example ###

Example for standard NetData installation under Ubuntu, working with Python >=2.6 and >=3.2:

```
cd /tmp/

git clone https://github.com/samyoung0424/netdata_nv_monitoring.git

sudo cp netdata_nv_plugin/nv.chart.py /usr/libexec/netdata/python.d/

sudo cp netdata_nv_plugin/nv.conf /etc/netdata/python.d/
```


## Options ##

Options are set in the `nv.conf` file.
### Memory Clock Factor ###

Set `nvMemFactor: 2` in the `nv.conf` file if you want to display "the real clock speed". This is due to [DDR RAM](https://en.wikipedia.org/wiki/DDR_SDRAM#Double_data_rate_.28DDR.29_SDRAM_specification). Default is `1`.


### Legacy Mode ###

With older GPUs like my Nvidia GeForce 9600m gt, the load and clock frequencies cannot be read by the NVML lib. Only temperature and memory usage is displayed.

Set `legacy: True` in the `nv.conf` file to poll GPU and memory load/frequency via the nvidia-settings application (also installed with the Nvidia driver).

*Tested under Ubuntu 16.04*

**IMPORTANT:** This legacy mode only works with a running X session, so this will **not** work on headless clients. Also when the X session is not hosted by root, which is usually the case when running e.g. Ubuntu, you **must** allow `root` to connect to the X session. You can do that by executing this command in a terminal as the user of the X session (i.e. the user you are logged into your e.g. GNOME desktop environment):

`xhost +local:root`

Don't forget to restart NetData afterwards with e.g. `sudo service netdata restart`

For the sake of completeness: If you want to disable the root access to the X session again, execute:

`xhost -local:root`



## Charts ##

Depending on the Graphics card, these informations are extracted:

- GPU and memory load
- Mapd Occupancy
- Free and used memory
- ECC errors (only for cards equipped with ECC memory e.g. Quadro cards)
- Temperature
- Fan speed
- Clock frequency for GPU core, SM and memory

Readouts for units (S-class systems) are integrated but not tested yet. These add:

- intake, exhaust and board temperatures
- PSU current, voltage and power
- Fan rpm


## Known Bugs/Issues ##

Bugs:
* No known bugs at the moment


## FAQ ##

> Why does only one of my two whatever values show up in the whatever graph/chart?

Probably because the one not drawn in the graph is zero. For example with two graphics cards where only one is under load, chances are that NetData only draws the one with load > 0%. As soon as the other one also returns values > 0 it will be drawn as well.


## License ##

The MIT License (MIT)
Copyright (c) 2016 Jan Arnold

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


