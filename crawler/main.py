'''
Created on 12.11.2014

@author: constantin
'''
import logging

from attacker import Attacker
from crawler import Crawler
from database.databasemanager import DatabaseManager
from utils.config import CrawlConfig, AttackConfig
from models.utils import CrawlSpeed
from utils.user import User
import csv
from utils.utils import calculate_similarity_between_pages

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s - %(message)s',
                    #datefmt='%d.%m.%Y %H:%M:%S.%f',
                    #filename='Attack.log',
                    #filemode='w'
                    )

if __name__ == '__main__':


    # In the Userobject, the first string you set is the name of the crawl run and also the name of the created database.
    # So if you want to keep old runs then just give different names for each crawl


    # The first of the line below, starts a scan with a logged in user.
    # Parameter desc: Name of DB - Privilege level: deprecated(Just let it 0) - URL where the login form is stored - login data as dict. The key is the parameter name in the login form that has to be set -
    # session: reflects the session within a DB. It is deprecated. Just set it to ABC
    #user = User("WordpressX", 0, "http://localhost:8080/wp-login.php", login_data = {"log": "admin", "pwd": "admin"}, session="ABC")


    # Crawl without user session. Parameter desc: Name of DB - Privilege level - session
    user = User("RUN1", 0, session="ABC")

    url = "http://example.com"
    # Creates the crawler config: URL: start url of the crawler(independent from login) - max_dept: how deep to crawl(link), max_click_depth: how deep to follow events - Crawlspeed: Fast is the best value here
    crawler_config = CrawlConfig("Some Name, doesn't matter", url, max_depth=1, max_click_depth=2, crawl_speed=CrawlSpeed.Fast)

    # From here you have nothing to chance. Except you want no attacking, then comment out the lines down
    logging.info("Crawler started...")
    database_manager = DatabaseManager(user, dropping=True)
    crawler = Crawler(crawl_config=crawler_config, database_manager=database_manager)#, proxy="localhost", port=8082)
    crawler.crawl(user)
    logging.info("Crawler finished")

    # If you want no attacking comment out the lines below.
    logging.info("Start attacking...")
    attack_config = AttackConfig(url)
    attacker = Attacker(attack_config, database_manager=database_manager)#, proxy="localhost", port=8082)
    attacker.attack(user)
    logging.info("Finish attacking...")