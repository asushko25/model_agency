from storages.backends.s3 import S3Storage

from ..storages_utill.acl_mixin import DefaultACLMixin


class CloudflareStorage(S3Storage):
    pass


class StaticFileStorage(CloudflareStorage, DefaultACLMixin):
    """
    For static files, like django admin site
    """

    location = "static"


class MediaFileStorage(CloudflareStorage, DefaultACLMixin):
    """
    For media files, like user uploaded images etc
    """
    location = "media"
