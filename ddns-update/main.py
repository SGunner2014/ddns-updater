# Fetches public IP address and updates cloudflare dns records accordingly
import os
import logging

from dotenv import load_dotenv

from services import ip_service, cloudflare_service


def main():
    load_dotenv()

    logger = logging.getLogger()

    zone_id = os.getenv("ZONE_ID")
    record_id = os.getenv("RECORD_ID")

    if not zone_id or not record_id:
        raise Exception("ZONE_ID and RECORD_ID environment variables must be set")

    logger.info("Fetching public IP address")
    public_address = ip_service.get_public_ip()
    logger.info(f"Public IP address: {public_address}")

    logger.info("Updating DNS record")
    cloudflare_service.update_dns_record(zone_id, record_id, public_address)
    logger.info("DNS record updated successfully")


if __name__ == "__main__":
    main()
