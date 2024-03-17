<h1>Pomodoro Timer Application</h1>
![python_AZQoDXPCPJ](https://github.com/LuuuuQ/PomodoroTimer/assets/140170604/57805a2c-f112-4a96-8398-6ec7a42ea33f.gif)


<h2>Overview</h2>
<p>The Pomodoro Timer Application is a productivity tool designed to assist users in managing their work and break intervals efficiently, following the Pomodoro Technique. The application boasts a user-friendly graphical interface implemented in Python, leveraging the Tkinter library for creating an interactive and visually appealing user experience.</p>

<h3>Project Structure</h3>

<h4>main.py</h4>
<p>The main.py file serves as the entry point for the Pomodoro Timer Application. It encapsulates the application's main logic by importing the PomodoroTimerWindow class from the window module and initializing the primary application loop.</p>

<h4>window.py</h4>
<p>Within the window.py module, the PomodoroTimerWindow class is defined, representing the primary window of the application. This class integrates various graphical elements, such as input fields, buttons, and a progress bar, to provide users with an intuitive and functional interface. Notably, the window is constructed using the custom customtkinter library, enhancing visual aesthetics and user experience.</p>

<h4>countdown.py</h4>
<p>The countdown.py module plays a pivotal role in the Pomodoro Timer Application, implementing the Countdown class responsible for managing countdown functionality. This class facilitates updating the timer, handling pause functionality, and triggering a callback when the timer reaches zero, contributing significantly to the core functionality of the Pomodoro Timer.</p>

<h4>assets/sounds</h4>
<p>The assets/sounds directory contains essential sound files (click.mp3, break.mp3, reset.mp3, error.mp3) utilized for providing audio feedback during different events within the application. Incorporating sound elements enhances user experience by delivering clear indications of state changes.</p>

<h3>Design Choices</h3>

<h4>Custom Tkinter Library</h4>
<p>The decision to employ a custom Tkinter library (customtkinter.py) stems from a desire to elevate the visual aesthetics of the application while ensuring a consistent theme throughout. This custom library streamlines the creation and customization of Tkinter widgets, resulting in code that is both more readable and maintainable.</p>

<h4>Audio Feedback</h4>
<p>The inclusion of audio feedback for various events, such as initiating, pausing, and completing a timer, enhances the overall user experience. These auditory cues provide users with a tangible and immediate sense of timer state changes, contributing to the user-friendliness of the application.</p>

<h4>Progress Bar</h4>
<p>The vertical progress bar serves as a visual representation of elapsed time during work or break intervals. This addition provides users with a quick and informative overview of their progress, promoting focused and effective work sessions.</p>

<h4>Modular Code Structure</h4>
<p>To enhance maintainability and readability, the code is organized into distinct modules (window.py, countdown.py), each assigned a specific responsibility. This modular structure facilitates easier extension or modification of the application's functionality, supporting a more scalable and adaptable codebase.</p>

<h3>How to Run</h3>
<h4>Requirements</h4>

<p>The posted requirements file lists the libraries needed:</p>
<p>customtkinter==5.2.2</p>
<p>pygame==2.5.2</p>

<p>Executing the Pomodoro Timer Application is straightforward—simply run the main.py file. Ensure that Python is installed on your system, and install the necessary dependencies (including pygame) by running pip install -r requirements.txt. This ensures a smooth and hassle-free execution of the application.</p>

