**School of Computing — Year 4 Project Proposal Form**

Project Title: Thieft

Student 1 Name: Jack O'Reilly

Student 1 ID: 18465312

Student 2 Name: Niall Bermingham

Student 2 ID: 18392656

Project Supervisor: Michael Scriney

**Introduction**

The project we are proposing is: A Bluetooth Enabled Anti-Theft device for vehicles, that also hosts a graphical user interface for the On-Board Diagnostics(OBD) of the vehicle. 


**Outline**

We intend to build a small device that incorporates a Raspberry Pi, Accelerometer and GPS. The Raspberry Pi single-board computer has built-in bluetooth connectivity, we will use this to detect if the owner of the vehicle's phone is in range of the device. The accelerometer allows us to tell if the vehicle is moving or not. If the vehicle is moving, and the owner's phone is not in range of the device, an SMS alert will be sent to the owner, that will also provide the location of the vehicle (made possible using the GPS). The device will also host a graphical user interface that displays the vehicle's On-Board Diagnostics(OBD).

**Background**

Between 2015 and 2017, roughly 700,000 motor vehicles were stolen across the EU. Whilst varius improvements in vehicle technology have certainly made life easier for drivers, criminals have been able to come up with new ways of gaining access to vehicles. To give an example, many relatively new cars have keys that send a short-range signal that tells it to unlock, even if they are in your pocket. Car thieves exploit this technology using electronic car key relay boxes, putting one as close to your home as they can to receive signals coming from your car key fob, then boosting the signal to the second device near your car, tricking the car into thinking the key is nearby, which then unlocks the doors.

While there are several preventative measures available to take against vehicle theft (key fob blockers, steering locks, loud alarm etc.), we believe that being alerted to a possible theft incident via text message is certainly a cost-effective solution to this important problem. As there are many other vehicle related capabilities using a Raspberry Pi, we thought we could make our device even more useful by allowing users to access the On-Board Diagnostics(OBD) of their vehicle, through an intuitive graphical interface.

**Achievements**

Users will be able to:

* Receive detailed SMS alerts to possible vehicle theft
* Alert emergency services with this information
* Locate vehicle position
* View On-Board Diagnostics of their vehicle
* Gain insight into possible vehicle issues
* Make decisions based on this information

**Justification**

As previously mentioned, this proposed project is in our opinion, very useful as:

* A preventative measure against vehicle theft, that alerts you to the possibility of a theft attempt, and simplifies the process of notifying the authorities with detailed information (time, place, location) of the incident.
* An easy to interact with interface, that not only tells the user about each of the OBD, but educates them. (through detailed descriptions, expected results/output levels etc.)

**Programming Language(s)**

* Python
* Javascript
* HTML/CSS
* C++

**Programming Tools / Tech Stack**

* Node.js
* React.js
* PyUnit

**Hardware**

* Raspberry Pi
* Accelerometer
* GSM/GPRS Module
* GPS Module
* OBD Reader

**Learning Challenges**

* Laying out a well strucutured plan for the project - as we are extremely busy this year, it is vitally important that a plan is put in place early, and that we stick to it. Although with assignments and other responsibilities, we will have to adapt and learn to prioritize work. This can be achieved through consistent communication, and keeping eachother honest.

* Testing - as there are many consequences to our device not functioning as intended, a significant amount of testing will have to be carried out. This will take a lot of time, and will have to be planned for well in advance.

* Quality Assurance - making sure we undertake the correct development procedures, and adhere to code quality standards throughout the course of the project.

* Security - as our device will be one dealing with theift some security will be implimented to protect the device from unwanted access.


**Breakdown Of Work**

We will certainly be flexible in our approach, as I'm sure we will work together and help eachother with much of what we propose to do, but we have planned to focus on the following sections individually:

Jack:
* User Interface Design
* Javascript
* Backend Management

Niall:
* Hardware Functionality (Accelerometer, GPS)
* Bluetooth Connectivity
* Raspberry Pi Configuration
* Security