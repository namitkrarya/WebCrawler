This python script takes input as the website address and crawls all the links in it with which have the domain name of the website.
You will also be asked how many agents you want to deploy on the website. More the agents, higher will be the speed of crawling. The value may range from 1 to 20 dependent on how many you system(hardware) could take. I would recommend it to be 8 for smooth and fast crawling.

To run the script, just open the terminal in the folder with all the files and run the following command :
```
sudo python3 main.py
```

The script prints the number of elements in the queue( of links TO BE crawled ), number of elements in the crawled file( of links that are already crawled ) and the link name while crawling them.
Enjoy Crawling!