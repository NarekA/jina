from prometheus_client import CollectorRegistry


class MonitoringMixin:
    """The Monitoring Mixin for pods"""

    metrics_registry: CollectorRegistry

    def _setup_monitoring(self):
        """
        Wait for the monitoring server to start
        """

        if self.args.monitoring:
            from prometheus_client import CollectorRegistry

            self.metrics_registry = CollectorRegistry()
        else:
            self.metrics_registry = None

        if self.args.monitoring:

            from prometheus_client import start_http_server

            start_http_server(self.args.port_monitoring, registry=self.metrics_registry)