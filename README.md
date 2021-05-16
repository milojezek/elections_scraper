# Engeto Academy: Selections Scraper

## Project Description
This project can be used to extract the results of the [parliamnetary elections in 2017](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

### Libraries installations
The libraries used in this project are saved in the file `requirements.txt`. 

For installation, I recommend using a new virtual environment and installed manager(pip):

```
$ pip3 --version
$ pip3 install -r requirements.txt
```
### Project Launch
All necessary information is displayed after running the file `elections_scraper.py`
The program will ask you to insert a link to a district. Then you will have to type the name of the new csv. file where the result will be saved.
Please, keep in mind that the program will only work if [the page](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) is displayed in Czech.

### Sample
Election result for Domažlice district: 
```
Link to the selected region: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3201
Please, name your csv file where you can later find the result: domazlice_result
```
