"""
This component has a test-case for testing
peer related operations
"""
# disruptive;

from tests.parent_test import ParentTest


class TestCase(ParentTest):
    """
    This TestCase class contains a function to test
    for peer probe , pool list and peer detach.
    """

    def run_test(self, redant):
        """
        In this testcase:
        1) Cluster is created.
        2) The storage pool is listed.
        """
        server1 = self.server_list[0]
        for _ in range(2):
            redant.create_cluster(self.server_list)
            node_list = redant.nodes_from_pool_list(server1)
            node_ip_list = redant.convert_hosts_to_ip(node_list, server1)
            redant.logger.info(node_ip_list)
            redant.delete_cluster(self.server_list)
            from time import sleep
            sleep(1)
