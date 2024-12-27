import json
import logging
from typing import List, Optional, Dict
import requests
logging.basicConfig(level=logging.INFO)

class Flower:
    """A class to interact with the Flower monitoring tool for Celery."""
    
    def __init__(self, authorization: str = "Basic ***", url: Optional[str] = None):
        """
        Initialize the Flower instance.

        :param authorization: Authorization header value (default is a placeholder).
        :param url: Base URL of the Flower instance.
        """
        if not url:
            raise ValueError("URL cannot be None or empty.")
        
        self.url = url.rstrip("/")
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Authorization': authorization,
            'Connection': 'keep-alive',
            'Priority': 'u=0',
        }

    def create_data_payload(self,count: int,columns:list=None) -> Dict[str, str]:
        """
        Generate the payload for the request.

        :param count: Number of rows to fetch.
        :return: A dictionary representing the payload.
        """
        columns = [
            "name", "uuid", "state", "args", "kwargs", "result", "received", "started", "runtime",
            "worker", "exchange", "routing_key", "retries", "revoked", "exception", "expires", "eta"
        ] if not columns else columns
        payload = {
            f"columns[{i}][data]": col for i, col in enumerate(columns)
        }
        payload.update({
            f"columns[{i}][searchable]": "true" for i in range(len(columns))
        })
        payload.update({
            f"columns[{i}][orderable]": "true" for i in range(len(columns))
        })
        payload.update({
            'draw': '1',
            'order[0][column]': '5',
            'order[0][dir]': 'asc',
            'start': '0',
            'length': str(count),
            'search[value]': '',
            'search[regex]': 'false',
        })
        return payload

    def get_flower_sorted_result(self, count: int = 50000) -> Optional[Dict]:
        """
        Fetch sorted results from the Flower server.

        :param count: Number of rows to fetch.
        :return: The parsed JSON response or None in case of failure.
        """
        try:
            base_url = self.url.strip("/tasks").strip("/workers")
            headers = self.headers.copy()
            headers['Origin'] = base_url
            headers['Referer'] = self.url

            data = self.create_data_payload(count)
            for _ in range(20):
                try:
                    response = requests.post(f"{self.url}/datatable", headers=headers, data=data,timeout=15)
                    if response:break
                except:
                    pass
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching data from Flower: {e}")
            return None

    def clean_result_data(self,result: Dict, clean_list: Optional[List[str]] = None) -> Dict:
        """
        Clean unnecessary fields from the result.

        :param result: The JSON result to clean.
        :param clean_list: List of fields to remove from the result.
        :return: The cleaned result.
        """
        default_clean_list = [
            "received", "sent", "started", "rejected", "succeeded", "failed", "retried", "revoked",
            "expires", "timestamp", "runtime", "exchange", "routing_key", "clock", "client", "eta",
            "root", "root_id", "parent", "parent_id", "children", "retries"
        ]
        clean_list = clean_list or default_clean_list

        if not result or "data" not in result:
            logging.warning("No valid result data to clean.")
            return {}

        for data in result.get("data", []):
            for field in clean_list:
                data.pop(field, None)

        return result

    def save_result_to_json(self,result: Dict, output_file: str = "source/flower_result.json") -> None:
        """
        Save the result to a JSON file.

        :param result: The cleaned JSON result.
        :param output_file: Output file name for the cleaned result.
        """
        try:
            with open(output_file, "w") as file:
                json.dump(result, file, indent=4)
            logging.info(f"Result saved to {output_file}")
        except (OSError, IOError) as e:
            logging.error(f"Failed to write to {output_file}: {e}")


