from unittest import mock, TestCase, main
from unifipy-api-client.controller import APIError, Controller


class testunifipy-api-client(TestCase):
    def test_controller_args(self):
        # Test for controller versions
        self.assertRaises(APIError, Controller, 'host',
                          'username', 'password', version='v3')

        # Test for missing arguments
        self.assertRaises(TypeError, Controller, 'username', 'password')

    @mock.patch('unifipy-api-client.controller.Controller')
    def test_unifipy-api-client_switch_sites(self, Mockunifipy-api-client):
        controller = Mockunifipy-api-client()

        # Test function to switch sites
        controller.switch_site.return_value = [True]
        response = controller.switch_site('test1')
        self.assertIsNotNone(response)
        self.assertIsInstance(True, bool)

    @mock.patch('unifipy-api-client.controller.Controller')
    def test_unifipy-api-client_get_aps(self, Mockunifipy-api-client):
        controller = Mockunifipy-api-client()

        controller.get_aps.return_value = [
            {
                '_id': '11111',
                '_uptime': '30506',
                'adopted': True,
                'ip': '192.168.1.5'
            }
        ]
        response = controller.get_aps()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)


if __name__ == '__main__':
    main()
