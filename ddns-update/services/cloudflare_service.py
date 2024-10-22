import os
import requests
from dotenv import load_dotenv


class CloudflareService:
    def __init__(self, api_token: str):
        self.base_url = "https://api.cloudflare.com/client/v4"
        self.api_token = api_token

    def update_dns_record(self, zone_id, record_id, ip_address):
        response = requests.patch(
            f"{self.base_url}/zones/{zone_id}/dns_records/{record_id}",
            headers={
                "Authorization": f"Bearer {self.api_token}",
                "Content-Type": "application/json",
            },
            json={"content": ip_address},
        )

        if response.status_code != 200:
            raise Exception("Failed to update DNS record")

        return response.json()


load_dotenv()

if not os.getenv("CLOUDFLARE_API_TOKEN"):
    raise Exception("CLOUDFLARE_API_TOKEN environment variable must be set")
cloudflare_service = CloudflareService(os.getenv("CLOUDFLARE_API_TOKEN"))
