Sorting Algorithm Visualizer

A desktop-based Python application that visually demonstrates classic sorting algorithms using animated bar graphs and real-time feedback. Built with pygame, it helps users understand how different sorting algorithms work step-by-step — now with added sound effects for each swap!
Features

    Real-time visual animation of sorting steps

    Choose ascending or descending order

    Supports multiple algorithms:

        Bubble Sort

        Insertion Sort

        Merge Sort

        Quick Sort

    Interactive buttons for Start, Reset, Sort Selection

    Sound feedback on each element swap

Tech Stack

    Language: Python 3

    Library: Pygame (for graphics and sound)

    Design: Object-Oriented Programming (OOP)

Upcoming Features

    Adjustable animation speed

    Sorting statistics (comparisons/swaps count)

    Dark mode toggle

    More algorithms (Heap, Selection, Radix, etc.)

    UI sliders for element count and delay

How to Run

    Clone the repo:
    git clone https://github.com/Kanishq-Potdar/Sorting-Visualizer.git
    cd Sorting-Visualizer

    Install required packages:
    pip install pygame

    Run the visualizer:
    python main.py

    Ensure a valid swap.wav file is present in the same directory for sound effects to work.

Project Structure

Sorting-Visualizer/
├── main.py # App entry point and control logic  
├── algorithms.py # Sorting algorithm implementations  
├── draw.py # GUI rendering and button logic  
├── swap.wav # Sound file for swap events  
└── README.md

Contributing

Pull requests are welcome! For new algorithms or features, please open an issue to discuss before submitting a PR.
