import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/enesisaoglu/rmis_interface_ws/install/rmis_web_launcher'
