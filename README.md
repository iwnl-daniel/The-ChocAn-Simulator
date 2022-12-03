# The-ChocAn-Simulator
>314 Group Project

## Group Members
- Alex Teav
- Andy Iliesi
- Daniel Gregorio-Torres
- Jordan Nguyen
- Joseph Wornath
- Liam McCracken

## Purpose of this project
The purpose of this application is to help the Chocoholics Anonymous organization by making it easy to help and manage their patients. A specially designed ChocAn computer terminal is placed in the location of each healthcare provider who provides services to ChocAn members. From the terminal, the application displays the member status and allows the provider to bill ChocAn after a healthcare service has been provided to the member. At the end of the week, the application will send out a report to each provider containing the list of services they provided to ChocAn members. An email is sent to each ChocAn member who received consulting from a ChocAn provider containing a list of services provided during the week. A record consisting of electronic funds is then written to the disk allowing the banking computer to ensure the provider's bank account is credited with the correct amount. At the ChocAn Data Center, operators are allowed to add or delete members or providers to ChocAn. They are also allowed to update member and provider records.


## Running the code
###### Unix/ macOS:
```
python3 -m venv env
source env/bin/activate
pip install --upgrade -r requirements.txt
python3 main.py
```

###### Windows:
```
py -m venv env
.\env\Scripts\activate
pip install --upgrade -r requirements.txt
python3 main.py
```
