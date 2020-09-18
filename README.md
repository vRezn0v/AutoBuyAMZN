# AutoBuyAMZN
A Script to Order a specified product from Amazon. Works in combination with Chrome and Windows Task Scheduler.
<br>
### Requirements:
- Selenium
- ConfigParser
- UrlLib3
- Chrome Webdriver

### Other Requirements
- Microsoft Windows
- Google Chrome

### Config.ini Format
>[MAIN]<br>
>DRIVER_LOCATION = ABSOLUTE PATH FOR THE CHROMEDRIVER<br>
><br>
>[CREDS]<br>
>USERNAME = ACCOUNT EMAIL<br>
>PASSWORD = AMAZON PASSWORD<br>
><br>
>[ORDER]<br>
>URL = https://amazon.in<br>
>CARD = LAST 4 DIGITS OF PREFERRED SAVED CARD<br>
>CVV = CVV<br>
>PRODUCT = PRODUCT NAME<br>
>ASIN = PRODUCT ASIN [IF AVAILABLE]<br>

### Installation:
1. Clone the Repository. ```git clone https://github.com/vrezn0v/AutoBuyAMZN```
2. `cd` into cloned repo. ```cd AutoBuyAMZN```
3. Install the dependencies. ```pip install -r requirements.txt```
4. Edit `config.ini` according to your requirements.
5. Run the Script or Schedule it with Task Scheduler.
