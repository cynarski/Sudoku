# Sudoku project in Python for Windows and Android
This is our first project of python

TODO:
* Start panel
* Game algorithms
* Win and Loss panel
* Android version

## Libraries which we used:
* kivy - 2.1.0
* numpy - 1.24.2
* dokusan - 0.1.0a6

## How to install libraries
Open command prompt in project folder and write

`python -m pip install --upgrade pip`

next 

`pip install kivy`

Of course you should do this with last two libraries 

## How to create app for android

We use buildozer wchih is kivy tool to create applicatiof for android
In command prompt we should write

`pip install buildozer`

next

`buildozer init`

This line create file buildozer.spec. In this file we can change name, choose orientation and other basic specifications wchih we want to have in our application.

Next we are ready to create app. We should write this line in cmd:

`buildozer -v android debug`

This opperation is very time consuming because lasts over one hour. When the app is ready we can installi it in our mobile phones and play.
