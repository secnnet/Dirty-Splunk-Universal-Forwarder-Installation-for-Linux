#!/usr/bin/env python

import os

# Define variables
SPLUNK_PACKAGE_URL = "https://splunk.com/forwarder.tgz"
INSTALL_LOCATION = "/opt/splunkforwarder"

# Download Splunk package
os.system("wget {} -O /tmp/forwarder.tgz".format(SPLUNK_PACKAGE_URL))

# Extract package
os.system("tar zxvf /tmp/forwarder.tgz -C {}".format(INSTALL_LOCATION))

# Start Splunk Universal Forwarder
os.system("{}/bin/splunk start --accept-license --answer-yes".format(INSTALL_LOCATION))
