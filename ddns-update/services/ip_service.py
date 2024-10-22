import requests


class IP_Service:
    @staticmethod
    def get_public_ip() -> str:
        response = requests.get("https://api.ipify.org")

        if response.status_code != 200:
            raise Exception("Failed to fetch public IP")

        return response.text


ip_service = IP_Service()
