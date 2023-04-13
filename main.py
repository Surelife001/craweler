import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = "nairaland"
HOMEPAGE = "https://www.nairaland.com/"
DOMAIN_NAME = get_domain_name(HOMEPAGE)
Queue_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# create worker threads (will die when main exit)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

# Each queued link is a new job
def create_jobs():
    for link in file_to_set(Queue_FILE):
        queue.put(link)
    queue.join()
    crawl()

# check if there are items in the queue, is so crawl them
def crawl():
    queued_links = file_to_set(Queue_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + "links in the queue")
        create_jobs()


create_workers()
crawl()