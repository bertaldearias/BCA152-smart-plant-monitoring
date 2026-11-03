
<div align="center">

# ESP32 BLE Mesh Smart Home System

**Arias | Dagondon | Estores**

</div>

---

## Navigation

1. [Project Overview](#1-project-overview)
2. [Features](#2-features)
3. [Learning Objectives](#3-learning-objectives)
4. [System Architecture](#4-system-architecture)
5. [Hardware Components](#5-hardware-components)
6. Pin Configuration — *Coming Soon*
7. BLE Mesh Architecture — *Coming Soon*
8. Gateway, Sensor, and Relay Modules — *Coming Soon*
9. Provisioning and Configuration — *Coming Soon*
10. Wi-Fi and Web Interface — *Coming Soon*
11. Repository Structure — *Coming Soon*
12. Getting Started — *Coming Soon*
13. Building and Uploading — *Coming Soon*
14. Testing and Verification — *Coming Soon*
15. Engineering Decisions — *Coming Soon*
16. Challenges Encountered — *Coming Soon*
17. Limitations — *Coming Soon*
18. Future Improvements — *Coming Soon*
19. References and Acknowledgments — *Coming Soon*

---

## 1. Project Overview

The **ESP32 BLE Mesh Smart Home System** is a distributed embedded system designed to demonstrate wireless communication, environmental monitoring, and device control using Bluetooth Low Energy (BLE) Mesh networking.

The project integrates three ESP32-based modules: a **Gateway**, a **Sensor Node**, and a **Relay/Switch Node**. Each module performs a specific function while participating in a common BLE Mesh network.

The gateway connects to a Wi-Fi network and provides a web-based interface for manual device control. The sensor node is intended to collect environmental information, while the relay/switch node is responsible for executing switching commands received through the BLE Mesh network.

The system is developed using the **Espressif IoT Development Framework (ESP-IDF)** and **PlatformIO**, following a modular approach to firmware development.

### Project Objectives

- Develop a distributed smart home system using ESP32 microcontrollers.
- Establish communication between multiple devices through BLE Mesh networking.
- Implement a Wi-Fi-enabled gateway with a web-based control interface.
- Integrate sensor monitoring and relay switching functionalities.
- Demonstrate BLE Mesh provisioning, model configuration, and message communication.

---

## 2. Features

The system is designed to support the following functionalities.

| Feature | Description | Development Status |
|---|---|---|
| BLE Mesh Networking | Establishes a wireless network between ESP32 devices. | In Progress |
| Gateway Provisioning | Registers the gateway as a BLE Mesh node. | Completed |
| Wi-Fi Connectivity | Connects the gateway to a local wireless network. | Completed |
| Web-Based Interface | Provides manual ON/OFF controls through a browser. | Completed |
| Sensor Monitoring | Collects environmental sensor information. | Pending Verification |
| Relay/Switch Control | Controls a connected switching device through BLE Mesh commands. | Pending Verification |
| Application Key Configuration | Supports secure application-level communication between mesh models. | In Progress |
| Modular Firmware | Separates functionality into reusable source modules. | Implemented |

### Gateway Functionality

The gateway currently supports:

- Wi-Fi initialization and connection.
- BLE Mesh initialization and provisioning.
- Application key registration.
- HTTP web server operation.
- Manual ON/OFF request handling.

The gateway web interface is operational. However, complete BLE Mesh switching functionality requires additional configuration and verification of the relay/switch node.

---

## 3. Learning Objectives

The development of the ESP32 BLE Mesh Smart Home System aims to demonstrate practical knowledge and technical skills in embedded systems and wireless communication.

Upon completion of the project, the developers should be able to:

1. Configure ESP32 development environments using PlatformIO and ESP-IDF.
2. Implement Bluetooth Low Energy Mesh networking using ESP32 microcontrollers.
3. Understand the BLE Mesh provisioning and configuration processes.
4. Configure application keys and BLE Mesh model bindings.
5. Implement communication between BLE Mesh client and server models.
6. Integrate Wi-Fi connectivity with an embedded HTTP web server.
7. Develop a web-based interface for controlling embedded devices.
8. Organize firmware into modular and reusable components.
9. Perform functional verification using serial monitoring and hardware testing.
10. Document engineering decisions, implementation results, and system limitations.

---

## 4. System Architecture

The ESP32 BLE Mesh Smart Home System follows a distributed architecture consisting of three primary modules.

The gateway serves as the interface between the local Wi-Fi network and the BLE Mesh network. The sensor node is intended to provide environmental measurements, while the relay/switch node receives control commands.

### System Architecture Diagram

```text
                    +----------------------+
                    |     User / Client    |
                    |     Web Browser      |
                    +----------+-----------+
                               |
                               | HTTP / Wi-Fi
                               |
                    +----------v-----------+
                    |    ESP32 Gateway     |
                    |----------------------|
                    | Wi-Fi Connectivity   |
                    | HTTP Web Server      |
                    | BLE Mesh Client      |
                    +----------+-----------+
                               |
                               | BLE Mesh
                               |
                  +------------+------------+
                  |                         |
        +---------v----------+    +---------v----------+
        |   ESP32-S3 Sensor  |    |  ESP32-S3 Relay    |
        |--------------------|    |--------------------|
        | Sensor Acquisition |    | Switching Control  |
        | BLE Mesh Node      |    | BLE Mesh Server    |
        +--------------------+    +--------------------+
```

### Architectural Components

**Gateway Module**

The gateway uses an ESP32 development board to establish Wi-Fi connectivity and initialize a BLE Mesh client. It hosts an HTTP web server that receives manual ON/OFF requests from a browser.

**Sensor Module**

The sensor module uses an ESP32-S3 microcontroller and is intended to collect environmental data. Its integration and communication functionality will be verified during subsequent development.

**Relay/Switch Module**

The relay/switch module uses an ESP32-S3 microcontroller to receive switching commands through BLE Mesh. It is intended to execute ON/OFF operations according to commands transmitted by the gateway.

### Communication Flow

1. The user accesses the gateway web interface through a browser.
2. The user selects an ON or OFF command.
3. The HTTP web server receives and processes the request.
4. The gateway prepares the corresponding BLE Mesh Generic OnOff command.
5. Once the client publication and relay node are configured, the command can be transmitted to the relay/switch node.
6. The relay/switch node processes the received command and updates its switching state.

The final communication sequence will be verified during end-to-end integration testing.

---

## 5. Hardware Components

The system uses ESP32-based microcontrollers assigned to specific functions within the BLE Mesh network.

### Primary Components

| Component | Quantity | Purpose |
|---|---|---|
| ESP32 DevKit V1 | 1 | Gateway, Wi-Fi connectivity, and web server |
| ESP32-S3 Development Board | 1 | Sensor node |
| ESP32-S3 Development Board | 1 | Relay/switch node |
| Sensor Module | As required | Environmental data acquisition |
| Relay/Switch Hardware | As required | Switching operations |
| USB Data Cables | 3 | Programming and power during development |
| Wi-Fi Network | 1 | Gateway network connectivity |
| Smartphone | 1 | BLE Mesh provisioning and configuration |

### Gateway Hardware

**Microcontroller:** ESP32 DevKit V1

The gateway is responsible for:

- Establishing a connection to a local Wi-Fi network.
- Initializing the BLE Mesh networking stack.
- Hosting the HTTP web interface.
- Sending control commands through the Generic OnOff Client model.

### Sensor Node Hardware

**Microcontroller:** ESP32-S3

The sensor node is intended to collect environmental measurements and participate in the BLE Mesh network.

The final sensor configuration and pin assignments will be documented after hardware integration.

### Relay/Switch Node Hardware

**Microcontroller:** ESP32-S3

The relay/switch node is intended to receive BLE Mesh Generic OnOff commands and control the assigned switching output.

The final relay connections and pin assignments will be documented after hardware integration.

### Development Tools

| Tool | Purpose |
|---|---|
| Visual Studio Code | Source code development |
| PlatformIO | Project management, compilation, and firmware uploading |
| ESP-IDF | Embedded software framework |
| nRF Mesh | BLE Mesh provisioning and configuration |
| Git | Version control |
| GitHub | Source code repository and documentation |
| Serial Monitor | Debugging and verification |

---

