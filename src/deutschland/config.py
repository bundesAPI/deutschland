from typing import Dict


class Config:
    proxy_config = None

    def __init__(self, proxies: Dict[str, str] = None):
        if proxies is not None and isinstance(proxies, dict):
            self.proxy_config = proxies

    def set_proxy(self, http_proxy: str, https_proxy: str):
        if self.proxy_config is None:
            self.proxy_config = {}
        self.proxy_config.update({"http": http_proxy, "https": https_proxy})


module_config = Config()
