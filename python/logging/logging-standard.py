import os
import logging

# Get the directory of the current module
module_dir = os.path.dirname(os.path.abspath(__file__))
# Construct a path to the log file in the log directory
log_file = os.path.join(module_dir, "log", "logging-standard.log")
