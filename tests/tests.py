import warnings

warnings.filterwarnings("ignore")

import unittest
import grequests
import logging
import time
from detoxify import Detoxify

# Use log instead of print
logger = logging.getLogger()
logger.setLevel(logging.INFO)

CLASSES = [
    "toxicity",
    "severe_toxicity",
    "obscene",
    "threat",
    "insult",
    "identity_attack",
    "sexual_explicit",
]


class TestApi(unittest.TestCase):

    URL = "http://localhost:7979"

    #def test_website_is_up(self):
        #r = requests.get(TestApi.URL)
        #self.assertTrue(r.status_code == 200)

    async def test_response(self):
        response = await self._async_connection.get("http://localhost:7979")
        self.assertEqual(response.status_code, 200)
        logging.info("Response test")
        self.addAsyncCleanup(self.on_cleanup)

    def test_stress(self):
        n_requests = 100

        start_time = time.time()

        logging.info(f"Sending {n_requests} requests...") 

        urls = [TestApi.URL]*n_requests
        responses = grequests.map(grequests.head(u) for u in urls)

        end_time = time.time()
        full_time_request = end_time-start_time

        logging.info(f"Time for 100 requests : {full_time_request} ms")

        self.assertTrue(full_time_request < 60000)


    def test_original(self):
        model = Detoxify("original")
        results = model.predict(["shut up, you liar", "you look like Marilyn Monroe"])
        logging.info("Original test")
        assert len(results) == 6
        assert all(cl in results for cl in CLASSES[:6])
        assert results["toxicity"][0] >= 0.7
        assert results["toxicity"][1] < 0.5

            
if __name__ == '__main__':
    unittest.main()