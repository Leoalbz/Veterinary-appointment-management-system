Requirements
Python 3.12 or higher

pip (Python package manager)

MySQL

Tkinter

MySQL Connector

Dependencies
Clone the repository or download the code.

Create and activate a virtual environment (optional).

To install dependencies, run:

pip install -r requirements.txt
Create the Executable
To create the executable file, follow these steps:

Ensure all dependencies are installed correctly.

Open the terminal or command line in the project directory.

Run the following command:

python -m PyInstaller --onefile --windowed --hidden-import=mysql.connector --add-data "background_img.png;." app.py
--onefile: Create a single executable file.

--windowed: Prevents a terminal window from opening (useful for graphical applications).

--add-data: Includes additional files such as images or databases.

--hidden-import: Ensures that dependencies like mysql.connector are included correctly.

The executable will be created in the dist folder inside the project directory.

Running the Executable
Once the file is created, you can find it inside the dist folder. Simply double-click to open it.

Notes
If you're encountering issues with dependencies or creating the executable, make sure all libraries are correctly installed in your environment.

The requirements.txt file contains all the dependencies needed for this project.
