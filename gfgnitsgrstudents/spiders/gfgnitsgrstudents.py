# gfgnitsgrstudents.py
import scrapy
import json


class GfgnitsgrstudentsSpider(scrapy.Spider):
    name = "gfgnitsgrstudents"  # this command has to match with the block in this command --> scrapy crawl [(gfgnitsgrstudents)] -o output.csv\n

    allowed_domains = ["practiceapi.geeksforgeeks.org"]

    def start_requests(self):
        page_size = 10
        total_pages = 190

        for page in range(1, total_pages + 1):
            url = f"https://practiceapi.geeksforgeeks.org/api/v1/institute/114/students/stats?page_size={page_size}&page={page}"
            yield scrapy.Request(url, callback=self.parse, meta={"page": page})

    def parse(self, response):
        data = json.loads(response.text)

        for student in data.get("results", []):
            yield {
                "user_id": student.get("user_id"),
                "handle": student.get("handle"),
                "coding_score": student.get("coding_score"),
                "total_problems_solved": student.get("total_problems_solved"),
                "potd_longest_streak": student.get("potd_longest_streak"),
                "profile_url": f"https://auth.geeksforgeeks.org/user/{student['handle']}/"
            }
