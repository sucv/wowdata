# Introduction
This tiny project is for the course Data Mining.

## Development Environment
- OS：Ubuntu 18.04
- Language：Python 3 with Anaconda 3
- Library：Scrapy，Pandas，Seaborn，Matplotlib, Jupyter Notebook

## Project Creation

```bash
# ~/  
conda create -n wow python==3.7 # Create a new virtual environment named wow
conda activate wow # Activate this what we created
conda install pandas seaborn scrapy jupyter notebook # Install all the needed libraries
mkdir ~/wow # Create a folder
cd ~/wow/ # Move to the folder

# ~/wow/ 
scrapy startproject wowdata # Create a new scrapy project
cd wowdata/ # Move to the project directory
```

Now the structure should be like below:

```markdown
wowdata/
    scrapy.cfg       
    wowdata/        
        __init__.py
        items.py         
        middlewares.py   
        pipelines.py      
        settings.py      
        spiders/          # Where the spider lives
            __init__.py
	    spider.py          # This is the crawler code. You will have to code it to crawl the data.
```


## Data Acquisition 

- Data Source: [wowhead](https://classic.wowhead.com/ "wowhead")
- Data Collection: [Python Scrapy](https://scrapy.org/ "Python Scrapy")

The crawler will generate two files

- all_weapon.json
- all_weapon_supp.json

at `~/wow/wowdata/wowdata`.

Unfortunately, the json files are partly in bad format, which cannot be directly process (either by Pandas or Python csv conversion). I choose to use this [online conversion](https://json-csv.com/ "online conversion") to do this dirty work. This site have daily limits on total download size! Our two csv files generated by this website are around 900 kb in total. I would attempt to shape the json by Python directly once I am strong enough.

Please put the two csv together with the json files. Your structure should be the same as in this github repo.


## Data Processing and Visualization
Before the Python part, we have to manually correct some minor problems in all_weapon_supp.csv.

The two pairs of weapons:

- Fahrad's Reloading Repeater
- Light Crossbow

and

- Stoneshatter
- Fine Light Crossbow

have to be swapped, so that each entries from the two csv files are well aligned. 

We also convert the csv files to xls files for safe keeping.

The file wowDataMining.ipynb will do the rest job.

Enjoy. 


