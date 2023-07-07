from typing import Dict


class Config:
    def __init__(self, proxies: Dict[str, str]):
        self.proxy_config = proxies or {}

    def set_proxy(self, http_proxy: str, https_proxy: str):
        """
        Sets the HTTP and HTTPS proxies to use.

        Args:
            http_proxy (str): The HTTP proxy to use.
            https_proxy (str): The HTTPS proxy to use.
        """
        self.proxy_config.update({"http": http_proxy, "https": https_proxy})


module_config = Config({})
