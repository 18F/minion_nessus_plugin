Minion Nessus Plugin
==================

This is a plugin for [Minion](https://github.com/mozilla/minion) that executes Nessus scans via the REST API.

Installation
------------

You can install the plugin by running the following command in the minion-nessus-plugin repository:

```python setup.py install```

If running minion inside of vitualenv, make sure to activate it first.

The plugin expects `NESSUS_USER` and `NESSUS_PASS` to be defined environment variables containing the credentials to use the Nessus REST API.

Example of plan
---------------
```
{
  "configuration": {
    "server_url": "https://nessusserver:8834",
    "verify": false,
    "policy": "Basic Scan",
    "target": "10.0.10.138",
    "scan_name": "Test Scanner",
    "scan_description": "Test Scan Description"
  },
  "description": "Run the Nessus scanner.",
  "plugin_name": "minion.plugins.nessus.NessusPlugin"
}
```
Available configuration options
-------------------------------
Most of the options are mandatory and do not have default values. (It'll get better, though)

* `configuration`
  * `server_url`: the server running Nessus.
  * `verify`: should the requests to Nessus verify the SSL cert of the Nessus server?
  * `policy`: the name of the Nessus policy to run.
  * `target`: the machine (or machines) to scan.
  * `scan_name`: the name of the scan.
  * `scan_description`: the description of the scan.

THANKS
------
Structurally, this plugin is based heavily on the [Minion-Nmap](https://github.com/mozilla/minion-nmap-plugin) plugin. 

Much of the Nessus REST API code is based on sample code posted [here](https://discussions.tenable.com/docs/DOC-1155#start=100)

TODO
----

* Tests
* More configuration options, and reasonable defaults
* Correct configuration issue with Celery (/minion-env/bin/minion-plugin-worker)
