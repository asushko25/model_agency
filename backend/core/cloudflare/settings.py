try:
    from decouple import config
except ImportError:
    import os

    config = os.environ.get

CLOUDFLARE_R2_CONFIG_OPTIONS = {}

bucket_name = config("CLOUDFLARE_R2_BUCKET")
endpoint_url = config("CLOUDFLARE_R2_BUCKET_ENDPOINT")
access_key = config("CLOUDFLARE_R2_ACCESS_KEY")
secret_key = config("CLOUDFLARE_R2_SECRET_KEY")

if all([bucket_name, endpoint_url, access_key, secret_key]):
    CLOUDFLARE_R2_CONFIG_OPTIONS = {
        "bucket_name": bucket_name,
        "endpoint_url": endpoint_url,
        "access_key": access_key,
        "secret_key": secret_key,
        "default_acl": "public-read",
        "signature_version": "s3v4",
    }
