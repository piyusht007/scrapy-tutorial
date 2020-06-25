# scrapy-tutorial
A sample python project to showcase web scraping using https://scrapy.org/

This project crawls a simple page on ```https://worldpostalcode.com``` and extracts place name and its respective postal code.

The actual page which is being crawled is, https://worldpostalcode.com/india/madhya-pradesh/jabalpur/

### Running the Spider

The project has a spider named as 'postal_codes' which can be executed using following commands:

```
scrapy crawl postal_codes
```

To store the crawled output to a **JSON/CSV/XML** file ```-o``` option can be used.

```
scrapy crawl postal_codes -o json
scrapy crawl postal_codes -o csv
scrapy crawl postal_codes -o xml
``` 

### Note

Install ```scrapy``` module on your machine and have a virtual environment to be able to run this code. Follow instructions from https://scrapy.org/

### Extras

Use scrapy shell to quickly crawl something and extract data in real-time. Following command can be used to run scrapy shell.

```
scrapy shell "https://worldpostalcode.com/india/madhya-pradesh/jabalpur/"
```  

