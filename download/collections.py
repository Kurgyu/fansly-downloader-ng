"""Download Fansly Collections"""


from .common import process_download_accessible_media
from .downloadstate import DownloadState
from .types import DownloadType

from config import FanslyConfig
from textio import input_enter_continue, print_error, print_info


def batch_list(input_list, batch_size):
    """Yield successive n-sized batches from input_list."""
    for i in range(0, len(input_list), batch_size):
        yield input_list[i:i + batch_size]


def download_collections(config: FanslyConfig, state: DownloadState):
    """Downloads Fansly purchased item collections."""

    print_info(f"Starting Collections sequence. Buckle up and enjoy the ride!")

    # This is important for directory creation later on.
    state.download_type = DownloadType.COLLECTIONS

    # send a first request to get all available "accountMediaId" ids, which are basically media ids of every graphic listed on /collections
    collections_response = config.http_session.get(
        'https://apiv3.fansly.com/api/v1/account/media/orders/',
        params={'limit': '9999','offset': '0','ngsw-bypass': 'true'},
        headers=config.http_headers()
    )

    if collections_response.status_code == 200:
        collections_response = collections_response.json()
        account_media_orders = collections_response['response']['accountMediaOrders']
        account_media_ids = [order['accountMediaId'] for order in account_media_orders]
  
        # Batch size based on API's limits
        batch_size = 150
  
        # Splitting the list into batches and making separate API calls for each
        for batch in batch_list(account_media_ids, batch_size):
            batched_ids = ','.join(batch)
            post_object = config.http_session.get(
                f"https://apiv3.fansly.com/api/v1/account/media?ids={batched_ids}",
                headers=config.http_headers())
            post_object = post_object.json()
  
            process_download_accessible_media(config, state, post_object['response'])

    else:
        print_error(f"Failed Collections download. Response code: {collections_response.status_code}\n{collections_response.text}", 23)
        input_enter_continue(config.interactive)
