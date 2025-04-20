# RMIS Web Interface

## Overview
A web-based GUI for the RMIS humanoid robot project, displaying messages from the `/my_topic` topic via `rosbridge_server`. The interface runs at `http://localhost:8000` and connects to `ws://localhost:9090`.

## Prerequisites
- ROS2 Humble (Ubuntu 22.04)
- `rosbridge_server` (`sudo apt install ros-humble-rosbridge-server`)
- `rmis_ws` repository (https://github.com/enesisaoglu/rmis_ws)

## Installation
1. Clone the repository:
   ```bash
   mkdir -p ~/rmis_interface_ws/src
   cd ~/rmis_interface_ws/src
   git clone https://github.com/enesisaoglu/rmis_interface_ws.git
2. Build the workspace:
   ```bash
   cd ~/rmis_interface_ws
   colcon build
   source install/setup.bash

## Usage
1. Start the web server:
   ```bash
   cd ~/rmis_interface_ws
   source install/setup.bash
   ros2 launch rmis_web_launcher web_launcher_launch.py
