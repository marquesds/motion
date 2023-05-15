import json
import re
from datetime import datetime

from motion import logger, mongo


class Connection:
    def get_db(self):
        return mongo.db

    def load_database(self):
        db_posts = self.get_db()
        db_passengers = self.get_db()
        db_lines = self.get_db()
        db_following = self.get_db()

        posts = db_posts.posts
        passengers = db_passengers.passengers
        lines = db_lines.lines
        following = db_following.following

        with open("motion/infra/db/mongodb/db.json") as db:
            data = json.load(db)

        if posts.count_documents({}) == 0:
            logger.info("Inserting posts...")
            posts.insert_many(data["posts"])
        else:
            logger.info("Database already loaded. Deleting posts...")
            posts.delete_many({})
            logger.info("Inserting posts...")
            posts.insert_many(data["posts"])

        if passengers.count_documents({}) == 0:
            logger.info("Inserting passengers...")
            passengers.insert_many(data["passengers"])
        else:
            logger.info("Database already loaded. Deleting passengers...")
            passengers.delete_many({})
            logger.info("Inserting passengers...")
            passengers.insert_many(data["passengers"])

        if lines.count_documents({}) == 0:
            logger.info("Inserting lines...")
            lines.insert_many(data["lines"])
        else:
            logger.info("Database already loaded. Deleting lines...")
            lines.delete_many({})
            logger.info("Inserting lines...")
            lines.insert_many(data["lines"])

        if following.count_documents({}) == 0:
            logger.info("Inserting following...")
            following.insert_many(data["following"])
        else:
            logger.info("Database already loaded. Deleting following...")
            following.delete_many({})
            logger.info("Inserting following...")
            following.insert_many(data["following"])


class MongoBusLineRepository:
    def __init__(self, connection):
        self.db_lines = connection.get_db()
        self.db_following = connection.get_db()

    def list(self, passenger, line=None):
        if not line:
            lines = list(self.db_lines.lines.find({}))
        else:
            regex = re.compile(f"{line}", re.IGNORECASE)
            lines = list(self.db_lines.lines.find({"number": {"$regex": regex}}))
            if not lines:
                lines = list(self.db_lines.lines.find({"description": {"$regex": regex}}))

        passenger = self.db_following.following.find_one({"passenger": passenger.email})

        for line in lines:
            if line["number"] in passenger.get("lines", []):
                line["following"] = True
            else:
                line["following"] = False

        return lines


class MongoSubscriptionRepository:
    def __init__(self, connection):
        self.db = connection.get_db()

    def follow(self, passenger, bus):
        ...

    def unfollow(self, passenger, bus):
        ...


class MongoPostRepository:
    def __init__(self, connection):
        self.db_posts = connection.get_db()
        self.db_passengers = connection.get_db()
        self.db_lines = connection.get_db()
        self.db_following = connection.get_db()

    def list(self, passenger):
        line_ids = self.db_following.following.find_one({"passenger": passenger.email})["lines"]

        posts = list(self.db_posts.posts.find({"line": {"$in": line_ids}}))

        for post in posts:
            line = self.db_lines.lines.find_one({"number": post["line"]})
            passenger = self.db_passengers.passengers.find_one({"email": post["passenger"]})

            post["line"] = line
            post["passenger"] = passenger

        posts.sort(
            key=lambda post: datetime.strptime(post["created_at"], "%Y-%m-%d %H:%M:%S"),
            reverse=True,
        )
        return posts
