import logging
import logging.handlers

import feedparser

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


if __name__ == "__main__":
    feed = 'https://bas.codes/rss.xml'
    feed_parser = feedparser.parse(feed)
    entries = feed_parser.entries[:3]
    
    with open("README.md", "w") as f:
        f.write("# Latest Blog Posts\n")
        for entry in entries:
            logger.info(f"processing entry {entry.title}")
            f.write(f"- [{entry.title}]({entry.link})\n")
    