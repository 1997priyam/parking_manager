
## Design of the system

 ### **Overview**
 
 - A parking lot was to be designed which should have the below mentioned features.
 - Park the vehicle at the spot nearest to entry and allot that spot to that car *(Vehicle Reg No and driver age given)*.
 - Get all slots of cars which were parked by the drivers with a certain age.
 - Get all registration numbers of cars which were parked by the drivers with a certain age.
 - Get the slot number of the car when its registration number is given.
 - Deallocate the slot when a car leaves the parking lot *(Slot number given)*.

### Note

 - I am using Python programming language to complete this assignment.
 - I haven't used any database as this was not mandatory to use.
 - I am maintaining the slots availability internally in a data strucutre.
 - I am not saving the history anywhere.
 - I have covered the relevant unit tests which are present in the `tests` directory.

### Design

 - I am using the `priority queue` data structure to get the available slots which are nearest to the entry.
 - Priority queue uses min heap internally because of which time complexity of insertion and removal is `O(log n)`. 
 - I am also maintaining 3 other data structures which are simple `hash maps` to ease the lookup time of my other queries. They are listed below: 
	 - `age_lookup` - To find the slot numbers and registration number when the age of driver is given.
	 - `regno_lookup`- To find the slot of the car when its registration number is given.
	 - `slot_lookup` - To find the registration number and age of the driver when a slot is vacated.

### Data structure format

    available_slots = PriorityQueue()

    age_lookup = {
	    "18": {
		    1: "KA-01-AA-1234",
		    2: "PB-02-UU-1234"
	    }
    }

    regno_lookup = {
	    "KA-01-AA-1234": 1,
	    "PB-02-UU-1234": 2
    }
    
    slots_lookup = {
		1: ["KA-01-AA-1234", "18"],
		2: ["PB-02-UU-1234", "18"]
    }
    

### Setup & Execution

 - Install Python
	 - [Macintosh](https://docs.python-guide.org/starting/install3/osx/)
	 - [Ubuntu](https://docs.python-guide.org/starting/install3/linux/)
	 - [Windows](https://docs.python.org/3/using/windows.html)
 - Install pytest by executing the following command `pip install pytest`.
 - Change your directory to the project directory.
 - Execute the following command to start the program `python3 main.py`.
 - Enter the file path of your command file and press enter.
 - The output will be printed on the terminal.
 - To run the tests, execute the following command:
	 - `pytest` To see the overview of the tests.
	 - `pytest -v` Turn on the verbose mode to view all tests in detail.

### Directory Strucutre

 - `/src` contains the source code.
	 - `/src/slots_manager.py` contains the logic to handle the allocation, deallocation and find queries from slots.
	 - `/src/utils.py` contains the utility/helper functions.
 - `/tests` contains all the unit tests files for the modules.
	 - `/tests/test_main.py` contains unit tests for the main module.
	 - `/tests/test_slots_manager.py` contains the unit tests for the slots_manager module.
	 - `/tests/utils/py` contains the unit tests for the utils module.

### Results
Below is the result when the provided sample file was run through this program.
![Program Output](https://pasteboard.co/K7m3rt6.png)

Below is the output when the unit tests are ran
![Unit Tests Output](https://pasteboard.co/K7m4a1X.png)
